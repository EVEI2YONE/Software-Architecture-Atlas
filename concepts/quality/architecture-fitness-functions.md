---
id: architecture-fitness-functions
title: "Architecture fitness functions"
category: quality
status: reviewed
reviewed_at: 2026-11-07
---

# Architecture fitness functions

> **Reviewed: scoped source-backed decision guidance.** The citations support ecosystem behavior or testing/quality methods, not verified improvements in an uninspected target application.

## Problem and context
Module-boundary violations survive conventional business tests.

## Applicability and constraints
Select advice using actual package manager, runtime, framework versions, deployment topology, test ownership and active analyzer/quality profile. Prototype, MVP and enterprise contexts may warrant different levels of formal enforcement; no universal tooling or numeric threshold is implied.

## Decision and trade-offs
Express important architecture constraints as executable dependency or compatibility tests tied to concrete failure risk.

### Simpler/no-change option
Code review and compiler project references may suffice in a small codebase.

### Risks, failure modes and counterexamples
Overly strict rules reject valid test or generated dependencies; runtime dynamic imports may escape checks.

## Illustrative application example
In a UI/API/worker solution, inspect the package declarations, lockfiles, import graph and CI execution before changing module boundaries, removing dependencies or claiming static-analysis compliance. A single coherent change with clear tests is preferable to extracting layers or reducing raw LOC without evidence.

## Verification, migration and rollback
Add a deliberately violating fixture and assert CI rejects it, document exceptions and rollback. Record observed evidence versus inference, tested consumers, a reversible change plan and the stop criteria. **Sonar status remains not run/unknown** for any target project unless actual scanner output is provided.

## Search aliases
architecture fitness functions; architecture fitness functions; maintainability; software quality; dependency hygiene

## Related concepts
- [architecture-dependency-rules](../code-organization/architecture-dependency-rules.md)
- [testing-strategy](../quality/testing-strategy.md)
- [module-public-contracts](../code-organization/module-public-contracts.md)

## Evidence and sources
1. Nx enforce module boundaries, https://nx.dev/docs/features/enforce-module-boundaries (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.
2. Microsoft Common web application architectures, https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.

## Maintenance
Reviewed 2026-11-07. Revisit on new tool/runtime versions, conflicting vendor behavior, target-specific incidents or independent claim-source audit. No real application code was changed or tested.
