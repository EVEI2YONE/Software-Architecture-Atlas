---
id: package-by-feature-vs-layer
title: "Package by feature versus package by layer"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Package by feature versus package by layer

> **Reviewed, scoped guidance.** Sources establish platform choices or tooling behavior; decision examples and stage recommendations are inferences pending evaluation in a real application.

## Problem and context
A framework-native Controllers/Services/Repositories layout is easy to bootstrap, but one feature change repeatedly touches unrelated type-based directories.

## Applicability
Compare project kind (UI/API/Functions/WebJobs/libraries/multi-project), framework and version, prototype/MVP/growth/enterprise stage, business ownership, execution and deployment topology. Source-specific claims apply only to the named platform or tool. No runtime results or developer navigation measurements were observed for a target application.

## Decision and trade-offs
Feature-first folders optimize locating and evolving cohesive capabilities; layer-first folders can clarify framework conventions and cross-cutting responsibilities when the application is small or transformations are shared. Logical dependency direction matters more than folder labels.

### No-change and alternative approaches
Keep layer-first for a small predictable API. Introduce feature directories for high-churn capabilities while preserving a small platform layer for common infrastructure. Split into packages/projects only after consumers and dependency enforcement justify the cost.

### Failure modes, costs and counterexamples
Grouping by feature without ownership rules can replicate security, validation or transactions. Grouping solely by layer can make business workflows hard to follow. Separate build projects introduce overhead even when directories would suffice.

## Worked example (illustrative, not prescribed)
Type-first: `controllers/orders`, `services/orders`, `repositories/orders`; candidate feature-first: `features/orders/{endpoint,application,tests}` with storage adapter in `infrastructure/` as needed. Respect framework-required path rules.

## Verification, migration and rollback
Compare one bug fix and one feature addition across current and proposed layout. Record time to locate code, navigation transitions, edited-file counts, dependency cycles and build/test behavior; retain no-change if evidence is weak. Record no-change outcome, impacted files and evidence; if introducing a project/package, assess dependency versioning, builds and release overhead. Revisit on changed platform conventions, team ownership or measured navigation friction.

## Search aliases
package by feature vs layer; package by feature versus package by layer; developer navigation; module boundaries; code reuse; application code structure

## Related concepts
- [vertical-slice-architecture](vertical-slice-architecture.md)
- [feature-first-folders](feature-first-folders.md)
- [modularity](modularity.md)

## Evidence and sources
1. Microsoft Learn, Developing ASP.NET Core MVC apps: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/develop-asp-net-core-mvc-apps (accessed 2026-11-07). Supports: Direct discussion of feature folders compared with technical-type folders.
2. Microsoft Learn, Common web application architectures: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07). Supports: Single-project organization and logical layer distinctions.

## Maintenance
Reviewed 2026-11-07. Do not infer measured code reduction, Sonar compliance or production readiness from this article. Independently recheck source versions and applicability on future reviews.
