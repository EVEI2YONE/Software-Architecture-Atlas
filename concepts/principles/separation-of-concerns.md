---
id: separation-of-concerns
title: "Separation of concerns"
category: principles
status: reviewed
reviewed_at: 2026-11-07
---

# Separation of concerns

> **Scoped source-backed decision guidance.** These references support design principles and trade-offs, not proven improvements in an uninspected target application.

## Problem and context
An endpoint performs transport validation, core pricing policy and storage operations in one long function.

## Applicability and scope
Language-independent conceptual guidance. Specific implementation, framework, version, workload, team and deployment constraints must be recorded for each application. References focus on .NET/cloud architecture or evolutionary design where indicated; do not extrapolate their platform-specific guarantees.

## Decision and trade-offs
Keep externally observable transport behavior, domain decisions and infrastructure responsibilities understandable; separate only concerns with independently changing requirements or distinct verification needs.

**Simpler/no-change and escalation choices:** For a tiny endpoint, keep cohesive helpers in one file; move business logic to a feature module when it gets reused or complex; isolate persistence only where tests or replacements require it.

## Risks and counterexamples
A rigid controller/service/repository stack for a trivial CRUD operation increases file hopping without clarifying ownership.

## Illustrative example (not target-repository evidence)
In a prototype, keep a single understandable code path and tests; for a changing feature, make one cohesive boundary at the point of demonstrable variation. For a larger system, evaluate the same decision against ownership, deployment, consistency and operational cost. Do not infer that a higher growth stage automatically needs more projects or processes.

## Implementation, validation and rollback
Trace a feature from route to rules to storage and tests; compare files touched, call hops and regression test coverage; preserve behavior on incremental moves. Record evidence and the assumptions that would reverse the decision. Preserve compatibility and make small, testable changes; revert if correctness or navigation worsens.

## Search aliases
Separation of concerns; separation of concerns; design tradeoffs; architecture decision; simpler alternative

## Related concepts
- [modularity](../code-organization/modularity.md)
- [decision records](../governance/decision-records.md)

## Evidence and sources
1. Microsoft Learn, Common web application architectures, https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07). Supports the scoped design decision discussion; not a benchmark of this catalog.
2. Martin Fowler, Beck Design Rules, https://martinfowler.com/bliki/BeckDesignRules.html (accessed 2026-11-07). Provides an alternative or complementary context and trade-offs.

## Maintenance
Reviewed 2026-11-07. Revisit after changes to the project's constraints, platform guidance or new empirical evidence. Application-specific benefits, measurements and independent source-claim audits remain open.
