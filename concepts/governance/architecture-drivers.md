---
id: architecture-drivers
title: "Architecture drivers and quality attributes"
category: governance
status: reviewed
reviewed_at: 2026-11-07
---

# Architecture drivers and quality attributes

> **Scoped source-backed decision guidance.** These references support design principles and trade-offs, not proven improvements in an uninspected target application.

## Problem and context
A team considers splitting a service without having latency, reliability, deployment or cost targets.

## Applicability and scope
Language-independent conceptual guidance. Specific implementation, framework, version, workload, team and deployment constraints must be recorded for each application. References focus on .NET/cloud architecture or evolutionary design where indicated; do not extrapolate their platform-specific guarantees.

## Decision and trade-offs
Express key quality attributes as scenarios: source and stimulus, environment, response and measurable response target; rank conflicts with business stakeholders before choosing patterns.

**Simpler/no-change and escalation choices:** Keep the current deployment when constraints are satisfied; investigate an internal module before extraction; compare target-specific cost, correctness and reversibility.

## Risks and counterexamples
Generic quality scores or invented performance budgets can make a speculative architecture seem evidence-based.

## Illustrative example (not target-repository evidence)
In a prototype, keep a single understandable code path and tests; for a changing feature, make one cohesive boundary at the point of demonstrable variation. For a larger system, evaluate the same decision against ownership, deployment, consistency and operational cost. Do not infer that a higher growth stage automatically needs more projects or processes.

## Implementation, validation and rollback
Capture actual traffic distribution, failure and recovery targets, release frequency, team ownership and cost ceiling; document missing numbers explicitly and revisit after measurements. Record evidence and the assumptions that would reverse the decision. Preserve compatibility and make small, testable changes; revert if correctness or navigation worsens.

## Search aliases
Architecture drivers and quality attributes; architecture drivers; design tradeoffs; architecture decision; simpler alternative

## Related concepts
- [decision-records](../governance/decision-records.md)
- [decision records](../governance/decision-records.md)

## Evidence and sources
1. Microsoft Learn, Architecture styles, https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/ (accessed 2026-11-07). Supports the scoped design decision discussion; not a benchmark of this catalog.
2. Microsoft Learn, Microservices architecture style, https://learn.microsoft.com/en-us/azure/architecture/microservices/ (accessed 2026-11-07). Provides an alternative or complementary context and trade-offs.

## Maintenance
Reviewed 2026-11-07. Revisit after changes to the project's constraints, platform guidance or new empirical evidence. Application-specific benefits, measurements and independent source-claim audits remain open.
