---
id: transactional-invariants
title: "Transactional invariants"
category: domain-design
status: reviewed
reviewed_at: 2026-11-07
---

# Transactional invariants

> **Reviewed, scoped source-backed guidance.** Architecture examples and selection heuristics are inferences; no external application, business invariant, performance or data integrity was tested.

## Problem and context
A transfer must not debit funds without the corresponding local credit; concurrent updates must respect stock constraints.

## Applicability
Apply after identifying actual business terminology, service and data ownership, storage engine/version, workload, transaction invariants and deployment boundaries. DDD terminology here is based predominantly on Microsoft's .NET-oriented architectural materials, not a mandate for a .NET implementation or microservice deployment.

## Decision and trade-offs
Identify exactly which facts require atomicity and enforce them with domain checks plus storage transactions and constraints. Separate same-store invariants from multi-service workflows.

### Simpler/no-change option
Use local SQL constraints and one transaction before introducing aggregates or sagas. Avoid broad transaction scopes with external calls.

### Failure modes and counterexamples
Read Committed and Repeatable Read differ across engines; PostgreSQL Serializable may require full transaction retries, not retries of individual statements.

## Illustrative workflow
For an Orders capability, trace request or scheduled-job entrypoint, application coordination, business policy, owned persistence, published contracts and tests. Keep one cohesive deployable when it meets requirements; consider stronger boundaries only for observed independent semantics, transaction guarantees or ownership needs. Domain events must not be confused with guaranteed external message delivery.

## Implementation, verification and rollback
Write negative tests for concurrent updates and rollback; record isolation engine/version and expected anomalies; instrument conflicts and safely retry only idempotent work. Record project-specific observations, negative tests, release/migration compatibility, and a reversible no-change option. Separate database transaction guarantees from cross-process coordination.

## Search aliases
transactional invariants; transactional invariants; domain boundaries; transactional consistency; business ownership

## Related concepts
- [aggregates](../domain-design/aggregates.md)
- [transactions](../data/transactions.md)
- [isolation-levels](../data/isolation-levels.md)

## Application-specific concurrency proof

For monetary overspend, tenant-scoped receipts, crash recovery and multi-process PostgreSQL test interleavings, follow [PostgreSQL transactional concurrency](../data/postgresql-transactional-concurrency.md). A metadata-valid architectural example is not a production financial-integrity test.

## Evidence and sources
1. PostgreSQL 18, Transaction isolation, https://www.postgresql.org/docs/18/transaction-iso.html (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.
2. Microsoft Learn, Domain model, https://learn.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/microservice-domain-model (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.

## Maintenance
Reviewed 2026-11-07. Revisit when database/runtime semantics change, source evidence conflicts, or actual application concurrency, ownership or migration tests change assumptions. Independent source-claim audit remains necessary.
