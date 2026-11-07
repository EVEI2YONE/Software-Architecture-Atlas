---
id: architecture-evolution
title: "Architecture evolution by product maturity"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Architecture evolution by product maturity

> **Reviewed, scoped sources and clearly marked inferred decision heuristics.** No real application or migration was evaluated.

## Problem and applicability
A product's stage (prototype, MVP, growth, enterprise) **does not determine its architecture**. Team ownership, product constraints, deployment independence, cost and change friction determine when a structure should evolve. Microsoft describes a single-project application and reasons to move to multi-project structures; AWS describes both domain-oriented decomposition and the additional complexity of service boundaries.

## Maturity stages: candidate experiments, not mandatory transformations

| Stage | Default candidate to compare | Evidence that might justify change | Avoid |
| --- | --- | --- | --- |
| Prototype | One clear deployable with direct, readable feature modules and essential tests | Framework requirements or genuine independent execution | Boilerplate layers, plugin systems for hypothetical requirements |
| MVP | Preserve proven working structure; add stable feature ownership and repeatable tests | Repeated cross-feature edits, deployment issues, real consumer compatibility needs | Automatic multiplication of services and packages |
| Growing business | Internal capability modules or selective libraries inside one deployment | Measured dependency cycles, coordination costs, different jobs or release cadences | Sharing similarly shaped but semantically distinct business logic |
| Enterprise | Explicit contracts, ownership, change controls and documented boundaries; **may still be a modular monolith** | Independent scaling/releases, compliance separation, team autonomy and operational resources | Assuming enterprise == microservices or a repository per team |

This matrix is **inferred** from source-backed architectural alternatives; none of the source documents establishes a universal maturity-to-folder mapping.

## Architecture decision gates
Before splitting, require a concrete driver, measured baseline (task time, file hops, touched-file counts, build/release frequency, change failure rate, deployment coupling), alternative no-change option, and ability to operate the resulting pieces. Independently deployable units require interface/version ownership, monitoring, recovery, authorization and data consistency work.

## Consolidation is also evolution
When fragmented libraries or services cause coordinated deployments, unnecessary network calls or duplicated policies, evaluate merging them into a cohesive internal module or one deployable. Do not assume one-way progression toward more projects.

## Example transition (illustrative)
A growing shop's Orders and Billing code share a deployable. Team changes repeatedly cross both packages. First move toward clear internal modules with no new network calls; measure change footprint and cycle count. Only consider a separate billing deployable after demonstrating independent release/ownership needs and a contract/data/rollback plan.

## Verification and rollback
Compare two representative change tasks before/after; test build, public APIs, data migration compatibility, job execution, security and release processes. Incrementally move one module and retain the previous path during the rollback window where warranted. Document reversible alternatives and evidence in an ADR.

## Limits
These sources describe architectural choices and migration strategies, not verified developer productivity improvements in an uninspected product. Platform-specific routing and packaging remain governed by [project archetypes](multi-project-structure.md).

## Search aliases
architecture evolution; prototype MVP growth enterprise; project splitting; consolidation; modular monolith; business scaling

## Related concepts
- [project-structure-selection](../code-organization/project-structure-selection.md)
- [modularity](../code-organization/modularity.md)
- [multi-project-structure](../code-organization/multi-project-structure.md)
- [decision-records](../governance/decision-records.md)

## Sources
1. Microsoft Common web application architectures: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (consulted 2026-11-07).
2. AWS Decompose by subdomain: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/decompose-subdomain.html (consulted 2026-11-07).
3. AWS Strangler fig pattern: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/strangler-fig.html (consulted 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Revisit after relevant platform or migration-guidance changes or contradictory measured results.
