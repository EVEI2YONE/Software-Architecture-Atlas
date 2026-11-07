---
id: sonar-rules-and-quality-profiles
title: "Sonar rules and quality profiles"
category: quality
status: reviewed
reviewed_at: 2026-11-07
---

# Sonar rules and quality profiles

> **Reviewed: scoped source-backed decision guidance.** The citations support ecosystem behavior or testing/quality methods, not verified improvements in an uninspected target application.

## Problem and context
Code review claims Sonar violations without a real profile or scanner run.

## Applicability and constraints
Select advice using actual package manager, runtime, framework versions, deployment topology, test ownership and active analyzer/quality profile. Prototype, MVP and enterprise contexts may warrant different levels of formal enforcement; no universal tooling or numeric threshold is implied.

## Decision and trade-offs
Separate quality profile, quality gate, hotspot and vulnerability. Identify product edition, language profile and actual rule key.

### Simpler/no-change option
Begin with defaults and improve high-risk findings rather than suppressing scores to pass.

### Risks, failure modes and counterexamples
Rules vary by analyzer edition/language; predicted smells are not observed scan issues.

## Illustrative application example
In a UI/API/worker solution, inspect the package declarations, lockfiles, import graph and CI execution before changing module boundaries, removing dependencies or claiming static-analysis compliance. A single coherent change with clear tests is preferable to extracting layers or reducing raw LOC without evidence.

## Verification, migration and rollback
Record key, path, profile, suppression rationale, scanner run and verified before/after results. Record observed evidence versus inference, tested consumers, a reversible change plan and the stop criteria. **Sonar status remains not run/unknown** for any target project unless actual scanner output is provided.

## Search aliases
sonar rules and quality profiles; sonar rules and quality profiles; maintainability; software quality; dependency hygiene

## Related concepts
- [quality-gates](../quality/quality-gates.md)
- [cognitive-complexity](../quality/cognitive-complexity.md)

## Evidence and sources
1. Sonar quality gates, https://docs.sonarsource.com/sonarqube-server/2026.1/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.
2. Sonar security-related rules, https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-rules/security-related-rules (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.

## Maintenance
Reviewed 2026-11-07. Revisit on new tool/runtime versions, conflicting vendor behavior, target-specific incidents or independent claim-source audit. No real application code was changed or tested.
