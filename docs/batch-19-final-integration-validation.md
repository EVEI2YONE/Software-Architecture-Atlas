# B19 — Cross-batch integrity, retrieval evaluation and Final Expanse handoff

**Assessment date:** 2026-11-07 · **Shared PR:** #5 · **Scope:** B15–B18 research addressing Final Expanse's six named blockers. **Exit state:** See GitHub Actions for code/metadata regression results; **application-level production blockers remain open**.

## 1. Context, canonical ownership and deduplication

Read the canonical index, taxonomy, evidence policy, existing general concepts, four research reports, new pages and B18 runbook before consolidation. New references were added only where generic guidance lacked a stable focused concept.

| Batch | Canonical owner / artifact | Reused existing knowledge | What is deliberately NOT duplicated |
| --- | --- | --- | --- |
| B15 | [PostgreSQL transactional concurrency](../concepts/data/postgresql-transactional-concurrency.md) | transactions, isolation-levels, transactional-invariants, data-access-boundaries | Generic ACID/DDD treatment |
| B16 | [Durable worker leases and fencing](../concepts/distributed-systems/durable-worker-leases-and-fencing.md) | idempotency, queues, delivery-guarantees, runtime locks, B15 | Generic queues/retry patterns |
| B17 | [Trading market-data integrity](../concepts/data/trading-market-data-integrity.md) | api-contracts, resilience, B15/B16 | Generic HTTP contracts or financial execution authorization |
| B18 | [Production verification runbook](batch-18-production-verification.md) with **five existing concept extensions** | observability, reliability-objectives, identity-and-access, package-locking-and-version-policy, testing-strategy | New canonical categories or duplicate concepts |
| B19 | This integration report and executable catalog/regression checks | B15–B18, evidence-policy, retrieval-evaluation | New architectural theory |

**Inventory:** 96 canonical concepts, including exactly three new focused entries from B15–B17 and zero new B18/B19 canonical concepts. Existing pages remain canonical and B18 guidance is a linked practical overlay, not a new identity or observability standard.

## 2. Terminology and invariant consistency

| Term or boundary | Shared meaning | Guardrail |
| --- | --- | --- |
| **Transaction** | One local database unit of work with atomic commit/rollback | Does not atomically include external exchange/API requests |
| **Short claim lock** | Database row selection/update protected until commit | Does not guarantee ownership throughout a subsequent slow evaluation |
| **Lease** | Expiring claim that enables another actor to take over | Does not cancel or stop the expired worker |
| **Fencing generation** | Monotonic ownership/version token enforced at the authoritative effect | A token merely logged or checked before remote I/O is not fencing |
| **Business idempotency key** | Stable identity for the *same* business evaluation/effect | Different from changing lease generation; document replay/conflict |
| **Valid market observation** | Source-attributed, temporally and numerically validated input | Does not authorize any trading account or real order |
| **Trade eligibility** | Independently verified account/venue/market permissions and policy | Public AssetPairs discovery and system status are insufficient |
| **SKIP / HOLD** | SKIP = unable/unauthorized to evaluate; HOLD = valid evaluation with no actionable signal | Never turn missing/stale market data into a success-like HOLD |
| **Worker liveness** | Process responds according to a specific probe | Does not show useful processing, progress or safe financial effects |
| **Hosted authentication** | Verified identity from an OIDC provider and a protected session | Not sufficient for cross-tenant authorization |
| **Frontend source tests** | Source-level contract expectations | Not a TypeScript compile, browser execution or accessibility audit |
| **Reviewed concept** | Metadata complete and scoped primary references supplied | Not a source-claim entailment certificate or target-system validation |

## 3. Sampled source-to-claim audit

Evidence is classified using [evidence policy](evidence-policy.md). The following are **sampled checks**, not a full audit of every citation across 96 concepts.

