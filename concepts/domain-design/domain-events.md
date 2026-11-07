---
id: domain-events
title: "Domain events"
category: domain-design
status: reviewed
reviewed_at: 2026-11-07
---

# Domain events

> **Reviewed, scoped source-backed guidance.** Architecture examples and selection heuristics are inferences; no external application, business invariant, performance or data integrity was tested.

## Problem and context
A confirmed Order should trigger internal business reactions without embedding every downstream step inside the aggregate.

## Applicability
Apply after identifying actual business terminology, service and data ownership, storage engine/version, workload, transaction invariants and deployment boundaries. DDD terminology here is based predominantly on Microsoft's .NET-oriented architectural materials, not a mandate for a .NET implementation or microservice deployment.

## Decision and trade-offs
Domain events describe past business facts inside a domain; distinguish them from integration events delivered across processes. Define publication timing and transactional consistency explicitly.

### Simpler/no-change option
A direct function call is preferable for simple tightly coupled behavior; raise an event only where decoupled local handlers clarify ownership.

### Failure modes and counterexamples
Dispatch-before-commit risks handlers acting on rolled-back data; after-commit dispatch risks lost notifications without durable coordination. Handler retries may cause duplicate effects.

## Illustrative workflow
For an Orders capability, trace request or scheduled-job entrypoint, application coordination, business policy, owned persistence, published contracts and tests. Keep one cohesive deployable when it meets requirements; consider stronger boundaries only for observed independent semantics, transaction guarantees or ownership needs. Domain events must not be confused with guaranteed external message delivery.

## Implementation, verification and rollback
Test event ordering, transaction failure, idempotency and handler retry semantics; do not imply automatic reliable external delivery. Record project-specific observations, negative tests, release/migration compatibility, and a reversible no-change option. Separate database transaction guarantees from cross-process coordination.

## Search aliases
domain events; domain events; domain boundaries; transactional consistency; business ownership

## Related concepts
- [aggregates](../domain-design/aggregates.md)
- [bounded-contexts](../domain-design/bounded-contexts.md)
- [event-driven](../distributed-systems/event-driven.md)
- [idempotency](../distributed-systems/idempotency.md)

## Evidence and sources
1. Microsoft Learn, Domain model, https://learn.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/microservice-domain-model (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.
2. Microsoft Learn, Application layer, https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/microservice-application-layer-implementation-web-api (accessed 2026-11-07). Applies to the named framework/database architecture or platform behavior; not verified on the user's applications.

## Maintenance
Reviewed 2026-11-07. Revisit when database/runtime semantics change, source evidence conflicts, or actual application concurrency, ownership or migration tests change assumptions. Independent source-claim audit remains necessary.
