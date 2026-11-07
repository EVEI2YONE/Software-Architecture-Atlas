---
id: adr-lifecycle
title: "ADR lifecycle and supersession"
category: governance
status: reviewed
reviewed_at: 2026-11-07
---

# ADR lifecycle and supersession

> **Scoped research guidance, not target-repository verification.** Source-backed platform behavior, inferred trade-offs and missing project-specific evidence are distinct. A reviewed catalog page always requires source inspection.

## Problem and context
Decisions are recorded once but nobody owns re-evaluation or can tell which ADR governs a feature today.

## Applicability and decision
Maintain one canonical decision log with proposed, accepted, superseded and (where used) deprecated states, decision owner, assumptions, timestamp, links to replacements and a change trigger. This narrows the existing ADR concept to maintenance and discoverability rather than adding a second ADR format.

### Simpler/no-change option
A tiny project can use one brief numbered Markdown record per consequential choice and a simple index; avoid formal committees and automatic ADRs for trivial changes.

### Failure modes and counterexamples
Editing history erases rationale, while competing accepted records create contradictory agent advice. Automation cannot infer approval or real-world applicability from status alone.

## Illustrative example (not an inspected application)
An initial 'single API deployment' ADR is superseded only after release ownership changes; the old decision remains linked for historical search, and the new ADR states rollback conditions.

## Validation, migration and rollback
Inspect one decision's timeline, superseding link and references from affected modules; reject dangling supersession and conflicting active decisions by human review. Revisit after changed constraints. Preserve original application behavior and compare against no-change. Verify framework/runtime/build-tool version and platform conventions; use a small reversible change before broad reorganization. Never assert measured code reduction, security, developer navigation or quality-gate success without a target application's results.

## Search aliases
adr lifecycle; adr lifecycle and supersession; adr; governance; supersession; decision-history; source applicability

## Related concepts
- [decision-records](../governance/decision-records.md)
- [architecture-drivers](../governance/architecture-drivers.md)
- [knowledge-index-validation](../governance/knowledge-index-validation.md)

## Evidence and sources
1. AWS Prescriptive Guidance, ADR process: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html (accessed 2026-11-07). Scope: the named platform, documentation workflow or evaluation approach, not a benchmark of this catalog.
2. Martin Fowler, Architecture Decision Record: https://martinfowler.com/bliki/ArchitectureDecisionRecord.html (accessed 2026-11-07). Scope: the named platform, documentation workflow or evaluation approach, not a benchmark of this catalog.

## Maintenance
Reviewed 2026-11-07. Revisit on policy/tool/version changes, contradictory sources or observed application behavior. Independent detailed claim-to-source and project-specific audits remain open.
