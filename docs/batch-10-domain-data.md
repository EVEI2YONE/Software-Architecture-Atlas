# B10 — Domain-driven design and data architecture

**Date:** 2026-11-07. **Branch:** `curation/b7-b14-knowledge-gaps-20261107`. **Shared draft PR:** #3. **Scope:** catalog curation, no target application audit.

## Context collected before implementation
The B9 branch index contained 64 concepts: 53 reviewed and 11 stubs. B10 targeted four stubs (`bounded-contexts`, `aggregates`, `domain-events`, `cqrs`) and seven unindexed dedicated concepts. Existing reviewed neighbors: `transactions`, `schema-evolution`, `module-public-contracts`, `api-contracts`, `idempotency` and `modularity`. We inspected the existing pages and the campaign context matrix before changes.

Primary source research (accessed 2026-11-07): Microsoft's [.NET DDD-oriented microservice guide](https://learn.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/ddd-oriented-microservice), [domain model](https://learn.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/microservice-domain-model) and [application layer](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/microservice-application-layer-implementation-web-api); Azure [CQRS](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs) and [anti-corruption layer](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer); and [PostgreSQL 18 transaction isolation](https://www.postgresql.org/docs/18/transaction-iso.html). These sources establish scoped methods and engine-specific guarantees, not empirical productivity or safety in an uninspected application.

## Research and deduplication decisions
- `bounded-contexts` concerns semantic model and language boundaries. Neither a bounded context nor aggregate demands a new service, repository or database.
- `ubiquitous-language` handles vocabulary; `context-mapping` defines relations between contexts; `anti-corruption-layers` addresses concrete integration translations. Reuse `module-public-contracts` for generic module APIs.
- `aggregates` defines cohesive consistency guardians; `transactional-invariants` specifies precise atomic business conditions; `isolation-levels` explains database-specific concurrency behavior. Keep generic transactions guidance in `transactions`.
- `domain-events` captures business facts; reliable external delivery remains B12 `event-driven`/queue research, not a guarantee of domain-event dispatch.
- `cqrs` is a read/write model decision, not inherently separate databases, event sourcing or an event broker. `data-access-boundaries` focuses persistence ownership and avoiding unneeded generic repositories.
- `domain-services-vs-application-services` separates domain policy from I/O orchestration; a tiny CRUD workflow can remain a direct function.

## Representative decision matrix (illustrative)
| Concern | No-change baseline | Trigger for additional structure | Test or evidence gate |
| --- | --- | --- | --- |
| Different meanings for Customer | Clear names within one module | Distinct billing/support semantics and ownership | Business interviews, model/API contract tests |
| Order state invariants | Data constraints plus simple transaction | Complex business rules or repeated invalid state | Concurrent negative tests and atomic rollback |
| Domain reaction | Direct in-process call | Multiple independently owned local reactions | Transaction timing and handler tests |
| Read scaling | One data model and store | Measured query/write asymmetry | Load tests, stale-read tolerance and projection recovery |
| Legacy ERP integration | One explicit mapper | Semantics differ; legacy model leaks broadly | Translation/contract tests, versioning and retirement |
| Isolation | Engine default with constraints | Reproduced anomalies under concurrent workload | Engine-specific schedule tests, retry conflicts and rollback |

## Delivered
Four stub upgrades: `bounded-contexts`, `aggregates`, `domain-events`, `cqrs`.

Seven new reviewed pages: `ubiquitous-language`, `context-mapping`, `domain-services-vs-application-services`, `transactional-invariants`, `anti-corruption-layers`, `data-access-boundaries`, `isolation-levels`.

Canonical index and domain-design/data category navigation updated. Expected branch index **71 total / 64 reviewed / 7 stubs**.

## Verification and limitations
Every page must retain primary URLs, scoped applicability, a simpler option, counterexamples, a verification method and rollback. Validate canonical IDs/frontmatter/source counts/links, plus retrieval tests and changed-status regression cases. Run catalog validator and tests through PR GitHub Actions and record actual result in campaign tracker.

No application-specific domains, actual transactions, data loss incidents, benchmarks or production systems were tested. Reviewed means scoped source-backed catalog guidance; independent claim-source audits and real application evaluations remain open.
