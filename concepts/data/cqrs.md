---
id: cqrs
title: "CQRS decision framework"
category: data
status: reviewed
reviewed_at: 2026-11-07
---

# CQRS decision framework

> **Reviewed, scoped source-backed guidance.** Architecture examples and selection heuristics are inferences; no external application, business invariant, performance or data integrity was tested.

## Problem and context
A growing application has complex writes and separately optimized read projections.

## Applicability
Apply after identifying actual business terminology, service and data ownership, storage engine/version, workload, transaction invariants and deployment boundaries. DDD terminology here is based predominantly on Microsoft's .NET-oriented architectural materials, not a mandate for a .NET implementation or microservice deployment.

## Decision and trade-offs
Separate command/write responsibilities from query/read responsibilities when measured asymmetry or domain complexity warrants it. CQRS does not require event sourcing, separate databases, brokers or microservices.

### Simpler/no-change option
For ordinary CRUD keep a shared data model and single database; if useful, separate only handlers or read DTOs within one deployment.

### Failure modes and counterexamples
Separately stored projections can lag; view rebuilds, duplicates and stale reads require explicit reconciliation and consistency design.

## Illustrative workflow
For an Orders capability, trace request or scheduled-job entrypoint, application coordination, business policy, owned persistence, published contracts and tests. Keep one cohesive deployable when it meets requirements; consider stronger boundaries only for observed independent semantics, transaction guarantees or ownership needs. Domain events must not be confused with guaranteed external message delivery.

## Implementation, verification and rollback
Benchmark real reads/writes and transaction invariants. Prototype same-store command/query separation before new data stores; test stale-read and rollback behavior. Record project-specific observations, negative tests, release/migration compatibility, and a reversible no-change option. Separate database transaction guarantees from cross-process coordination.

## Search aliases
cqrs decision framework; cqrs; domain boundaries; transactional consistency; business ownership

## Related concepts
- [transactions](../data/transactions.md)
- [data-access-boundaries](../data/data-access-boundaries.md)
- [schema-evolution](../data/schema-evolution.md)
- [domain-events](../domain-design/domain-events.md)

## Evidence and sources
1. Azure Architecture Center, CQRS pattern, https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.
2. Microsoft Learn, Application layer, https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/microservice-application-layer-implementation-web-api (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.

## Maintenance
Reviewed 2026-11-07. Revisit when database/runtime semantics change, source evidence conflicts, or actual application concurrency, ownership or migration tests change assumptions. Independent source-claim audit remains necessary.
