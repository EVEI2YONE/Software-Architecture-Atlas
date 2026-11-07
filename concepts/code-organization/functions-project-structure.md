---
id: functions-project-structure
title: "Serverless Functions project structure"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Serverless Functions project structure

> **Scoped reviewed guidance.** Sources substantiate framework conventions; directory trees and decisions below are illustrative **inferences**, not measured universal improvements.

## Applicability
Azure Functions (.NET isolated worker example). Azure Functions 4.x with .NET isolated worker; different bindings/languages and hosting models have different conventions.

## Framework-grounded constraints
The isolated worker is a .NET console-style executable with project file, Program.cs, function code and host.json. Local settings hold local environment values and should not be committed with secrets. Trigger entrypoints and independent business behavior can be separated without a distinct project per function.

## Candidate layout (illustrative, not a runnable repository)
```text
OrderFunctions/
  OrderFunctions.csproj
  Program.cs
  host.json
  local.settings.json  # local only; exclude from source control
  Functions/
    OrderCreatedFunction.cs
  Orders/
    ProcessOrder.cs
Tests/
  ProcessOrderTests.cs
```

## Simpler alternative
One small Functions project with functions alongside related processing code is enough when shared runtime/config and deployment are suitable.

## Counterexample and costs
Do not infer that every trigger requires its own deployable. Splitting functions affects packaging, app settings, bindings, cold starts and release coordination; a function's trigger retry is not exactly-once execution.

## Evaluation, migration and rollback
Gather runtime/framework versions, source/deployment tree, entrypoints, ownership and two representative feature changes before recommending a layout. Check function discovery, trigger bindings, host configuration, environment differences, cancellation/retries, duplicate delivery, permissions, deployment artifact and tests using supported versions. Move one cohesive unit at a time; preserve behavior and contracts; compare file hops, files touched and net maintained LOC excluding generated code. Revert when navigation, correctness, runtime discovery or operational ownership worsens.

## Evidence limits
The cited docs support specific platform capabilities and constraints. They do not independently demonstrate shorter completion time, fewer bugs, fewer LOC, or improved maintainability for an uninspected application. No application code was changed or executed for this entry.

## Search aliases
functions project structure; azure functions (.net isolated worker example); application folder structure; code navigation; project files; reusable modules

## Related concepts
- [Project structure selection](project-structure-selection.md)
- [Feature first folders](feature-first-folders.md)
- [Modularity](modularity.md)
- [Code simplification](code-simplification.md)

## Sources
1. Azure Functions .NET isolated worker guide: https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide (consulted 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Reassess upon major framework/hosting version change or evidence from an application-specific navigation/reliability study.
