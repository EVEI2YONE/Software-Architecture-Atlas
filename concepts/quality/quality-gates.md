---
id: quality-gates
title: "Sonar quality gates and static analysis"
category: quality
status: reviewed
reviewed_at: 2026-11-07
---

# Sonar quality gates and static analysis

> **Reviewed: scoped source-backed decision guidance.** The citations support ecosystem behavior or testing/quality methods, not verified improvements in an uninspected target application.

## Problem and context
Unit tests pass but scanner gate status is unknown.

## Applicability and constraints
Select advice using actual package manager, runtime, framework versions, deployment topology, test ownership and active analyzer/quality profile. Prototype, MVP and enterprise contexts may warrant different levels of formal enforcement; no universal tooling or numeric threshold is implied.

## Decision and trade-offs
Identify the actual quality profile, rule keys, gate, new-code baseline and scanner run. Hotspots are review prompts, not automatically vulnerabilities.

### Simpler/no-change option
Start with compiler, tests and an appropriate configured quality gate; no universal threshold is mandated.

### Risks, failure modes and counterexamples
A green gate is not proof of production security; exclusions may conceal risk.

## Illustrative application example
In a UI/API/worker solution, inspect the package declarations, lockfiles, import graph and CI execution before changing module boundaries, removing dependencies or claiming static-analysis compliance. A single coherent change with clear tests is preferable to extracting layers or reducing raw LOC without evidence.

## Verification, migration and rollback
Record scanner run ID, issue paths, rule keys and actual pass/fail; rerun after fixes. Record observed evidence versus inference, tested consumers, a reversible change plan and the stop criteria. **Sonar status remains not run/unknown** for any target project unless actual scanner output is provided.

## Search aliases
sonar quality gates and static analysis; quality gates; maintainability; software quality; dependency hygiene

## Related concepts
- [sonar-rules-and-quality-profiles](../quality/sonar-rules-and-quality-profiles.md)
- [cognitive-complexity](../quality/cognitive-complexity.md)
- [testing-strategy](../quality/testing-strategy.md)

## Evidence and sources
1. Sonar quality gates, https://docs.sonarsource.com/sonarqube-server/2026.1/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.
2. Sonar security-related rules, https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-rules/security-related-rules (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.

## Maintenance
Reviewed 2026-11-07. Revisit on new tool/runtime versions, conflicting vendor behavior, target-specific incidents or independent claim-source audit. No real application code was changed or tested.
