---
id: solid
title: "SOLID principles"
category: principles
status: reviewed
reviewed_at: 2026-11-07
---

# SOLID principles

> **Scoped source-backed decision guidance.** These references support design principles and trade-offs, not proven improvements in an uninspected target application.

## Problem and context
An evolving API has a service class combining pricing rules, persistence and HTTP formatting.

## Applicability and scope
Language-independent conceptual guidance. Specific implementation, framework, version, workload, team and deployment constraints must be recorded for each application. References focus on .NET/cloud architecture or evolutionary design where indicated; do not extrapolate their platform-specific guarantees.

## Decision and trade-offs
Separate business policy from volatile I/O where distinct reasons to change are observed; preserve substitutability and small consumer-focused contracts. Open/closed design means useful extension seams, not interfaces for every class.

**Simpler/no-change and escalation choices:** Keep the class where ownership and change history are simple; extract only the unstable persistence boundary if needed; split further only after changes demonstrate independent concerns.

## Risks and counterexamples
An interface-per-class and speculative hierarchy can hide the call path; inheritance that strengthens preconditions violates substitutability.

## Illustrative example (not target-repository evidence)
In a prototype, keep a single understandable code path and tests; for a changing feature, make one cohesive boundary at the point of demonstrable variation. For a larger system, evaluate the same decision against ownership, deployment, consistency and operational cost. Do not infer that a higher growth stage automatically needs more projects or processes.

## Implementation, validation and rollback
Review last feature changes and test call sites; run behavioral and contract tests before/after extraction; inspect navigation steps, dependency graph and consumer breakage. Record evidence and the assumptions that would reverse the decision. Preserve compatibility and make small, testable changes; revert if correctness or navigation worsens.

## Search aliases
SOLID principles; solid; design tradeoffs; architecture decision; simpler alternative

## Related concepts
- [dependency-inversion](../code-organization/dependency-inversion.md)
- [decision records](../governance/decision-records.md)

## Evidence scope and uncertainty

The references below support adjacent architectural design and DI decisions but do not constitute independent primary evidence for all five SOLID principle formulations. Treat claims about SOLID as general design heuristics; consult original principle definitions and inspect substitution/consumer contracts in the target design. Additional claim-level source review remains open.

## Evidence and sources
1. Microsoft Learn, Common web application architectures, https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07). Supports the scoped design decision discussion; not a benchmark of this catalog.
2. Microsoft Learn, Dependency injection guidelines, https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection-guidelines (accessed 2026-11-07). Provides an alternative or complementary context and trade-offs.

## Maintenance
Reviewed 2026-11-07. Revisit after changes to the project's constraints, platform guidance or new empirical evidence. Application-specific benefits, measurements and independent source-claim audits remain open.
