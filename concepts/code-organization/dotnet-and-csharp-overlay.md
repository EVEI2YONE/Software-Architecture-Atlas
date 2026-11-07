---
id: dotnet-and-csharp-overlay
title: ".NET and C# architecture overlay"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# .NET and C# architecture overlay

> **Scoped research guidance, not target-repository verification.** Source-backed platform behavior, inferred trade-offs and missing project-specific evidence are distinct. A reviewed catalog page always requires source inspection.

## Problem and context
An API, Azure Functions app, WebJobs worker and library share C# but their hosting, DI, compilation and deployment requirements differ.

## Applicability and decision
Retain framework entrypoints and .csproj boundaries; use feature-owned folders within projects and move to a class library only with a stable cross-deployable contract. Distinguish application core, adapters, integration tests and package interfaces; inspect .NET target framework and SDK behavior before choosing shared build props.

### Simpler/no-change option
For prototype/MVP retain one understandable project plus tests; a helper need not become an interface or NuGet package solely for reuse.

### Failure modes and counterexamples
DI scope mismatches, public types leaking EF entities and unnecessary .csproj layers increase coupling. A solution file is a navigation/build aggregate, not a runtime modularity guarantee.

## Illustrative example (not an inspected application)
Illustrative `src/Api/Features/Orders`, `src/Worker/Jobs`, `src/OrderCore` and `tests/OrderCore.Tests`. Keep functions in discoverable runtime paths and record DI scopes; assess independent deployment rather than automatically extracting projects.

## Validation, migration and rollback
Run dotnet build/test for exact TFMs, inspect project references and scoped DI lifetimes, verify API route and Function/worker discovery. Compare feature-file hops, build times and project references; rollback a split that increases complexity. Preserve original application behavior and compare against no-change. Verify framework/runtime/build-tool version and platform conventions; use a small reversible change before broad reorganization. Never assert measured code reduction, security, developer navigation or quality-gate success without a target application's results.

## Search aliases
dotnet and csharp overlay; .net and c# architecture overlay; dotnet; csharp; aspnet; csproj; azure-functions; source applicability

## Related concepts
- [project-structure-selection](../code-organization/project-structure-selection.md)
- [multi-project-structure](../code-organization/multi-project-structure.md)
- [functions-project-structure](../code-organization/functions-project-structure.md)
- [libraries-project-structure](../code-organization/libraries-project-structure.md)

## Evidence and sources
1. Microsoft Learn, Common web application architectures: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07). Scope: the named platform, documentation workflow or evaluation approach, not a benchmark of this catalog.
2. Microsoft Learn, .NET dependency injection: https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection (accessed 2026-11-07). Scope: the named platform, documentation workflow or evaluation approach, not a benchmark of this catalog.

## Maintenance
Reviewed 2026-11-07. Revisit on policy/tool/version changes, contradictory sources or observed application behavior. Independent detailed claim-to-source and project-specific audits remain open.
