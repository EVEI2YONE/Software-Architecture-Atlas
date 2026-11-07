---
id: webjobs-project-structure
title: "Background WebJobs and worker structure"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Background WebJobs and worker structure

> **Scoped reviewed guidance.** Sources substantiate framework conventions; directory trees and decisions below are illustrative **inferences**, not measured universal improvements.

## Applicability
Azure App Service WebJobs / background processor. Azure App Service WebJobs, not a universal queue-worker standard.

## Framework-grounded constraints
WebJobs support continuous and triggered modes, including scheduled jobs. Continuous jobs may run on multiple App Service instances, while triggered jobs use different execution/packaging conventions. Deployment is tied to App Service hosting, so operational boundaries matter.

## Candidate layout (illustrative, not a runnable repository)
```text
Jobs/
  SettlementWorker/
    SettlementWorker.csproj
    Program.cs
    SettlementJob.cs
    Services/
      ReconcilePayments.cs
    settings.job  # only if scheduled/triggered and applicable
Tests/
  SettlementJobTests.cs
```

## Simpler alternative
Retain a small background job within an existing supported app if schedule, ownership and scale do not warrant another host or project.

## Counterexample and costs
Do not blindly share a mutable singleton state across scaled-out continuous jobs or assume a scheduled WebJob has Azure Functions trigger semantics. Extra workers create operational work.

## Evaluation, migration and rollback
Gather runtime/framework versions, source/deployment tree, entrypoints, ownership and two representative feature changes before recommending a layout. Check actual deployment path/mode, Always On applicability, scheduling, concurrency, duplicate processing, graceful shutdown, telemetry, secrets and rollback of job package. Move one cohesive unit at a time; preserve behavior and contracts; compare file hops, files touched and net maintained LOC excluding generated code. Revert when navigation, correctness, runtime discovery or operational ownership worsens.

## Evidence limits
The cited docs support specific platform capabilities and constraints. They do not independently demonstrate shorter completion time, fewer bugs, fewer LOC, or improved maintainability for an uninspected application. No application code was changed or executed for this entry.

## Search aliases
webjobs project structure; azure app service webjobs / background processor; application folder structure; code navigation; project files; reusable modules

## Related concepts
- [Project structure selection](project-structure-selection.md)
- [Feature first folders](feature-first-folders.md)
- [Modularity](modularity.md)
- [Code simplification](code-simplification.md)

## Sources
1. Run background tasks with WebJobs: https://learn.microsoft.com/en-us/azure/app-service/webjobs-create (consulted 2026-11-07).
2. WebJobs SDK getting started: https://learn.microsoft.com/en-us/azure/app-service/webjobs-sdk-get-started (consulted 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Reassess upon major framework/hosting version change or evidence from an application-specific navigation/reliability study.
