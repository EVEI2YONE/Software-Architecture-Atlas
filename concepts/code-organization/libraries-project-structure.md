---
id: libraries-project-structure
title: "Reusable library and package structure"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Reusable library and package structure

> **Scoped reviewed guidance.** Sources substantiate framework conventions; directory trees and decisions below are illustrative **inferences**, not measured universal improvements.

## Applicability
Shared libraries (Python packaging and .NET NuGet examples). Python PyPA package layout and SDK-style .NET NuGet publishing; no universal src folder requirement.

## Framework-grounded constraints
PyPA distinguishes flat and src layouts; src layout requires installing the package for execution and helps catch accidental imports of repository-root code. The .NET SDK-style library can be packaged with NuGet metadata and dependencies.

## Candidate layout (illustrative, not a runnable repository)
```text
# Python distributable example
pyproject.toml
src/
  billing_rules/
    __init__.py
    calculations.py
tests/
  test_calculations.py
# .NET alternative: BillingRules/BillingRules.csproj
```

## Simpler alternative
Keep stable shared functions as internal modules until a real second consumer, API boundary or independent lifecycle justifies package publishing.

## Counterexample and costs
Do not turn cosmetic duplication into a shared package. Publishing adds semantic compatibility, versioning, dependency policy and release burden. Flat Python layouts are legitimate in suitable contexts.

## Evaluation, migration and rollback
Gather runtime/framework versions, source/deployment tree, entrypoints, ownership and two representative feature changes before recommending a layout. Test installed artifacts (not just source-tree imports), public API compatibility, wheel/package contents, consumer integration, dependency constraints and ability to revert a package extraction. Move one cohesive unit at a time; preserve behavior and contracts; compare file hops, files touched and net maintained LOC excluding generated code. Revert when navigation, correctness, runtime discovery or operational ownership worsens.

## Evidence limits
The cited docs support specific platform capabilities and constraints. They do not independently demonstrate shorter completion time, fewer bugs, fewer LOC, or improved maintainability for an uninspected application. No application code was changed or executed for this entry.

## Search aliases
libraries project structure; shared libraries (python packaging and .net nuget examples); application folder structure; code navigation; project files; reusable modules

## Related concepts
- [Project structure selection](project-structure-selection.md)
- [Feature first folders](feature-first-folders.md)
- [Modularity](modularity.md)
- [Code simplification](code-simplification.md)

## Sources
1. PyPA src versus flat layout: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/ (consulted 2026-11-07).
2. Microsoft .NET NuGet guidance: https://learn.microsoft.com/en-us/dotnet/standard/library-guidance/nuget (consulted 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Reassess upon major framework/hosting version change or evidence from an application-specific navigation/reliability study.
