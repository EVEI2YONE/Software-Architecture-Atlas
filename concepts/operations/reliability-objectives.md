---
id: reliability-objectives
title: "Reliability objectives, error budgets and recovery"
category: operations
status: reviewed
reviewed_at: 2026-11-07
---

# Reliability objectives, error budgets and recovery

> **Reviewed — limited to cited source methods.** No real workload, incident recovery, financial cost or deployment has been measured.

## Scope
Google SRE distinguishes SLI (measurement), SLO (objective) and SLA (external agreement), and documents error-budget decision policies. AWS recovery guidance recommends business-defined RTO/RPO, tested backups and regular recovery exercises. These are techniques, not automatic numeric thresholds.

## Decision method
- Identify a user journey or job outcome. Define numerator, denominator, measurement source, exclusions and time window.
- Negotiate the SLO with product and service owners; explicitly record the risk/cost trade-off. For example, a proposed success-rate SLO needs an evidence-backed target rather than a generic 99.9%.
- Define what action follows budget consumption: prioritize reliability work, reduce rollout risk, or reconsider whether the objective matches user needs.
- Distinguish recovery time objective (RTO) from allowable data-loss objective (RPO); validate both against business and backup/restore reality.

## Alternatives and anti-patterns
A prototype may start with one service-health signal and a manually rehearsed recovery path, but critical data still needs protection. Too many SLIs obscure user experience; CPU utilization alone is not a user SLO. A backup that has never been restored is not verified recovery.

## Verification and rollback
Test representative user errors and slow responses, alert routing, pager responsibility, recovery from loss of a zone/dependency and restore from backup. Measure actual recovery time/data loss; identify owners and rerun after major changes. Do not assert that a service meets an SLO or RPO/RTO without telemetry and restoration exercises.

## Search aliases
reliability objectives; operations; service reliability; enterprise runtime; resource budgets

## Related concepts
- [resilience](../operations/resilience.md)
- [observability](../operations/observability.md)
- [transactions](../data/transactions.md)

## Evidence and sources
1. Google SRE Service Level Objectives: https://sre.google/sre-book/service-level-objectives/ (accessed 2026-11-07).
2. Google SRE Implementing SLOs: https://sre.google/workbook/implementing-slos/ (accessed 2026-11-07).
3. AWS Well-Architected Failure Management: https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-failmgmt.html (accessed 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Revisit on incident, major platform/version changes or conflicting measurements.
