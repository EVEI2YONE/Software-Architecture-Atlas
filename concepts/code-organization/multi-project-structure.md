---
id: multi-project-structure
title: "Multi-project solution and deployable boundaries"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Multi-project solution and deployable boundaries

> **Scoped reviewed guidance.** Sources substantiate framework conventions; directory trees and decisions below are illustrative **inferences**, not measured universal improvements.

## Applicability
UI + API + Functions + WebJobs + internal library. Example drawn from .NET single-/multi-project guidance and Azure hosting documentation; not a required enterprise template.

## Framework-grounded constraints
Logical layers/modules and physical deployment boundaries are different. An internal library can support multiple deployables, but coordinating API/data versions and independent job releases can be more costly than a single deployment.

## Candidate layout (illustrative, not a runnable repository)
```text
apps/
  web-ui/
  orders-api/
  order-events-functions/
  settlement-webjob/
libs/
  contracts/   # only stable shared contracts
  order-rules/ # only where ownership is clear
tests/
  integration/
```

## Simpler alternative
A modular monolith plus one worker may satisfy the same requirements; for an MVP, retaining a single application can reduce release and dependency overhead.

## Counterexample and costs
Do not create projects solely to match a diagram or place database entities, DTOs, secret configuration and all helpers into one shared package. Separate deployables only for demonstrated boundaries.

## Evaluation, migration and rollback
Gather runtime/framework versions, source/deployment tree, entrypoints, ownership and two representative feature changes before recommending a layout. Map dependency direction, contracts and versions, team ownership, deployment graph, release coupling, secrets, integration tests, cyclic references, build times and safe rollback. Move one cohesive unit at a time; preserve behavior and contracts; compare file hops, files touched and net maintained LOC excluding generated code. Revert when navigation, correctness, runtime discovery or operational ownership worsens.

## Evidence limits
The cited docs support specific platform capabilities and constraints. They do not independently demonstrate shorter completion time, fewer bugs, fewer LOC, or improved maintainability for an uninspected application. No application code was changed or executed for this entry.

## Search aliases
multi project structure; ui + api + functions + webjobs + internal library; application folder structure; code navigation; project files; reusable modules

## Related concepts
- [Project structure selection](project-structure-selection.md)
- [Feature first folders](feature-first-folders.md)
- [Modularity](modularity.md)
- [Code simplification](code-simplification.md)

## Sources
1. Common web application architectures: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (consulted 2026-11-07).
2. Azure Functions isolated worker: https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide (consulted 2026-11-07).
3. App Service WebJobs overview: https://learn.microsoft.com/en-us/azure/app-service/overview-webjobs (consulted 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Reassess upon major framework/hosting version change or evidence from an application-specific navigation/reliability study.
