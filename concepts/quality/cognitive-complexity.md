---
id: cognitive-complexity
title: "Cognitive complexity and human readability"
category: quality
status: reviewed
reviewed_at: 2026-11-07
---

# Cognitive complexity and human readability

> **Reviewed: scoped source-backed decision guidance.** The citations support ecosystem behavior or testing/quality methods, not verified improvements in an uninspected target application.

## Problem and context
Nested methods are difficult to reason about; analyzer reports a complexity score.

## Applicability and constraints
Select advice using actual package manager, runtime, framework versions, deployment topology, test ownership and active analyzer/quality profile. Prototype, MVP and enterprise contexts may warrant different levels of formal enforcement; no universal tooling or numeric threshold is implied.

## Decision and trade-offs
Use complexity as a readability signal rather than a universal defect; simplify behavior-preservingly.

### Simpler/no-change option
Retain coherent code if helper extraction would hide the flow.

### Risks, failure modes and counterexamples
Reducing line count, nesting score or method length can worsen comprehension and traceability.

## Illustrative application example
In a UI/API/worker solution, inspect the package declarations, lockfiles, import graph and CI execution before changing module boundaries, removing dependencies or claiming static-analysis compliance. A single coherent change with clear tests is preferable to extracting layers or reducing raw LOC without evidence.

## Verification, migration and rollback
Capture actual rule/profile, test branches, compare comprehension and unchanged semantics. Record observed evidence versus inference, tested consumers, a reversible change plan and the stop criteria. **Sonar status remains not run/unknown** for any target project unless actual scanner output is provided.

## Search aliases
cognitive complexity and human readability; cognitive complexity; maintainability; software quality; dependency hygiene

## Related concepts
- [quality-gates](../quality/quality-gates.md)
- [code-simplification](../code-organization/code-simplification.md)
- [sonar-rules-and-quality-profiles](../quality/sonar-rules-and-quality-profiles.md)

## Evidence and sources
1. Sonar code metrics, https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/metrics-definition (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.
2. Martin Fowler Beck Design Rules, https://martinfowler.com/bliki/BeckDesignRules.html (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.

## Maintenance
Reviewed 2026-11-07. Revisit on new tool/runtime versions, conflicting vendor behavior, target-specific incidents or independent claim-source audit. No real application code was changed or tested.
