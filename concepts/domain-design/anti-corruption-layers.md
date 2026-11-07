---
id: anti-corruption-layers
title: "Anti-corruption layers"
category: domain-design
status: reviewed
reviewed_at: 2026-11-07
---

# Anti-corruption layers

> **Reviewed, scoped source-backed guidance.** Architecture examples and selection heuristics are inferences; no external application, business invariant, performance or data integrity was tested.

## Problem and context
A modern Order model must integrate a legacy ERP's incompatible status and pricing semantics.

## Applicability
Apply after identifying actual business terminology, service and data ownership, storage engine/version, workload, transaction invariants and deployment boundaries. DDD terminology here is based predominantly on Microsoft's .NET-oriented architectural materials, not a mandate for a .NET implementation or microservice deployment.

## Decision and trade-offs
Create a narrow adapter translating external semantics into local domain contracts, keeping integration differences owned at the boundary.

### Simpler/no-change option
A direct mapping function may be enough if schemas already align; add a long-lived layer only where semantic mismatch is real.

### Failure modes and counterexamples
Extra adapters add latency and ownership. Translating only field names without behavioral semantics can leak legacy assumptions; trust boundaries require validation.

## Illustrative workflow
For an Orders capability, trace request or scheduled-job entrypoint, application coordination, business policy, owned persistence, published contracts and tests. Keep one cohesive deployable when it meets requirements; consider stronger boundaries only for observed independent semantics, transaction guarantees or ownership needs. Domain events must not be confused with guaranteed external message delivery.

## Implementation, verification and rollback
Run contract tests for edge cases, failure mapping and versions; trace observability and plan adapter retirement/rollback. Record project-specific observations, negative tests, release/migration compatibility, and a reversible no-change option. Separate database transaction guarantees from cross-process coordination.

## Search aliases
anti-corruption layers; anti corruption layers; domain boundaries; transactional consistency; business ownership

## Related concepts
- [context-mapping](../domain-design/context-mapping.md)
- [bounded-contexts](../domain-design/bounded-contexts.md)
- [api-contracts](../distributed-systems/api-contracts.md)

## Evidence and sources
1. Azure Architecture Center, Anti-corruption layer, https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.
2. Microsoft Learn, DDD-oriented microservice, https://learn.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/ddd-oriented-microservice (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.

## Maintenance
Reviewed 2026-11-07. Revisit when database/runtime semantics change, source evidence conflicts, or actual application concurrency, ownership or migration tests change assumptions. Independent source-claim audit remains necessary.
