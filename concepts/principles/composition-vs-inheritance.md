---
id: composition-vs-inheritance
title: "Composition versus inheritance"
category: principles
status: reviewed
reviewed_at: 2026-11-07
---

# Composition versus inheritance

> **Scoped source-backed decision guidance.** These references support design principles and trade-offs, not proven improvements in an uninspected target application.

## Problem and context
A subclass inherits a broad base API to reuse only one operation.

## Applicability and scope
Language-independent conceptual guidance. Specific implementation, framework, version, workload, team and deployment constraints must be recorded for each application. References focus on .NET/cloud architecture or evolutionary design where indicated; do not extrapolate their platform-specific guarantees.

## Decision and trade-offs
Prefer composition/delegation when capabilities vary independently or inherited contracts do not truly describe an is-a relationship; retain inheritance for stable substitutable type families.

**Simpler/no-change and escalation choices:** A direct function call may be simpler than both patterns; use a small injected collaborator when behavior must vary; retain inheritance when every subclass satisfies parent contracts.

## Risks and counterexamples
Delegation adds forwarding code and indirection; replacing inheritance can break public APIs, serialization and polymorphic consumers.

## Illustrative example (not target-repository evidence)
In a prototype, keep a single understandable code path and tests; for a changing feature, make one cohesive boundary at the point of demonstrable variation. For a larger system, evaluate the same decision against ownership, deployment, consistency and operational cost. Do not infer that a higher growth stage automatically needs more projects or processes.

## Implementation, validation and rollback
Run substitutability and contract tests for all subtypes; inspect consumers and public signature changes; migrate incrementally with adapters and rollback. Record evidence and the assumptions that would reverse the decision. Preserve compatibility and make small, testable changes; revert if correctness or navigation worsens.

## Search aliases
Composition versus inheritance; composition vs inheritance; design tradeoffs; architecture decision; simpler alternative

## Related concepts
- [dependency-inversion](../code-organization/dependency-inversion.md)
- [decision records](../governance/decision-records.md)

## Evidence and sources
1. Refactoring.Guru, Replace Inheritance with Delegation, https://refactoring.guru/replace-inheritance-with-delegation (accessed 2026-11-07). Supports the scoped design decision discussion; not a benchmark of this catalog.
2. Microsoft Learn, Dependency injection guidelines, https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection-guidelines (accessed 2026-11-07). Provides an alternative or complementary context and trade-offs.

## Maintenance
Reviewed 2026-11-07. Revisit after changes to the project's constraints, platform guidance or new empirical evidence. Application-specific benefits, measurements and independent source-claim audits remain open.
