---
id: module-public-contracts
title: "Module public contracts and ownership"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Module public contracts and ownership

> **Reviewed, scoped guidance.** Sources establish platform choices or tooling behavior; decision examples and stage recommendations are inferences pending evaluation in a real application.

## Problem and context
Consumers reach into another feature's internal data classes and storage tables, so routine internal refactors require coordinated changes.

## Applicability
Compare project kind (UI/API/Functions/WebJobs/libraries/multi-project), framework and version, prototype/MVP/growth/enterprise stage, business ownership, execution and deployment topology. Source-specific claims apply only to the named platform or tool. No runtime results or developer navigation measurements were observed for a target application.

## Decision and trade-offs
Document a stable, narrow entrypoint into a module: public operations, request/response semantics, error and authorization guarantees, ownership and compatibility policy. In-process modules need not become network services or published packages.

### No-change and alternative approaches
For a one-consumer prototype use a small public function and private internals; evolve to a package-level facade when consumers multiply. Split deployables only for independently justified deployment and operational needs.

### Failure modes, costs and counterexamples
Sharing mutable database entities as contracts couples storage evolution to every client. Interface-per-class, barrel exports of every internal type, and centrally owned generic contracts obscure ownership. Cross-team versions introduce migration cost.

## Worked example (illustrative, not prescribed)
`orders/public` exposes `placeOrder` and an explicit result type while `orders/internal/storage` remains private. Worker and API call the public operation, subject to their transaction and runtime constraints.

## Verification, migration and rollback
Enumerate actual consumer imports, public contracts and runtime calls. Add tests for compatible responses and unauthorized operations; enforce import rules where tooling permits. Move one consumer at a time; preserve adapters while rolling back. Record no-change outcome, impacted files and evidence; if introducing a project/package, assess dependency versioning, builds and release overhead. Revisit on changed platform conventions, team ownership or measured navigation friction.

## Search aliases
module public contracts; module public contracts and ownership; developer navigation; module boundaries; code reuse; application code structure

## Related concepts
- [modularity](modularity.md)
- [dependency-inversion](dependency-inversion.md)
- [api-contracts](../distributed-systems/api-contracts.md)
- [information-hiding](../principles/information-hiding.md)

## Evidence and sources
1. Microsoft Learn, Common web application architectures: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07). Supports: Dependency direction and application-core contracts.
2. Nx, Enforce Module Boundaries: https://nx.dev/docs/features/enforce-module-boundaries (accessed 2026-11-07). Supports: Concrete TypeScript and workspace dependency enforcement mechanisms.

## Maintenance
Reviewed 2026-11-07. Do not infer measured code reduction, Sonar compliance or production readiness from this article. Independently recheck source versions and applicability on future reviews.
