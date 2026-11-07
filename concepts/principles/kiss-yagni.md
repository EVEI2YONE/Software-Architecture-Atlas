---
id: kiss-yagni
title: "KISS and YAGNI"
category: principles
status: reviewed
reviewed_at: 2026-11-07
---

# KISS and YAGNI

> **Scoped source-backed decision guidance.** These references support design principles and trade-offs, not proven improvements in an uninspected target application.

## Problem and context
An MVP proposes plugins, distributed queues and multi-tenant sharding for potential future requirements.

## Applicability and scope
Language-independent conceptual guidance. Specific implementation, framework, version, workload, team and deployment constraints must be recorded for each application. References focus on .NET/cloud architecture or evolutionary design where indicated; do not extrapolate their platform-specific guarantees.

## Decision and trade-offs
Choose the smallest design supporting demonstrated constraints; build observability and automated regression tests so future adaptation remains possible.

**Simpler/no-change and escalation choices:** Prefer one deployable and an explicit interface where genuinely necessary; introduce queues or service boundaries only when durability, ownership or scaling evidence requires them.

## Risks and counterexamples
YAGNI does not justify skipping required authentication, data integrity, recoverability or contractual compatibility; the cheapest initial code may create high reversal cost.

## Illustrative example (not target-repository evidence)
In a prototype, keep a single understandable code path and tests; for a changing feature, make one cohesive boundary at the point of demonstrable variation. For a larger system, evaluate the same decision against ownership, deployment, consistency and operational cost. Do not infer that a higher growth stage automatically needs more projects or processes.

## Implementation, validation and rollback
List current vs hypothetical requirements, evaluate migration reversibility and measure actual load/change friction; revisit architecture with defined triggers. Record evidence and the assumptions that would reverse the decision. Preserve compatibility and make small, testable changes; revert if correctness or navigation worsens.

## Search aliases
KISS and YAGNI; kiss yagni; design tradeoffs; architecture decision; simpler alternative

## Related concepts
- [decision-records](../governance/decision-records.md)
- [decision records](../governance/decision-records.md)

## Evidence and sources
1. Martin Fowler, Yagni, https://martinfowler.com/bliki/Yagni.html (accessed 2026-11-07). Supports the scoped design decision discussion; not a benchmark of this catalog.
2. Microsoft Learn, Common web application architectures, https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07). Provides an alternative or complementary context and trade-offs.

## Maintenance
Reviewed 2026-11-07. Revisit after changes to the project's constraints, platform guidance or new empirical evidence. Application-specific benefits, measurements and independent source-claim audits remain open.
