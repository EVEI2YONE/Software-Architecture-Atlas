---
id: trading-market-data-integrity
title: "Trading market-data integrity and decision eligibility"
category: data
status: reviewed
reviewed_at: 2026-11-07
---

# Trading market-data integrity and decision eligibility

> **Reviewed, scoped research guidance—not a certified data feed or trading strategy.** Kraken Spot REST and WebSocket details are based on Kraken's published API documentation, accessed 2026-11-07. The normalized contract, validation order, statuses and tests below are **proposed architectural practices**, not vendor-prescribed universal policies or executed Final Expanse tests. No profitability or suitability claim is made.

## Problem, scope and boundaries

A successful market-data HTTP response does **not** establish that observations are final, current, complete, internally consistent, attributable to the right instrument, or suitable for a particular user's trading decision. A public exchange listing also does **not** establish account, geographic, permission, or order eligibility.

This page extends the general [API contracts](../distributed-systems/api-contracts.md), [resilience](../operations/resilience.md), and [idempotency](../distributed-systems/idempotency.md) guidance with a focused **spot-market data validation boundary**. B15/B16 own transaction integrity and worker fencing; this concept owns the data quality of strategy inputs. Paper-price modeling, live order authorization and financial ledgers are separate concerns.

## Kraken Spot-specific source facts

- Kraken's REST OHLC endpoint explicitly includes an entry for the **current unfinished timeframe** as its final element, even when using `since`; that element is not a confirmed closed candle. The endpoint returns **at most 720 recent entries**, not unlimited history [1]. Never feed the last element into a strategy that requires confirmed candles.
- Kraken's WebSocket v2 OHLC channel emits updates **when trade events occur**. No recent update is not proof that a stream is current; snapshot-versus-update and event timing must be understood [2].
- Kraken's `AssetPairs` response includes instrument identifiers, base/quote, order minimums, cost minimums, lot/price precision, tick size and pair status in documented responses. Internal REST identifiers can differ from display symbols and WebSocket representations [3, 4].
- Kraken provides public system status [5]. Public system/pair status does **not** replace authenticated account-level exchange permissions or jurisdiction-specific eligibility checks.
- Kraken Spot error messages may identify failures of order minimum, minimum notional/cost, and tick-size rules. A market-data listing is not advance proof every order is valid [6].

Only the documented endpoint/version behavior is a source-backed exchange fact. Freshness allowances, history requirements, anomaly limits, fallback behavior, and eligibility policy are product decisions and require verification.

## Proposed normalized data lineage contract

An adapter should preserve original fields alongside a normalized, immutable observation. Illustrative field groups:

| Field group | Minimum fields | Validation question |
| --- | --- | --- |
| Provenance | `venue`, `endpoint`, `api_version`, `retrieved_at_utc`, source key, request parameters | Which actual source and query supplied this observation? |
| Instrument | canonical internal market ID, raw pair ID, base/quote, mapping version, market type = spot | Does it refer to the same market, quote currency and venue as the configured bot? |
| Time | interval, candle open, candle close/exclusive boundary, source event/update time if available, receipt time | Is this interval complete, ordered and not implausibly future-dated? |
| Values | open/high/low/close, volume, optional count, exact decimal representation | Are values finite, positive where required, internally consistent and in documented units? |
| Quality | finality classification, gap/duplicate status, freshness class, reason codes, validation ruleset version | Why was this observation accepted, rejected, or withheld? |
| Market metadata | `status`, `ordermin`, `costmin`, `tick_size`, `lot_decimals` or equivalent | Are instrument rules current enough for this operation? |
| Decision linkage | bot ID, configuration revision, ordered validated candle identifiers, evaluation timestamp | Can a later reviewer reproduce the strategy input and skip/hold decision? |

Distinguish **exchange event time** from **our time of receipt**. Never invent an event timestamp when the provider does not supply one. Persist the raw source key, normalized mapping and ruleset version needed to explain a historical decision. Apply a bounded retention/privacy policy to raw payloads.

## Validation pipeline — fail closed

