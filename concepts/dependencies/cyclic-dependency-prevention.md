---
id: cyclic-dependency-prevention
title: "Cyclic dependency prevention"
category: dependencies
status: reviewed
reviewed_at: 2026-11-07
---

# Cyclic dependency prevention

> **Reviewed: scoped source-backed decision guidance.** The citations support ecosystem behavior or testing/quality methods, not verified improvements in an uninspected target application.

## Problem and context
Modules or projects form dependency loops.

## Applicability and constraints
Select advice using actual package manager, runtime, framework versions, deployment topology, test ownership and active analyzer/quality profile. Prototype, MVP and enterprise contexts may warrant different levels of formal enforcement; no universal tooling or numeric threshold is implied.

## Decision and trade-offs
Map directed graph and ownership, break cycles at coherent contract boundaries; prevent reintroduction with focused checks.

### Simpler/no-change option
For small projects, imports and code review may be enough.

### Risks, failure modes and counterexamples
An indiscriminate Shared project only relocates coupling; reflection can evade static checks.

## Illustrative application example
In a UI/API/worker solution, inspect the package declarations, lockfiles, import graph and CI execution before changing module boundaries, removing dependencies or claiming static-analysis compliance. A single coherent change with clear tests is preferable to extracting layers or reducing raw LOC without evidence.

## Verification, migration and rollback
Build a forbidden-edge test, run build and integration suite, migrate one edge at a time. Record observed evidence versus inference, tested consumers, a reversible change plan and the stop criteria. **Sonar status remains not run/unknown** for any target project unless actual scanner output is provided.

## Search aliases
cyclic dependency prevention; cyclic dependency prevention; maintainability; software quality; dependency hygiene

## Related concepts
- [architecture-dependency-rules](../code-organization/architecture-dependency-rules.md)
- [module-public-contracts](../code-organization/module-public-contracts.md)
- [dependency-inversion](../code-organization/dependency-inversion.md)

## Evidence and sources
1. Nx enforce module boundaries, https://nx.dev/docs/features/enforce-module-boundaries (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.
2. Microsoft Common web application architectures, https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.

## Maintenance
Reviewed 2026-11-07. Revisit on new tool/runtime versions, conflicting vendor behavior, target-specific incidents or independent claim-source audit. No real application code was changed or tested.