| Reference | Claim scoped and checked | Result / remaining limitation |
| --- | --- | --- |
| [PostgreSQL 18 SELECT](https://www.postgresql.org/docs/18/sql-select.html) | FOR UPDATE/SKIP LOCKED row-lock behavior; queue-like use caveats | Primary vendor source checked; deployed schema/lock behavior untested |
| [PostgreSQL 18 Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html) | Isolation-specific retries after serialization conflict | Source-backed; example retry algorithms remain proposed |
| [SQLAlchemy 2.0 Session Transactions](https://docs.sqlalchemy.org/en/20/orm/session_transaction.html) | Unit-of-work context and transaction boundaries | Source-backed; snippets intentionally require application models |
| [Kleppmann's fencing analysis](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html) | Expired worker can continue; resource must reject stale actor | Original engineering analysis; proposed PostgreSQL design not tested |
| [Kraken REST OHLC](https://docs.kraken.com/api-reference/market-data/get-ohlc-data) | Final OHLC element is unfinished, bounded historic response | Primary exchange documentation confirmed; current network behavior untested |
| [Kraken WebSocket v2 OHLC](https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/ohlc) | Stream updates depend on trades | Primary exchange documentation confirmed; no real socket test |
| [Kraken Spot error guide](https://docs.kraken.com/exchange/guides/general/errors) | Non-empty response error array indicates error | Canonical URL updated from redirect during B19 |
| [RFC 10017](https://www.rfc-editor.org/rfc/rfc10017.html) | August 2026 browser OAuth architecture and BFF/PKCE advice | Primary published BCP confirmed; actual identity provider settings untested |
| [Vite TypeScript features](https://vite.dev/guide/features) | Vite transpiles TS without performing type checking | Vendor documentation confirmed; must run separate actual tsc |
| [npm ci](https://docs.npmjs.com/cli/v11/commands/npm-ci/) | Clean locked install is required to establish reproducibility | Vendor-specified command, not evidence of a successful application install |

**Classification:** Primary cited behavior is **source-supported** at the listed version and audit date; application-oriented architectures, thresholds, SQL schemas, metrics and test matrices remain **inferred/proposed**. Existing sources and all other catalog pages were **not comprehensively live-URL or claim-entailment audited**. Vendor URLs can change; verify again before implementation.

## 4. Six blocker-to-concept handoff matrix

| Final Expanse blocker | Primary Atlas entry | Supporting guidance | Required verification in Final Expanse (NOT DONE by Atlas) |
| --- | --- | --- | --- |
| Real PostgreSQL multi-worker/financial concurrency | [B15 PostgreSQL concurrency](../concepts/data/postgresql-transactional-concurrency.md) | [B15 report](batch-15-postgresql-concurrency.md), transactional-invariants | Real PostgreSQL, multiple independent connections/processes; overspend, rollback, migration, receipts and retries |
| Leases, renewal, stale-worker fencing and restart | [B16 worker fencing](../concepts/distributed-systems/durable-worker-leases-and-fencing.md) | [B16 report](batch-16-worker-leases-fencing.md), idempotency | Expire/reclaim old lease, block old generation on every local effect, crash/replay and no duplicate fills |
| Background monitoring and operational recovery | [Observability](../concepts/operations/observability.md) | [Reliability objectives](../concepts/operations/reliability-objectives.md), [B18 runbook](batch-18-production-verification.md) | Deployed progress metrics, actual alerts, response owners, operator halt, failure injection, RTO/RPO recovery |
| Hosted login, sessions, account/tenant ownership | [Identity and access](../concepts/governance/identity-and-access.md) | [B18 OIDC runbook](batch-18-production-verification.md), threat-modeling | Provider integration, PKCE/state, tokens/sessions, negative cross-tenant API and worker tests on hosted domains |
| Trusted Kraken market data and eligibility | [B17 market integrity](../concepts/data/trading-market-data-integrity.md) | [B17 report](batch-17-trading-market-data-integrity.md), API contracts | Real read-only Kraken contract smoke, candle finality/freshness, mapping, account/jurisdiction permission, SKIP and idempotent replay |
| React/Vite build, browser and accessibility acceptance | [Testing strategy](../concepts/quality/testing-strategy.md) | [Package locking](../concepts/dependencies/package-locking-and-version-policy.md), [B18 runbook](batch-18-production-verification.md) | Clean npm ci, TypeScript check, Vite build, real browser auth/API flow, keyboard/axe/assistive tech and mobile tests |

This is the explicit separation between **research knowledge filled** and **product blockers resolved**. It is never permissible to move an implementation item to "passed" based solely on Atlas catalog CI.

## 5. Agent retrieval evaluation

The repository's deterministic lexical search and [golden fixture](../tests/fixtures/retrieval_gold.json) are a lookup aid, not source verification. B15–B17 added canonical ID and natural-language cases. B19 also tests that the shared blocker handoff contains all six blockers and all three focused canonical entries, that each B18 extension reaches its runbook, and that its core terminology remains distinguishable.

### Expected agent workflow

1. Search `catalog/index.json` by the blocker; prefer canonical exact ID or 2–5 candidate results.
2. Verify the selected concept's category, path, status, versioned sources and counterexamples.
3. Follow relevant B15–B18 research report and test matrix; read cross-linked concepts only when necessary.
4. Determine whether recommendation is **observed**, **supported**, **inferred** or **unknown** under the evidence policy.
5. Apply the smallest justified change to the actual software and run target-specific tests; do not infer production readiness.
6. Report negative results and unresolved validation separately from the knowledge index.

### Retrieval negative-control policy

A generic query such as "authentication" should not automatically force the much narrower market-data page; conversely a nonexistent ID should remain unmatched. Hand-picked gold cases are necessary but insufficient for independent search relevance; B19 deliberately does not claim semantic retrieval precision, held-out human-query accuracy or source citation correctness.

## 6. CI and exit criteria

Required repository checks (run in GitHub Actions after the last B19 change):

~~~sh
python scripts/validate_catalog.py
python scripts/validate_documentation.py
python -m unittest discover -s tests -v
python scripts/search_catalog.py "postgresql-transactional-concurrency" --json
python scripts/search_catalog.py "durable-worker-leases-and-fencing" --json
python scripts/search_catalog.py "trading-market-data-integrity" --json
~~~

Catalog and document validators check metadata, links and counts. Unit tests check deterministic offline retrieval and the B18/B19 reference handoffs. They do **not** execute PostgreSQL, Kraken, identity-provider, worker, browser or production monitoring checks.

**Research exit:** Complete when CI is green on the final PR head and B15–B19 documentation, glossary and handoff are indexed and internally consistent. **Application exit:** Remains open until Final Expanse demonstrates all environment-specific verification listed above.

## 7. Revisit triggers

Review this research when Kraken API schemas or trade restrictions change; PostgreSQL/SQLAlchemy versions are upgraded; workers change delivery or ownership technology; hosted identity design changes; Vite/Node changes break builds; a new incident disproves an assumption; or a Final Expanse integration test reveals a counterexample. Preserve failure evidence and revise canonical concepts rather than altering historical reports without explanation.
