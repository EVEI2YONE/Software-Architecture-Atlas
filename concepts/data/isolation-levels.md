---
id: isolation-levels
title: "Database isolation levels"
category: data
status: reviewed
reviewed_at: 2026-11-07
---

# Database isolation levels

> **Reviewed, scoped source-backed guidance.** Architecture examples and selection heuristics are inferences; no external application, business invariant, performance or data integrity was tested.

## Problem and context
Two concurrent transactions each observe a valid snapshot but jointly violate a business constraint.

## Applicability
Apply after identifying actual business terminology, service and data ownership, storage engine/version, workload, transaction invariants and deployment boundaries. DDD terminology here is based predominantly on Microsoft's .NET-oriented architectural materials, not a mandate for a .NET implementation or microservice deployment.

## Decision and trade-offs
Choose isolation levels by supported anomaly guarantees, workload contention and retry semantics of the actual database engine. PostgreSQL Read Committed, Repeatable Read and Serializable are not interchangeable with other engines' identically named settings.

### Simpler/no-change option
Use Read Committed plus appropriate row constraints and locks where sufficient; elevate isolation only if invariant/concurrency tests justify it.

### Failure modes and counterexamples
Serializable can abort transactions requiring retries of the whole unit of work; do not blindly replay external effects. Different databases provide different phantom and snapshot behavior.

## Illustrative workflow
For an Orders capability, trace request or scheduled-job entrypoint, application coordination, business policy, owned persistence, published contracts and tests. Keep one cohesive deployable when it meets requirements; consider stronger boundaries only for observed independent semantics, transaction guarantees or ownership needs. Domain events must not be confused with guaranteed external message delivery.

## Implementation, verification and rollback
Reproduce concurrent schedules and measure conflicts, lock waits, throughput and retry rate; verify a rollback strategy before changing isolation. Record project-specific observations, negative tests, release/migration compatibility, and a reversible no-change option. Separate database transaction guarantees from cross-process coordination.

## Search aliases
database isolation levels; isolation levels; domain boundaries; transactional consistency; business ownership

## Related concepts
- [transactions](../data/transactions.md)
- [transactional-invariants](../domain-design/transactional-invariants.md)
- [schema-evolution](../data/schema-evolution.md)

## Evidence scope and uncertainty

PostgreSQL-specific isolation behavior should be checked against the exact database engine/version; Azure CQRS guidance is background context for read/write model separation rather than an authority for SQL isolation-level semantics. Do not transpose PostgreSQL guarantees to SQL Server, MySQL, or other engines without their vendor documentation.

## Evidence and sources
1. PostgreSQL 18, Transaction isolation, https://www.postgresql.org/docs/18/transaction-iso.html (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.
2. Azure Architecture Center, CQRS pattern, https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.

## Maintenance
Reviewed 2026-11-07. Revisit when database/runtime semantics change, source evidence conflicts, or actual application concurrency, ownership or migration tests change assumptions. Independent source-claim audit remains necessary.
