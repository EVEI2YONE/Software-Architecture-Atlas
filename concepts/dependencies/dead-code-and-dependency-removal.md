---
id: dead-code-and-dependency-removal
title: "Dead code and dependency removal"
category: dependencies
status: reviewed
reviewed_at: 2026-11-07
---

# Dead code and dependency removal

> **Reviewed: scoped source-backed decision guidance.** The citations support ecosystem behavior or testing/quality methods, not verified improvements in an uninspected target application.

## Problem and context
Legacy code and packages accumulate and obscure feature navigation.

## Applicability and constraints
Select advice using actual package manager, runtime, framework versions, deployment topology, test ownership and active analyzer/quality profile. Prototype, MVP and enterprise contexts may warrant different levels of formal enforcement; no universal tooling or numeric threshold is implied.

## Decision and trade-offs
Verify all direct, dynamic, runtime, migration and public consumers before removal.

### Simpler/no-change option
Keep harmless repetition when independent features must evolve differently.

### Risks, failure modes and counterexamples
Static search misses reflection, scripts, plugins and external consumers.

## Illustrative application example
In a UI/API/worker solution, inspect the package declarations, lockfiles, import graph and CI execution before changing module boundaries, removing dependencies or claiming static-analysis compliance. A single coherent change with clear tests is preferable to extracting layers or reducing raw LOC without evidence.

## Verification, migration and rollback
Remove one leaf dependency or dead branch; clean restore, smoke-test and rollback on failure. Record observed evidence versus inference, tested consumers, a reversible change plan and the stop criteria. **Sonar status remains not run/unknown** for any target project unless actual scanner output is provided.

## Search aliases
dead code and dependency removal; dead code and dependency removal; maintainability; software quality; dependency hygiene

## Related concepts
- [code-simplification](../code-organization/code-simplification.md)
- [supply-chain](../dependencies/supply-chain.md)
- [dependency-conflicts](../dependencies/dependency-conflicts.md)

## Evidence and sources
1. GitHub dependency review, https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.
2. npm ci, https://docs.npmjs.com/cli/v11/commands/npm-ci/ (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.

## Maintenance
Reviewed 2026-11-07. Revisit on new tool/runtime versions, conflicting vendor behavior, target-specific incidents or independent claim-source audit. No real application code was changed or tested.
