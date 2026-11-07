---
id: data-access-boundaries
title: "Data access boundaries"
category: data
status: reviewed
reviewed_at: 2026-11-07
---

# Data access boundaries

> **Reviewed, scoped source-backed guidance.** Architecture examples and selection heuristics are inferences; no external application, business invariant, performance or data integrity was tested.

## Problem and context
A user-facing feature reads a database table owned by a different business module and bypasses invariants.

## Applicability
Apply after identifying actual business terminology, service and data ownership, storage engine/version, workload, transaction invariants and deployment boundaries. DDD terminology here is based predominantly on Microsoft's .NET-oriented architectural materials, not a mandate for a .NET implementation or microservice deployment.

## Decision and trade-offs
Define data ownership, public query/command contracts, transaction scope and persistence adapters. Separate domain policies from storage technology where it protects changeable concerns; no generic repository is mandatory.

### Simpler/no-change option
A small API with stable SQL can use direct, well-scoped queries. Introduce repository/adapter contracts only where behavior and test substitution benefit.

### Failure modes and counterexamples
Leaky shared database entity types couple modules; excessive repository wrappers duplicate ORM abstractions and hide transactions.

## Illustrative workflow
For an Orders capability, trace request or scheduled-job entrypoint, application coordination, business policy, owned persistence, published contracts and tests. Keep one cohesive deployable when it meets requirements; consider stronger boundaries only for observed independent semantics, transaction guarantees or ownership needs. Domain events must not be confused with guaranteed external message delivery.

## Implementation, verification and rollback
Trace data reads/writes and consumer dependency paths; test concurrency, migration and public contract compatibility before moving access. Record project-specific observations, negative tests, release/migration compatibility, and a reversible no-change option. Separate database transaction guarantees from cross-process coordination.

## Search aliases
data access boundaries; data access boundaries; domain boundaries; transactional consistency; business ownership

## Related concepts
- [transactions](../data/transactions.md)
- [module-public-contracts](../code-organization/module-public-contracts.md)
- [schema-evolution](../data/schema-evolution.md)

## Evidence and sources
1. Microsoft Learn, Domain model, https://learn.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/microservice-domain-model (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.
2. Microsoft Learn, Application layer, https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/microservice-application-layer-implementation-web-api (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.

## Maintenance
Reviewed 2026-11-07. Revisit when database/runtime semantics change, source evidence conflicts, or actual application concurrency, ownership or migration tests change assumptions. Independent source-claim audit remains necessary.
