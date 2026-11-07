---
id: vertical-slice-architecture
title: "Vertical slice architecture"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Vertical slice architecture

> **Reviewed, scoped guidance.** Sources establish platform choices or tooling behavior; decision examples and stage recommendations are inferences pending evaluation in a real application.

## Problem and context
A user-visible change to order cancellation crosses controllers, generic services, mapping modules and scattered tests.

## Applicability
Compare project kind (UI/API/Functions/WebJobs/libraries/multi-project), framework and version, prototype/MVP/growth/enterprise stage, business ownership, execution and deployment topology. Source-specific claims apply only to the named platform or tool. No runtime results or developer navigation measurements were observed for a target application.

## Decision and trade-offs
A vertical slice encapsulates a user operation or feature workflow from entrypoint through application decision and required integration seam. This is a way to assign change ownership, not a requirement for one handler, mediator or repository per operation.

### No-change and alternative approaches
Keep existing framework folders if the feature is trivially navigable. Move one cohesive feature and tests together when repeated changes bounce across unrelated directories. Retain a shared domain model or platform adapters when their stable behavior truly spans slices.

### Failure modes, costs and counterexamples
Copying persistence, authentication or invariant logic per handler can cause inconsistencies. Deeply nesting each slice in boilerplate layers and mediator abstractions may increase total indirection. Some frameworks require prescribed route/trigger paths.

## Worked example (illustrative, not prescribed)
Illustrative `features/orders/cancel/{endpoint,policy,tests}` and `features/orders/place/{endpoint,policy,tests}` with common domain rules owned once by `orders/domain/`. This is not a required tree.

## Verification, migration and rollback
Trace two actual tasks entrypoint→policy→integration→tests, count navigation hops and files edited; check duplicate invariants, references, DI wiring and route behavior. Migrate one slice, run affected tests and roll back if the change path worsens. Record no-change outcome, impacted files and evidence; if introducing a project/package, assess dependency versioning, builds and release overhead. Revisit on changed platform conventions, team ownership or measured navigation friction.

## Search aliases
vertical slice architecture; vertical slice architecture; developer navigation; module boundaries; code reuse; application code structure

## Related concepts
- [feature-first-folders](feature-first-folders.md)
- [package-by-feature-vs-layer](package-by-feature-vs-layer.md)
- [project-structure-selection](project-structure-selection.md)

## Evidence and sources
1. Microsoft Learn, Developing ASP.NET Core MVC apps: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/develop-asp-net-core-mvc-apps (accessed 2026-11-07). Supports: Feature organization/vertical-slice navigation option.
2. Microsoft Learn, Common web application architectures: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07). Supports: Application layering and separation trade-offs.

## Maintenance
Reviewed 2026-11-07. Do not infer measured code reduction, Sonar compliance or production readiness from this article. Independently recheck source versions and applicability on future reviews.
