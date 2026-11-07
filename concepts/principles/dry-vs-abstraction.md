---
id: dry-vs-abstraction
title: "DRY versus premature abstraction"
category: principles
status: reviewed
reviewed_at: 2026-11-07
---

# DRY versus premature abstraction

> **Scoped source-backed decision guidance.** These references support design principles and trade-offs, not proven improvements in an uninspected target application.

## Problem and context
Two features contain similar-looking validation but are governed by different domain rules.

## Applicability and scope
Language-independent conceptual guidance. Specific implementation, framework, version, workload, team and deployment constraints must be recorded for each application. References focus on .NET/cloud architecture or evolutionary design where indicated; do not extrapolate their platform-specific guarantees.

## Decision and trade-offs
Remove duplicated knowledge when a single authoritative business rule really must remain synchronized; identical syntax alone does not prove shared ownership.

**Simpler/no-change and escalation choices:** Leave intentional repetition while the rules are still diverging; extract a shared rule within its owning module when synchronized changes are repeatedly observed.

## Risks and counterexamples
A generic validation framework introduces flags, callbacks and coupling that is costlier than two explicit short functions.

## Illustrative example (not target-repository evidence)
In a prototype, keep a single understandable code path and tests; for a changing feature, make one cohesive boundary at the point of demonstrable variation. For a larger system, evaluate the same decision against ownership, deployment, consistency and operational cost. Do not infer that a higher growth stage automatically needs more projects or processes.

## Implementation, validation and rollback
Compare change history and invariants; add tests distinguishing domain-specific cases before extracting; audit callers and undo the abstraction if changes begin to diverge. Record evidence and the assumptions that would reverse the decision. Preserve compatibility and make small, testable changes; revert if correctness or navigation worsens.

## Search aliases
DRY versus premature abstraction; dry vs abstraction; design tradeoffs; architecture decision; simpler alternative

## Related concepts
- [code-simplification](../code-organization/code-simplification.md)
- [decision records](../governance/decision-records.md)

## Evidence and sources
1. Martin Fowler, Beck Design Rules, https://martinfowler.com/bliki/BeckDesignRules.html (accessed 2026-11-07). Supports the scoped design decision discussion; not a benchmark of this catalog.
2. Martin Fowler, Is Design Dead?, https://martinfowler.com/articles/designDead.html (accessed 2026-11-07). Provides an alternative or complementary context and trade-offs.

## Maintenance
Reviewed 2026-11-07. Revisit after changes to the project's constraints, platform guidance or new empirical evidence. Application-specific benefits, measurements and independent source-claim audits remain open.
