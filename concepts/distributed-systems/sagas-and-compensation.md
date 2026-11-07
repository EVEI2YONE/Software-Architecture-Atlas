---
id: sagas-and-compensation
title: "Sagas and compensation"
category: distributed-systems
status: reviewed
reviewed_at: 2026-11-07
---

# Sagas and compensation

> **Reviewed, scoped source-backed guidance.** Broker features and guarantees apply only to specified products, tiers and configurations. This page does not certify any target system's delivery, consistency or resilience.

## Problem and context
A multi-service order workflow must reserve stock, authorize a payment and arrange shipment, but no single local transaction spans all steps.

## Applicability
Record real service/data owners, message broker and edition, runtime and SDK, contractual consistency and security requirements, consumer deployment lifecycles, backlog and incident evidence. For a prototype or MVP, compare no change and a simpler direct or local transaction. For growing/enterprise systems, do not confuse independent modules with separate network deployables.

## Decision and trade-offs
Model explicit local steps, durable workflow state, forward recovery and compensating business actions. Choose choreography for a few understandable participants or orchestration when a coordinator improves observability and failure handling. Compensation is semantic work, not database rollback.

### Simpler/no-change alternative
Prefer one owned database transaction or a simple synchronous workflow if requirements permit it; do not add saga infrastructure for a single-service update.

### Failure modes and counterexamples
An irreversible external action may not be fully compensable, and compensation can itself fail or race with concurrent changes. A central orchestrator adds a potential bottleneck; choreography can obscure dependencies.

## Illustrative workflow
An Orders API commits its own business state, then downstream inventory and notification responsibilities react through explicitly versioned contracts if asynchronous integration is justified. Each separate consumer defines its duplicate-handling, ordering, error, recovery and observability policy. These are conceptual choices, not tested implementation or a guarantee of exactly-once business effects.

## Verification, migration and rollback
Run failure-injection at every step, repeated commands, compensation failures and manual-intervention paths. Validate audit trail, idempotency, no double refunds and safe exit/restart of the coordinator. Record expected versus observed results, supported versions, unacceptable loss/latency, explicit owners and fallback. Use smaller reversible increments and preserve existing consumers during compatibility windows.

## Search aliases
sagas and compensation; sagas and compensation; distributed delivery; integration reliability; messaging failures; service autonomy

## Related concepts
- [consistency](../distributed-systems/consistency.md)
- [transactions](../data/transactions.md)
- [idempotency](../distributed-systems/idempotency.md)
- [outbox-pattern](../distributed-systems/outbox-pattern.md)

## Evidence and sources
1. AWS Prescriptive Guidance, Saga patterns, https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-patterns.html (accessed 2026-11-07). Primary vendor/platform guidance supports scoped technology behavior; real application guarantees require independent tests.
2. Microsoft Azure Architecture Center, Compensating Transaction pattern, https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction (accessed 2026-11-07). Primary vendor/platform guidance supports scoped technology behavior; real application guarantees require independent tests.

## Maintenance
Reviewed 2026-11-07. Revisit for broker tiers/SDK versions, changed consumer contracts, delivery incidents, or source updates. An independent claim-to-source audit and application-specific validation remain open.
