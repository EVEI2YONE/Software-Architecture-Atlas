---
id: architecture-styles
title: "Architecture styles and boundary selection"
category: governance
status: reviewed
reviewed_at: 2026-11-07
---

# Architecture styles and boundary selection

> **Scoped source-backed decision guidance.** These references support design principles and trade-offs, not proven improvements in an uninspected target application.

## Problem and context
A growing product must choose between layered, feature-first, modular-monolith and independently deployed services.

## Applicability and scope
Language-independent conceptual guidance. Specific implementation, framework, version, workload, team and deployment constraints must be recorded for each application. References focus on .NET/cloud architecture or evolutionary design where indicated; do not extrapolate their platform-specific guarantees.

## Decision and trade-offs
Compare logical layers, ports/adapters, modular monolith and distributed services by dependency direction, deployment independence, data ownership and operational complexity; architecture styles are constraints, not badges.

**Simpler/no-change and escalation choices:** Keep one deployable with clear feature boundaries unless separate release cadence, independent resource scaling or governance makes distribution worthwhile.

## Risks and counterexamples
Microservices add network failure, contract versioning, tracing and distributed consistency; layered designs can cause horizontal feature hopping; excessive ports add indirection.

## Illustrative example (not target-repository evidence)
In a prototype, keep a single understandable code path and tests; for a changing feature, make one cohesive boundary at the point of demonstrable variation. For a larger system, evaluate the same decision against ownership, deployment, consistency and operational cost. Do not infer that a higher growth stage automatically needs more projects or processes.

## Implementation, validation and rollback
Build a decision matrix using actual requirements and current system map; prototype one boundary; test end-to-end behavior, deployment/rollback and measured maintenance impact. Record evidence and the assumptions that would reverse the decision. Preserve compatibility and make small, testable changes; revert if correctness or navigation worsens.

## Search aliases
Architecture styles and boundary selection; architecture styles; design tradeoffs; architecture decision; simpler alternative

## Related concepts
- [modularity](../code-organization/modularity.md)
- [decision records](../governance/decision-records.md)

## Evidence and sources
1. Microsoft Learn, Architecture styles, https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/ (accessed 2026-11-07). Supports the scoped design decision discussion; not a benchmark of this catalog.
2. Microsoft Learn, Common web application architectures, https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07). Provides an alternative or complementary context and trade-offs.

## Maintenance
Reviewed 2026-11-07. Revisit after changes to the project's constraints, platform guidance or new empirical evidence. Application-specific benefits, measurements and independent source-claim audits remain open.
