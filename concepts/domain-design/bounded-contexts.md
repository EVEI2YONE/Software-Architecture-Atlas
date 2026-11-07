---
id: bounded-contexts
title: "DDD bounded contexts"
category: domain-design
status: reviewed
reviewed_at: 2026-11-07
---

# DDD bounded contexts

> **Reviewed, scoped source-backed guidance.** Architecture examples and selection heuristics are inferences; no external application, business invariant, performance or data integrity was tested.

## Problem and context
Business teams use the same term Customer with different definitions in billing and support.

## Applicability
Apply after identifying actual business terminology, service and data ownership, storage engine/version, workload, transaction invariants and deployment boundaries. DDD terminology here is based predominantly on Microsoft's .NET-oriented architectural materials, not a mandate for a .NET implementation or microservice deployment.

## Decision and trade-offs
A bounded context defines where a domain model and language remain internally consistent; it is not automatically a service or repository. Identify model owners, translations and cross-context expectations before deployable boundaries.

### Simpler/no-change option
Keep a cohesive internal module for a modest domain; split models only when independent semantics and change pressures are demonstrated.

### Failure modes and counterexamples
One shared canonical Customer object can leak unrelated semantics. One microservice per context is not mandatory; network boundaries add failure modes.

## Illustrative workflow
For an Orders capability, trace request or scheduled-job entrypoint, application coordination, business policy, owned persistence, published contracts and tests. Keep one cohesive deployable when it meets requirements; consider stronger boundaries only for observed independent semantics, transaction guarantees or ownership needs. Domain events must not be confused with guaranteed external message delivery.

## Implementation, verification and rollback
Map conflicting terms with stakeholders, sample changes, contract tests and integration paths; trial one internal boundary before service extraction. Record project-specific observations, negative tests, release/migration compatibility, and a reversible no-change option. Separate database transaction guarantees from cross-process coordination.

## Search aliases
ddd bounded contexts; bounded contexts; domain boundaries; transactional consistency; business ownership

## Related concepts
- [ubiquitous-language](../domain-design/ubiquitous-language.md)
- [context-mapping](../domain-design/context-mapping.md)
- [aggregates](../domain-design/aggregates.md)
- [modularity](../code-organization/modularity.md)

## Evidence and sources
1. Microsoft Learn, DDD-oriented microservice, https://learn.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/ddd-oriented-microservice (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.
2. Microsoft Learn, Domain model, https://learn.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/microservice-domain-model (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.

## Maintenance
Reviewed 2026-11-07. Revisit when database/runtime semantics change, source evidence conflicts, or actual application concurrency, ownership or migration tests change assumptions. Independent source-claim audit remains necessary.
