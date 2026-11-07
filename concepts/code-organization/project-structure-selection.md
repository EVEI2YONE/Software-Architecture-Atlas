---
id: project-structure-selection
title: "Application file and project structure selection"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Application file and project structure selection

> **Reviewed, scoped guidance.** Sources establish platform choices or tooling behavior; decision examples and stage recommendations are inferences pending evaluation in a real application.

## Problem and context
A product includes a web UI, API, scheduled jobs and a library. A team wants fewer maintained files and easier feature discovery, but the current deployment constraints are not known.

## Applicability
Compare project kind (UI/API/Functions/WebJobs/libraries/multi-project), framework and version, prototype/MVP/growth/enterprise stage, business ownership, execution and deployment topology. Source-specific claims apply only to the named platform or tool. No runtime results or developer navigation measurements were observed for a target application.

## Decision and trade-offs
Choose boundaries separately for repository, deployable, module and directory. First preserve framework-required entrypoints and build conventions. Where a feature's route, policy, persistence and tests change together, evaluate co-location; where independent contracts or releases are genuinely needed, evaluate modules or packages.

### No-change and alternative approaches
A prototype may keep one project and native framework folders; an MVP may group feature-owned files within it; a growing system may add explicit modules and only proven shared libraries; an enterprise may need ownership and version controls yet still remain a modular monolith. These are hypotheses, not stage-based requirements.

### Failure modes, costs and counterexamples
A central Shared project carrying all data models and dependencies increases coupling; aggressive fragmentation multiplies DI registrations, versioning and debugging hops. Moving a serverless entrypoint can break function discovery; moving framework routes can break routing.

## Worked example (illustrative, not prescribed)
Illustrative: `apps/web/`, `apps/api/`, `workers/settlement/`, `modules/orders/`, `tests/`. An equally reasonable small solution is `app/features/orders/` plus its tests within one deployable. Choose after inspecting the actual framework, release graph and representative changes.

## Verification, migration and rollback
Record framework/version, build graph, deployable and data boundaries, team ownership, two realistic feature-change tasks, file hops/time, files touched, dependency cycles and build/test costs. Prototype moving one feature. Run routing/trigger discovery, build, contract and integration tests, compare no-change baseline, and revert if navigation or compatibility worsens. Record no-change outcome, impacted files and evidence; if introducing a project/package, assess dependency versioning, builds and release overhead. Revisit on changed platform conventions, team ownership or measured navigation friction.

## Search aliases
project structure selection; application file and project structure selection; developer navigation; module boundaries; code reuse; application code structure

## Related concepts
- [feature-first-folders](feature-first-folders.md)
- [modularity](modularity.md)
- [multi-project-structure](multi-project-structure.md)
- [architecture-evolution](architecture-evolution.md)
- [package-by-feature-vs-layer](package-by-feature-vs-layer.md)
- [monorepo-vs-multirepo](monorepo-vs-multirepo.md)

## Evidence and sources
1. Microsoft Learn, Common web application architectures: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07). Supports: Single-project and multi-project trade-offs in .NET web apps.
2. Microsoft Learn, Developing ASP.NET Core MVC apps: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/develop-asp-net-core-mvc-apps (accessed 2026-11-07). Supports: Feature folders and navigation costs in larger MVC projects.
3. Microsoft Learn, Azure Functions .NET isolated worker guide: https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide (accessed 2026-11-07). Supports: Function runtime entrypoints and constraints.

## Maintenance
Reviewed 2026-11-07. Do not infer measured code reduction, Sonar compliance or production readiness from this article. Independently recheck source versions and applicability on future reviews.
