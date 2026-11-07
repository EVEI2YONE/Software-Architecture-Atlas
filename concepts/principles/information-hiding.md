---
id: information-hiding
title: "Information hiding"
category: principles
status: reviewed
reviewed_at: 2026-11-07
---

# Information hiding

> **Scoped source-backed decision guidance.** These references support design principles and trade-offs, not proven improvements in an uninspected target application.

## Problem and context
A feature exposes its database schema and mutable internal objects to every caller.

## Applicability and scope
Language-independent conceptual guidance. Specific implementation, framework, version, workload, team and deployment constraints must be recorded for each application. References focus on .NET/cloud architecture or evolutionary design where indicated; do not extrapolate their platform-specific guarantees.

## Decision and trade-offs
Expose only the capability consumers need; keep data representation, scheduling and storage mechanics owned by the module so internal changes remain local.

**Simpler/no-change and escalation choices:** In small in-process features, a narrow function and private data may be sufficient; create published contracts only when actual consumers require them.

## Risks and counterexamples
Overly generic abstraction leaks implementation via configuration flags; excessive wrappers hide behavior and impede debugging.

## Illustrative example (not target-repository evidence)
In a prototype, keep a single understandable code path and tests; for a changing feature, make one cohesive boundary at the point of demonstrable variation. For a larger system, evaluate the same decision against ownership, deployment, consistency and operational cost. Do not infer that a higher growth stage automatically needs more projects or processes.

## Implementation, validation and rollback
Enumerate consumer-visible APIs and potential breaking changes; run contract and integration tests; verify internal representation can change without consumer edits. Record evidence and the assumptions that would reverse the decision. Preserve compatibility and make small, testable changes; revert if correctness or navigation worsens.

## Search aliases
Information hiding; information hiding; design tradeoffs; architecture decision; simpler alternative

## Related concepts
- [modularity](../code-organization/modularity.md)
- [decision records](../governance/decision-records.md)

## Evidence and sources
1. Microsoft Learn, Common web application architectures, https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07). Supports the scoped design decision discussion; not a benchmark of this catalog.
2. Microsoft Learn, Architecture styles, https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/ (accessed 2026-11-07). Provides an alternative or complementary context and trade-offs.

## Maintenance
Reviewed 2026-11-07. Revisit after changes to the project's constraints, platform guidance or new empirical evidence. Application-specific benefits, measurements and independent source-claim audits remain open.