1. **Transport and schema:** Enforce timeouts, response size, content type and authenticated TLS; inspect exchange-specific error arrays even when HTTP status is successful. Unknown response shapes and partial payloads are unavailable, not neutral observations.
2. **Market identity:** Resolve raw identifiers using versioned exchange reference data, not string substitution alone. Verify venue, spot type, base, quote and configured market. Reject ambiguous or conflicting aliases.
3. **Finality:** For Kraken REST OHLC, exclude the last unfinished interval by contract [1]. For other feeds, prove the interval's closure using that provider's semantics; do not assume a snapshot message means final.
4. **Temporal integrity:** Convert source times to UTC with explicit units; enforce strict ordering, interval boundaries, no unjustified future event time and no duplicates masquerading as a new candle. Handle clock uncertainty explicitly.
5. **History completeness:** Check the strategy-required window and gap policy. A 720-entry endpoint limit or missing periods can make an indicator unavailable. Out-of-order updates must not silently rewrite previously accepted evidence.
6. **Numerical integrity:** Parse numeric strings as exact decimals where appropriate. Reject NaN, infinities, impossible prices, negative volume, or OHLC relationships such as high below open/close or low above open/close. The treatment of true zero-volume intervals must be source- and strategy-specific; do not fabricate trades.
7. **Freshness:** Compare newest **confirmed** observation to a product-approved maximum age for the interval/strategy and current operating mode. Log measured age; do not use an arbitrary global freshness threshold or treat WebSocket silence as healthy.
8. **Feed conflict and status:** If independent sources disagree outside a defined tolerance, or a source is stale/degraded, mark input unavailable pending reconciliation; do not average disagreements into a synthetic "truth" by default.
9. **Trading eligibility as a separate gate:** Public pair metadata is necessary context but insufficient for user-level eligibility. Before any consequential execution, independently verify account authentication/permissions, jurisdiction, exchange status, instrument restrictions, current precision/minimums and risk. Unknown eligibility means **not authorized**.
10. **Decision record:** Persist validated input identifiers, policy version and reasons. AI research or model sentiment is advisory, never a substitute for market-data validation or independent risk authorization.

### Data-quality states versus authorization states

These are *illustrative application states*, not Kraken API enums.

| Data state | Meaning | Strategy decision |
| --- | --- | --- |
| `VALIDATED_CLOSED` | Complete and acceptable confirmed history | May evaluate strategy; **not** permission to execute |
| `PROVISIONAL` | Open/unfinished candle or unconfirmed update | Skip for closed-candle strategies |
| `STALE` | Newest confirmed observation outside approved age | Skip and surface data-age reason |
| `GAPPED` | Insufficient or inconsistent history | Skip or approved explicit gap policy; never silently interpolate |
| `AMBIGUOUS_MARKET` | Missing/changed/conflicting instrument mapping | Skip; investigate mapping |
| `SOURCE_UNAVAILABLE` | Timeout, rate limit, exchange error, parse failure | Skip; bounded safe retry by worker policy |
| `INCONSISTENT` | Impossible values, conflicting feeds, duplicates with changed payload | Skip and quarantine for investigation |

Eligibility states should be **separately modeled** as `ELIGIBLE`, `INELIGIBLE`, and `UNKNOWN`. Only `ELIGIBLE` can pass that gate, and validation alone never grants risk/execution authority. A rejected input should not be disguised as a momentum HOLD signal.

## Kraken example — closed-candle selection

~~~python
# Illustrative adapter boundary, NOT a complete Kraken client.
# Kraken Spot REST OHLC last array row is the still-open interval [1].
def eligible_closed_rows(kraken_ohlc_rows, *, required_count: int):
    if required_count <= 0:
        raise ValueError("required_count must be positive")
    if len(kraken_ohlc_rows) < required_count + 1:
        return ("SKIP_INSUFFICIENT_HISTORY", [])
    candidates = kraken_ohlc_rows[:-1]
    # A production validator must ALSO check timestamps, order, gaps,
    # interval boundaries, market identity, freshness and numeric integrity.
    return ("CANDIDATES_REQUIRE_VALIDATION", candidates[-required_count:])
~~~

Never mistake this shortlist for validated input. In a quiet market, lack of trades/updates may make older closed candles stale; validate actual candle times [2]. Capture the configured interval and last validated candle ID when recording an idempotent bot evaluation [7].

## Instrument identity, precision, and order constraints

Treat the normalized market key as a composite of exchange identity + spot market identity + base/quote + mapping version where needed. Kraken's documented internal symbols, `altname`/`wsname`, and display names can differ [3, 4]. Maintain explicit mappings and detect market renames/delistings.

For any eventual order, use current exchange instrument metadata for `tick_size`, `ordermin`, `costmin` and supported lot/price precision; perform exact-decimal quantization and re-check notional **after** rounding. A minimum order size is not evidence the account is eligible or the market is currently online. Exchange acceptance/rejection remains the final external fact, but it does not replace local pre-trade authorization [3, 6].

## Adversarial fixtures and negative verification plan — NOT EXECUTED

