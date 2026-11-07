---
id: aggregates
title: "Aggregates and invariants"
category: domain-design
status: reviewed
reviewed_at: 2026-11-07
---

# Aggregates and invariants

> **Reviewed, scoped source-backed guidance.** Architecture examples and selection heuristics are inferences; no external application, business invariant, performance or data integrity was tested.

## Problem and context
An order update must preserve valid line totals and state transitions despite concurrent changes.

## Applicability
Apply after identifying actual business terminology, service and data ownership, storage engine/version, workload, transaction invariants and deployment boundaries. DDD terminology here is based predominantly on Microsoft's .NET-oriented architectural materials, not a mandate for a .NET implementation or microservice deployment.

## Decision and trade-offs
Aggregate roots own invariants that must hold within a transactional consistency boundary. Select the smallest cohesive boundary supported by real business rules, not the largest object graph.

### Simpler/no-change option
Simple validated records and a database constraint may be sufficient for CRUD; use a richer aggregate only for meaningful invariants.

### Failure modes and counterexamples
Overlarge aggregates increase contention; writing children behind the aggregate root breaks assumed invariants; a transaction cannot atomically commit arbitrary remote messages.

## Illustrative workflow
For an Orders capability, trace request or scheduled-job entrypoint, application coordination, business policy, owned persistence, published contracts and tests. Keep one cohesive deployable when it meets requirements; consider stronger boundaries only for observed independent semantics, transaction guarantees or ownership needs. Domain events must not be confused with guaranteed external message delivery.

## Implementation, verification and rollback
Write invariant and concurrency tests, inspect transaction scope and version conflicts; add one aggregate boundary with rollback plan. Record project-specific observations, negative tests, release/migration compatibility, and a reversible no-change option. Separate database transaction guarantees from cross-process coordination.

## Search aliases
aggregates and invariants; aggregates; domain boundaries; transactional consistency; business ownership

## Related concepts
- [bounded-contexts](../domain-design/bounded-contexts.md)
- [transactional-invariants](../domain-design/transactional-invariants.md)
- [transactions](../data/transactions.md)

## Evidence and sources
1. Microsoft Learn, Domain model, https://learn.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/microservice-domain-model (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.
2. PostgreSQL 18, Transaction isolation, https://www.postgresql.org/docs/18/transaction-iso.html (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.

## Maintenance
Reviewed 2026-11-07. Revisit when database/runtime semantics change, source evidence conflicts, or actual application concurrency, ownership or migration tests change assumptions. Independent source-claim audit remains necessary.
