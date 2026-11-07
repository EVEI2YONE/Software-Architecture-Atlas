---
id: context-mapping
title: "DDD context mapping"
category: domain-design
status: reviewed
reviewed_at: 2026-11-07
---

# DDD context mapping

> **Reviewed, scoped source-backed guidance.** Architecture examples and selection heuristics are inferences; no external application, business invariant, performance or data integrity was tested.

## Problem and context
Billing relies on catalog data yet has independent pricing and lifecycle semantics.

## Applicability
Apply after identifying actual business terminology, service and data ownership, storage engine/version, workload, transaction invariants and deployment boundaries. DDD terminology here is based predominantly on Microsoft's .NET-oriented architectural materials, not a mandate for a .NET implementation or microservice deployment.

## Decision and trade-offs
Map upstream/downstream context relationships and translation ownership before coupling schemas or extracting services. Record data ownership and contract compatibility.

### Simpler/no-change option
For one team and deployable, explicit module APIs and a small translation function can be sufficient.

### Failure modes and counterexamples
A shared library carrying mutable domain entities creates a hidden common model; uncontrolled copying causes divergence.

## Illustrative workflow
For an Orders capability, trace request or scheduled-job entrypoint, application coordination, business policy, owned persistence, published contracts and tests. Keep one cohesive deployable when it meets requirements; consider stronger boundaries only for observed independent semantics, transaction guarantees or ownership needs. Domain events must not be confused with guaranteed external message delivery.

## Implementation, verification and rollback
Map calls, shared tables, version changes and cross-team handoffs; test an explicit boundary with backfill/rollback where data changes. Record project-specific observations, negative tests, release/migration compatibility, and a reversible no-change option. Separate database transaction guarantees from cross-process coordination.

## Search aliases
ddd context mapping; context mapping; domain boundaries; transactional consistency; business ownership

## Related concepts
- [bounded-contexts](../domain-design/bounded-contexts.md)
- [anti-corruption-layers](../domain-design/anti-corruption-layers.md)
- [module-public-contracts](../code-organization/module-public-contracts.md)

## Evidence and sources
1. Microsoft Learn, DDD-oriented microservice, https://learn.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/ddd-oriented-microservice (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.
2. Azure Architecture Center, Anti-corruption layer, https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.

## Maintenance
Reviewed 2026-11-07. Revisit when database/runtime semantics change, source evidence conflicts, or actual application concurrency, ownership or migration tests change assumptions. Independent source-claim audit remains necessary.
