---
id: transactions
title: "Transactions and boundaries"
category: data
status: reviewed
reviewed_at: 2026-11-07
---

# Transactions and boundaries

> **Reviewed — scoped PostgreSQL-oriented guidance; not a claim about any application's consistency.**

## Decision
Keep transactions scoped to invariants that truly must commit together. A transaction isolation choice affects which concurrent anomalies are excluded; PostgreSQL 18 documentation explains Read Committed, Repeatable Read and Serializable, and notes that serialization failures can require retrying an entire transaction [1].

## Practical questions
- What business invariant spans these writes, and can the transaction be local to one database?
- Are concurrent updates, conflicts and retries tested under representative workloads?
- Do external API calls or messages cross the boundary? A database commit does not atomically commit arbitrary remote effects.
- Would a single local transaction be simpler than distributed orchestration?

## Failure cases and tests
Check lost-update/write-skew scenarios, rollback on exceptions, lock waits, transient serialization failures and duplicate requests. PostgreSQL sequences need special care because their changes are not rolled back like ordinary transaction writes [1]. Never automatically retry a transaction with non-idempotent external effects.

## Migration and rollback
Inspect transaction scope, add concurrency tests and monitor conflicts before changing isolation. Stage changes, compare correctness and contention, and restore the previous isolation/queries if regressions occur after confirming data integrity.

## Search aliases
ACID; transaction isolation; serializable; data integrity; database boundary

## Related concepts
- [aggregates](../domain-design/aggregates.md)
- [consistency](../distributed-systems/consistency.md)
- [schema evolution](schema-evolution.md)

## Evidence and sources
1. PostgreSQL 18 Documentation, *Transaction Isolation*: https://www.postgresql.org/docs/18/transaction-iso.html (accessed 2026-11-07). PostgreSQL-specific semantics; other databases differ.
2. RFC 9110 *HTTP Semantics*: https://www.rfc-editor.org/rfc/rfc9110.html (accessed 2026-11-07). HTTP retry safety is separate from database atomicity.

## Maintenance
Reviewed 2026-11-07; revisit for database engine/version changes, observed anomalies and workload changes.
