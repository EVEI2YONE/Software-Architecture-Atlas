---
id: api-project-structure
title: "API endpoint and feature structure"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# API endpoint and feature structure

> **Scoped reviewed guidance.** Sources substantiate framework conventions; directory trees and decisions below are illustrative **inferences**, not measured universal improvements.

## Applicability
HTTP API (ASP.NET Core Minimal APIs example). ASP.NET Core Minimal APIs; routing/hosting conventions differ for MVC and other API frameworks.

## Framework-grounded constraints
MapGroup can group route prefixes and shared endpoint metadata and authorization, reducing repetitive configuration. Feature grouping can remain inside a single application/deployable.

## Candidate layout (illustrative, not a runnable repository)
```text
Api/
  Program.cs
  Features/
    Orders/
      OrdersEndpoints.cs
      OrderRequest.cs
      OrderService.cs
    Customers/
      CustomersEndpoints.cs
  Infrastructure/
    DbContext.cs
Tests/
  OrdersApiTests.cs
```

## Simpler alternative
Small API: keep a few clearly named endpoints in Program.cs if they remain readable. Use route groups only for meaningful shared configuration.

## Counterexample and costs
An endpoint-per-project or controller-service-repository class trio for every trivial CRUD operation can add navigation and DI overhead; avoid confusing API folder grouping with separate service deployment.

## Evaluation, migration and rollback
Gather runtime/framework versions, source/deployment tree, entrypoints, ownership and two representative feature changes before recommending a layout. Run route enumeration, auth/validation/negative contract tests, OpenAPI generation, DI lifecycle checks and integration tests; compare task file hops and net maintained code. Move one cohesive unit at a time; preserve behavior and contracts; compare file hops, files touched and net maintained LOC excluding generated code. Revert when navigation, correctness, runtime discovery or operational ownership worsens.

## Evidence limits
The cited docs support specific platform capabilities and constraints. They do not independently demonstrate shorter completion time, fewer bugs, fewer LOC, or improved maintainability for an uninspected application. No application code was changed or executed for this entry.

## Search aliases
api project structure; http api (asp.net core minimal apis example); application folder structure; code navigation; project files; reusable modules

## Related concepts
- [Project structure selection](project-structure-selection.md)
- [Feature first folders](feature-first-folders.md)
- [Modularity](modularity.md)
- [Code simplification](code-simplification.md)

## Sources
1. ASP.NET Core Minimal APIs route groups: https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/route-handlers?view=aspnetcore-9.0 (consulted 2026-11-07).
2. Common web application architectures: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (consulted 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Reassess upon major framework/hosting version change or evidence from an application-specific navigation/reliability study.
