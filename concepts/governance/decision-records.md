---
id: decision-records
title: "Architecture decision records"
category: governance
status: reviewed
reviewed_at: 2026-11-07
---

# Architecture decision records

> **Reviewed: scoped decision-documentation method.** Writing an ADR records rationale; it does not verify correctness of the chosen architecture.

## Purpose and applicability
A short architecture decision record (ADR) preserves the context, choice, alternatives and consequences behind a significant design decision. AWS Prescriptive Guidance defines an ADR process and its states [1]; Martin Fowler describes brief records, confidence, alternatives, and superseding rather than rewriting accepted decisions [2].

Use an ADR for consequential choices: module or service boundaries, irreversible interfaces, persistence approaches and deployment strategies. Routine renames or implementation details need not receive a ceremonial ADR.

## Minimal reviewable record
- **ID/title/status/date/owner:** proposed, accepted, or superseded; link any replacement.
- **Decision question and context:** business drivers, affected services, constraints, team/workload assumptions.
- **Evidence:** observed repository facts, measurements and references; mark inferred and unknown separately.
- **Options:** no-change and viable alternatives, costs and failure modes.
- **Decision and rationale:** what was chosen, why, and which assumption makes it reasonable.
- **Consequences and risks:** migration, tests, rollback, operational ownership.
- **Revisit trigger:** which measurable event changes the decision.
- **Confidence:** why sources and measurements support the recommendation.

## Example (illustrative, not an approved real decision)
Question: should an API extract order handling into an independent service? Alternatives: keep current folders, introduce an internal orders module, or extract a deployable. Hypothetical decision: use a module first if separate releases are not needed. Revisit if independent scaling or release ownership becomes a measured bottleneck.

## Anti-patterns
- Records that only announce the selected pattern and hide alternatives.
- Editing history to make an old decision look newly justified.
- Generating an ADR for each trivial code change.
- Treating an accepted ADR as immutable truth in the face of changed requirements; supersede with new evidence.

## Validation and rollback
Review that the record's facts and assumptions match the current repository. Record unresolved disagreements. If a decision is reversed, preserve its history and link a superseding ADR, including migration/tests/rollback for the underlying system change.

## Search aliases
ADR; architectural decision; decision log; architecture tradeoff; design rationale; reversible decisions

## Related concepts
- [KISS and YAGNI](../principles/kiss-yagni.md)
- [quality gates](../quality/quality-gates.md)
- [modularity](../code-organization/modularity.md)

## Evidence and sources
1. AWS Prescriptive Guidance, *Architectural decision record process*, https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html (accessed 2026-11-07). Explains context, decision, consequences and lifecycle.
2. Martin Fowler, *Architecture Decision Record*, published 2026-03-24, https://martinfowler.com/bliki/ArchitectureDecisionRecord.html (accessed 2026-11-07). Addresses brevity, alternatives, confidence, and superseding decisions.

## Maintenance
Reviewed: 2026-11-07. Revisit if the chosen organization's governance or decision-log workflow changes.
