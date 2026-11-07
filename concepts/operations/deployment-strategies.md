---
id: deployment-strategies
title: "Deployment strategies and safe rollback"
category: operations
status: reviewed
reviewed_at: 2026-11-07
---

# Deployment strategies and safe rollback

> **Reviewed — limited to cited source methods.** No real workload, incident recovery, financial cost or deployment has been measured.

## Supported scope
Azure Well-Architected guidance recommends small, consistent, quality-gated changes, progressive exposure, health checks and stopping on anomalies. Canary and blue-green can reduce blast radius but create infrastructure/operational overhead. Not every workload needs these patterns.

## Compare options
- **Simple rolling update:** when backward compatibility and a short overlap are sufficient; beware mixed versions.
- **Canary/progressive release:** when representative traffic, telemetry and reliable stop conditions exist.
- **Blue-green:** when separately provisioned capacities and reversible traffic shifts justify their cost.
- **Feature flag:** when behavior can be toggled without unsafe state changes; not a database recovery mechanism.

## Required architecture checks
Document artifact version, owner/approver, rollout waves, health indicators, release dependencies, API and schema compatibility, rollback/roll-forward plan, and emergency process. Test full application startup, integration and rollback in a production-like environment. Avoid declaring success after only a green CI pipeline: real workloads and rollout health may differ.

## Counterexample and rollback
If an app is tiny and downtime acceptable, a verified simple deployment may be easier and safer than a multi-region progressive system. A database migration can be irreversible; code rollback does not necessarily restore old data. Stop rollout on observed degradation and choose rollback or safe forward-fix using real data compatibility evidence.

## Search aliases
deployment strategies; operations; service reliability; enterprise runtime; resource budgets

## Related concepts
- [observability](../operations/observability.md)
- [resilience](../operations/resilience.md)
- [schema-evolution](../data/schema-evolution.md)

## Evidence and sources
1. Azure Well-Architected Safe Deployments: https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments (accessed 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Revisit on incident, major platform/version changes or conflicting measurements.
