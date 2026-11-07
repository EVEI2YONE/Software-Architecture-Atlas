# B17 — Trusted trading market-data integrity

**Research date:** 2026-11-07 · **Scope:** Final Expanse Phase 5 spot-market data and automated paper-bot strategy inputs · **Research state:** source-backed reference delivered; application integration and live-network validation not attempted.

## Context and deduplication

The Atlas's existing [API contracts](../concepts/distributed-systems/api-contracts.md), [resilience](../concepts/operations/resilience.md), [idempotency](../concepts/distributed-systems/idempotency.md), [B15 transactions](batch-15-postgresql-concurrency.md), and [B16 worker fencing](batch-16-worker-leases-fencing.md) cover adjacent responsibilities but do not define exchange-data candle finality, timestamp provenance, pair aliases, order constraints or user eligibility. One canonical [Trading market-data integrity and decision eligibility](../concepts/data/trading-market-data-integrity.md) concept was added to avoid repeating the generic principles.

## Evidence gathered

Kraken Developers' current Spot REST OHLC documentation explicitly identifies the last response item as an unfinished candle and notes that no more than 720 recent entries can be retrieved. Kraken Spot WebSocket v2 OHLC documentation describes trade-driven updates. Kraken AssetPairs responses document internal/display identifiers, market status, tick size, size/cost minimums and precision. Kraken's support article explains differences in REST/WebSocket symbols. Public reference data does not identify an individual account's permissions or location eligibility.

These are cited vendor-documented behaviors, **not** live API results from a Final Expanse worker. Source freshness and future API changes still need checks.

## B17 deliverables

1. Indexed, source-backed concept covering source provenance, venue/symbol mapping, interval finality, OHLC constraints, exact decimal parsing, stale/gapped observations, pair metadata, and independent account eligibility.
2. Proposed data lineage fields and explicit quality versus authorization state machines.
3. Illustrative closed-candle selection and clear warning that excluding the unfinished Kraken row does **not** finish all validation.
4. Failure/skip fixture matrix: unfinished candle, insufficient history, out-of-order/duplicate samples, stale observations, mismatched base/quote, invalid prices, HTTP-200 exchange errors, partial outages, expired metadata, unsupported pair status and account ineligibility.
5. Explicit restriction that a market being listed via a public API cannot authorize a trade.
6. Links to existing Atlas concepts and canonical/natural-language retrieval regression cases.

## Final Expanse verification handoff (not executed)

| Product checkpoint | Test requirement | Expected observable result |
| --- | --- | --- |
| Kraken REST adapter | Live read-only OHLC and AssetPairs smoke tests, contract fixtures | Parsing handles documented shapes and errors |
| Strategy input | Closed interval, strict timestamps, sufficient history | Unfinished/stale/gapped candles produce SKIP, not an order |
| Market metadata | Internal/display symbols, base/quote, decimal minimums and tick size | Wrong identity or minimums rejected; no guessed mapping |
| Trading permission | Authenticated account exchange rights and jurisdiction policy | Unknown eligibility rejects execution despite public listing |
| Worker replay | Re-run validated candle after restart | B16 fencing and B15 unique receipt prevent duplicate financial effect |
| UI recovery | Present unavailable/stale/unknown states | User does not see fabricated current pricing |
| Paper execution realism | Explicit server-owned price and fill assumptions | No claim that candle closing price equals executable fill price |

The Atlas has no access to validated Final Expanse production exchange credentials, compliance state or user account eligibility for this research batch.

## B17 validation checks

~~~sh
python scripts/validate_catalog.py
python scripts/validate_documentation.py
python -m unittest discover -s tests -v
python scripts/search_catalog.py "trading-market-data-integrity" --json
python scripts/search_catalog.py "trading market data integrity" --json
~~~

These verify documentation metadata and catalog retrieval, not correctness of real exchange requests or market prices. CI must be observed independently.

## Forward work

B18 addresses worker observability, hosted identity/tenant controls and frontend build verification. B19 will audit cross-concept consistency, sources and retrieval. No Final Expanse implementation code is changed here.
