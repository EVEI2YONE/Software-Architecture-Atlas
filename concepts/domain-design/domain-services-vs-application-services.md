---
id: domain-services-vs-application-services
title: "Domain services versus application services"
category: domain-design
status: reviewed
reviewed_at: 2026-11-07
---

# Domain services versus application services

> **Reviewed, scoped source-backed guidance.** Architecture examples and selection heuristics are inferences; no external application, business invariant, performance or data integrity was tested.

## Problem and context
An operation coordinates a payment provider and calculates discount eligibility.

## Applicability
Apply after identifying actual business terminology, service and data ownership, storage engine/version, workload, transaction invariants and deployment boundaries. DDD terminology here is based predominantly on Microsoft's .NET-oriented architectural materials, not a mandate for a .NET implementation or microservice deployment.

## Decision and trade-offs
Keep intrinsic business policy in domain entities/value objects or a domain service when it does not belong to one entity; application services orchestrate I/O, authorization, transactions and workflows.

### Simpler/no-change option
A single cohesive function may be better for trivial behavior; do not create two services solely to satisfy a naming pattern.

### Failure modes and counterexamples
Business invariants hidden in handlers are harder to reuse and test; putting database/network orchestration into pure domain services couples policy to infrastructure.

## Illustrative workflow
For an Orders capability, trace request or scheduled-job entrypoint, application coordination, business policy, owned persistence, published contracts and tests. Keep one cohesive deployable when it meets requirements; consider stronger boundaries only for observed independent semantics, transaction guarantees or ownership needs. Domain events must not be confused with guaranteed external message delivery.

## Implementation, verification and rollback
Classify each operation's responsibilities, unit-test policy without I/O and integration-test transaction/adapter behavior; migrate one path at a time. Record project-specific observations, negative tests, release/migration compatibility, and a reversible no-change option. Separate database transaction guarantees from cross-process coordination.

## Search aliases
domain services versus application services; domain services vs application services; domain boundaries; transactional consistency; business ownership

## Related concepts
- [aggregates](../domain-design/aggregates.md)
- [bounded-contexts](../domain-design/bounded-contexts.md)
- [data-access-boundaries](../data/data-access-boundaries.md)

## Evidence and sources
1. Microsoft Learn, Application layer, https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/microservice-application-layer-implementation-web-api (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.
2. Microsoft Learn, DDD-oriented microservice, https://learn.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/ddd-oriented-microservice (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.

## Maintenance
Reviewed 2026-11-07. Revisit when database/runtime semantics change, source evidence conflicts, or actual application concurrency, ownership or migration tests change assumptions. Independent source-claim audit remains necessary.
