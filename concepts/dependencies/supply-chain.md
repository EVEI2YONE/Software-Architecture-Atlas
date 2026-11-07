---
id: supply-chain
title: "Software supply chain hygiene"
category: dependencies
status: reviewed
reviewed_at: 2026-11-07
---

# Software supply chain hygiene

> **Reviewed: scoped source-backed decision guidance.** The citations support ecosystem behavior or testing/quality methods, not verified improvements in an uninspected target application.

## Problem and context
Unreviewed third-party packages enter a release pipeline.

## Applicability and constraints
Select advice using actual package manager, runtime, framework versions, deployment topology, test ownership and active analyzer/quality profile. Prototype, MVP and enterprise contexts may warrant different levels of formal enforcement; no universal tooling or numeric threshold is implied.

## Decision and trade-offs
Check package provenance, license, advisories, dependency changes and privileged build actions; separate exposure from exploitability.

### Simpler/no-change option
Use existing platform capabilities and few vetted dependencies before adding elaborate tooling.

### Risks, failure modes and counterexamples
An absence of advisories is not proof of safety; vulnerability alerts demand applicability assessment.

## Illustrative application example
In a UI/API/worker solution, inspect the package declarations, lockfiles, import graph and CI execution before changing module boundaries, removing dependencies or claiming static-analysis compliance. A single coherent change with clear tests is preferable to extracting layers or reducing raw LOC without evidence.

## Verification, migration and rollback
Review dependency graph diff, license and security notices, CI privileges, build and rollback. Record observed evidence versus inference, tested consumers, a reversible change plan and the stop criteria. **Sonar status remains not run/unknown** for any target project unless actual scanner output is provided.

## Search aliases
software supply chain hygiene; supply chain; maintainability; software quality; dependency hygiene

## Related concepts
- [dependency-conflicts](../dependencies/dependency-conflicts.md)
- [package-locking-and-version-policy](../dependencies/package-locking-and-version-policy.md)
- [quality-gates](../quality/quality-gates.md)

## Evidence and sources
1. GitHub dependency review, https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.
2. GitHub reviewing dependency changes, https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-dependency-changes-in-a-pull-request (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.

## Maintenance
Reviewed 2026-11-07. Revisit on new tool/runtime versions, conflicting vendor behavior, target-specific incidents or independent claim-source audit. No real application code was changed or tested.