| Fixture / fault | Expected decision | Required evidence |
| --- | --- | --- |
| Kraken REST returns final in-progress row | `PROVISIONAL`; do not evaluate it | Raw row count and interval, selected confirmed IDs |
| Not enough rows after excluding final element | `GAPPED` / insufficient history | Strategy window and available confirmed count |
| Duplicate time with different prices | `INCONSISTENT` | Both source observations retained for diagnosis |
| Out-of-order rows or missing intervals | `GAPPED` / reject | UTC interval sequence and rule |
| Old confirmed candles with recent HTTP receipt | `STALE` | Separate source and receipt timestamps |
| Future timestamp or mixed seconds/milliseconds | `INCONSISTENT` | Unit conversion and clock checks |
| Non-finite/negative price, high lower than low | `INCONSISTENT` | Numeric and OHLC constraints |
| Kraken error array populated despite HTTP 200 | `SOURCE_UNAVAILABLE` | Endpoint error category, no strategy execution |
| Internal XBT/XXBT symbol mapped to wrong base/quote | `AMBIGUOUS_MARKET` | Raw and canonical pair mapping |
| Pair maintenance/cancel-only/post-only restrictions | `INELIGIBLE` for unsupported operation | Current pair and system metadata |
| Unknown user jurisdiction or account trade rights | `UNKNOWN`, reject trading | No assumption from public AssetPairs |
| Wrong precision or below minimum after rounding | Reject proposed order | Decimal quantization/min notional checks |
| Two sources disagree outside defined tolerance | `INCONSISTENT` | Conflict and source precedence policy |
| Replayed candle following worker restart | Same idempotent evaluation, no second fill | B16 fencing and unique business receipt |
| Stale cached pair rules | Pause/skip operation | Metadata refresh/expiry and reason code |
| WebSocket disconnect / no trade events | Validate actual time; do not assume healthy | Last event and receipt timestamps |

Set policy thresholds explicitly per interval and risk appetite; calibrate with observed exchange behavior. Paper-fill simulation price assumptions require a separate slippage/liquidity model, not merely an OHLC close; none of this validates fill realism or strategy profitability.

## Verification and rollback handoff

For Final Expanse, run fixture-based parser contract tests, live read-only Kraken REST and WebSocket smoke tests, deterministic strategy inputs with injected time, gap/replay tests, account permission checks, and paper-simulation reconciliation. Validate before enabling any live trading. During source regression, fail closed to `SKIP`, surface a user-facing reason and preserve prior validated evidence. Do **not** fall back from an invalid source to unreviewed/unattributed alternate prices.

## Search aliases

kraken spot OHLC uncommitted candle; market data freshness; closed candle validation; exchange source provenance; symbol normalization; ordermin costmin tick size; financial market data integrity; out of order candles; market eligibility; trusted trading price

## Related concepts

- [API contracts](../distributed-systems/api-contracts.md)
- [Resilience](../operations/resilience.md)
- [Idempotency](../distributed-systems/idempotency.md)
- [Durable worker fencing](../distributed-systems/durable-worker-leases-and-fencing.md)
- [PostgreSQL transactional concurrency](postgresql-transactional-concurrency.md)

## Evidence and sources

1. Kraken Developers, Spot REST Get OHLC Data: https://docs.kraken.com/api-reference/market-data/get-ohlc-data (accessed 2026-11-07). Unfinished last candle and bounded 720-entry historical data.
2. Kraken Developers, Spot WebSocket v2 OHLC: https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/ohlc (accessed 2026-11-07). Trade-driven streaming update and snapshot schema.
3. Kraken Developers, Get Tradable Asset Pairs: https://docs.kraken.com/api-reference/market-data/get-tradable-asset-pairs (accessed 2026-11-07). Instrument metadata examples, precision, minimums and status.
4. Kraken Support, API Symbols and Tickers: https://support.kraken.com/articles/360000920306-api-symbols-and-tickers (accessed 2026-11-07). REST and WebSocket symbol differences.
5. Kraken Developers, Get System Status: https://docs.kraken.com/api-reference/market-data/get-system-status (accessed 2026-11-07). Public exchange status endpoint.
6. Kraken Developers, Spot Error Messages: https://docs.kraken.com/api/docs/guides/spot-errors/ (accessed 2026-11-07). Minimum notional/order size and tick-size rejection categories.
7. IETF RFC 9110, HTTP Semantics: https://www.rfc-editor.org/rfc/rfc9110.html (accessed 2026-11-07). HTTP behavior is separate from application business-effect idempotency.

## Maintenance

Reviewed 2026-11-07. Verify deployed Kraken API versions, exact provider response semantics, account/jurisdiction policy, actual exchange behavior and regression outputs before deploying. No financial, compliance, or security certification follows from catalog validation.
