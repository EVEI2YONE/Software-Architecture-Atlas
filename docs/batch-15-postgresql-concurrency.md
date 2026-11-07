# B15 — PostgreSQL concurrency and transactional integrity

**Research date:** 2026-11-07. **Scope:** Final Expanse Phase 5 PostgreSQL, SQLAlchemy, concurrent customer accounts, paper capital and durable scheduling. **State:** source-scoped reference written; live PostgreSQL verification remains open.

## Context reviewed

Canonical Atlas entries already covered [transactions](../concepts/data/transactions.md), [isolation levels](../concepts/data/isolation-levels.md), [data-access boundaries](../concepts/data/data-access-boundaries.md), [transactional invariants](../concepts/domain-design/transactional-invariants.md), and [idempotency](../concepts/distributed-systems/idempotency.md). The Atlas is a reference catalog; none of these pages demonstrates Final Expanse multi-worker correctness. The application previously relied primarily on SQLite-based integration checks; those cannot substitute for a real PostgreSQL race test.

## Delivered B15 knowledge

- One new [PostgreSQL transactional concurrency and SQLAlchemy](../concepts/data/postgresql-transactional-concurrency.md) focused entry, **not** a duplicate general transaction article.
- Short SQLAlchemy Session transaction pattern with pessimistic row locking, exception rollback and explicit illustration boundaries.
- Decision matrix: READ COMMITTED versus SERIALIZABLE when justified, row locks, SKIP LOCKED queue claiming, unique idempotency keys, cross-row predicates and remote side-effects.
- Monetary, capital-reservation and tenant invariants to prove in target software.
- Real PostgreSQL, multi-connection/process **proposed test matrix**: overspend, duplicate replay, write skew, deadlocks, SERIALIZABLE errors, timeouts, crash-before/after-commit, parallel claims, cross-tenant access and connection pools.
- Existing concept cross-links, index metadata, browse path and retrieval gold queries.

## Source applicability and uncertainties

Sources: PostgreSQL 18 transaction isolation, SQL SELECT, locking and constraints; SQLAlchemy 2.0 Session transaction and concurrency documentation. The sample is illustrative, not runnable standalone; it intentionally relies on application-specific mapped tables, exceptions, validated actor identity and persisted reservation receipts. Database locks do not replace expiring worker leases or fencing (B16).

No PostgreSQL instance, actual Final Expanse schema/driver, production market access, financial ledger, benchmark, recovery drill or multi-worker load test was run during this Atlas research batch. Reviewed status is **not** an independently audited proof of the prose or production safety.

## Verification commands for PR

~~~sh
python scripts/validate_catalog.py
python -m unittest discover -s tests -v
python scripts/search_catalog.py "postgresql-transactional-concurrency" --json
python scripts/search_catalog.py "postgresql transactional concurrency" --json
~~~

Catalog metadata and tests must pass before final acceptance. The golden retrieval fixture must not imply query relevance beyond its hand-picked expected queries.

## Final Expanse handoff

| Blocker | Use B15 guidance to implement | Required application evidence |
| --- | --- | --- |
| PostgreSQL concurrency | Row lock/constraint strategy and retry policy | Actual real-PostgreSQL concurrent balance + receipt tests |
| Worker race | Atomic short claim transaction | B16 lease/fencing and multi-process failure tests still needed |
| Financial correctness | Atomic exact-money available/reserved and receipt writes | Schema constraints, multi-tenant negative tests, ledger reconciliation |
| Transaction migration | Production-like schema/locking/rollback rehearsal | Migration timing, old/new compatibility, actual restore drill |

**B15 boundary:** scoped reference guidance delivered. **Not resolved:** Final Expanse PostgreSQL deployment or concurrency blocker; implementation verification remains necessary.
