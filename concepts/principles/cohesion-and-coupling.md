---
id: cohesion-and-coupling
title: "Cohesion and coupling"
category: principles
status: reviewed
reviewed_at: 2026-11-07
---

# Cohesion and coupling

> **Scoped source-backed decision guidance.** These references support design principles and trade-offs, not proven improvements in an uninspected target application.

## Problem and context
A shared utility package imports billing, catalog and HTTP concerns, making unrelated changes ripple.

## Applicability and scope
Language-independent conceptual guidance. Specific implementation, framework, version, workload, team and deployment constraints must be recorded for each application. References focus on .NET/cloud architecture or evolutionary design where indicated; do not extrapolate their platform-specific guarantees.

## Decision and trade-offs
Group code that changes for the same business reason and limit cross-module knowledge to stable interfaces; measure coupling through actual imports and change propagation.

**Simpler/no-change and escalation choices:** Keep small cohesive features together even inside one project; split packages only when ownership, reuse or build constraints warrant an enforced boundary.

## Risks and counterexamples
Excessive tiny modules create navigation overhead; a giant shared package increases cycles and upgrade risk.

## Illustrative example (not target-repository evidence)
In a prototype, keep a single understandable code path and tests; for a changing feature, make one cohesive boundary at the point of demonstrable variation. For a larger system, evaluate the same decision against ownership, deployment, consistency and operational cost. Do not infer that a higher growth stage automatically needs more projects or processes.

## Implementation, validation and rollback
Inspect dependency cycles, co-change patterns and feature navigation; make one reversible split with build and tests, compare before/after edges. Record evidence and the assumptions that would reverse the decision. Preserve compatibility and make small, testable changes; revert if correctness or navigation worsens.

## Search aliases
Cohesion and coupling; cohesion and coupling; design tradeoffs; architecture decision; simpler alternative

## Related concepts
- [modularity](../code-organization/modularity.md)
- [decision records](../governance/decision-records.md)

## Evidence and sources
1. Microsoft Learn, Common web application architectures, https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07). Supports the scoped design decision discussion; not a benchmark of this catalog.
2. Microsoft Learn, Architecture styles, https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/ (accessed 2026-11-07). Provides an alternative or complementary context and trade-offs.

## Maintenance
Reviewed 2026-11-07. Revisit after changes to the project's constraints, platform guidance or new empirical evidence. Application-specific benefits, measurements and independent source-claim audits remain open.
