---
id: consistency
title: "Distributed consistency and trade-offs"
category: distributed-systems
status: reviewed
reviewed_at: 2026-11-07
---

# Distributed consistency and trade-offs

> **Reviewed, scoped source-backed guidance.** Broker features and guarantees apply only to specified products, tiers and configurations. This page does not certify any target system's delivery, consistency or resilience.

## Problem and context
An order is committed in one service while inventory and a read model still show earlier state.

## Applicability
Record real service/data owners, message broker and edition, runtime and SDK, contractual consistency and security requirements, consumer deployment lifecycles, backlog and incident evidence. For a prototype or MVP, compare no change and a simpler direct or local transaction. For growing/enterprise systems, do not confuse independent modules with separate network deployables.

## Decision and trade-offs
Identify which invariants need atomic local transactions and which independently owned consumers can tolerate bounded stale state. Define observable consistency windows, correlation IDs, reconciliation ownership and business failure behavior. Distinguish database isolation from cross-process convergence.

### Simpler/no-change alternative
Keep a single transactional data owner or one deployable if strict consistency is essential; do not split data or create events solely for hypothetical scaling.

### Failure modes and counterexamples
Eventual consistency can show partially updated data; an unbounded convergence delay is not a useful guarantee. Retrying non-idempotent effects or assuming a distributed transaction covers all APIs risks duplication and data loss.

## Illustrative workflow
An Orders API commits its own business state, then downstream inventory and notification responsibilities react through explicitly versioned contracts if asynchronous integration is justified. Each separate consumer defines its duplicate-handling, ordering, error, recovery and observability policy. These are conceptual choices, not tested implementation or a guarantee of exactly-once business effects.

## Verification, migration and rollback
Test lost acknowledgments, delayed/out-of-order events, duplicate delivery, consumer outage and partial commits; measure convergence lag and invariant violations. Preserve reconciliation logs and rollback by reinstating compatible contracts, not by pretending remote effects can be undone atomically. Record expected versus observed results, supported versions, unacceptable loss/latency, explicit owners and fallback. Use smaller reversible increments and preserve existing consumers during compatibility windows.

## Search aliases
distributed consistency and trade-offs; consistency; distributed delivery; integration reliability; messaging failures; service autonomy

## Related concepts
- [transactions](../data/transactions.md)
- [aggregates](../domain-design/aggregates.md)
- [delivery-guarantees](../distributed-systems/delivery-guarantees.md)
- [sagas-and-compensation](../distributed-systems/sagas-and-compensation.md)

## Evidence and sources
1. Microsoft Azure Architecture Center, Event-driven architecture style, https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven (accessed 2026-11-07). Primary vendor/platform guidance supports scoped technology behavior; real application guarantees require independent tests.
2. AWS Prescriptive Guidance, Saga patterns, https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-patterns.html (accessed 2026-11-07). Primary vendor/platform guidance supports scoped technology behavior; real application guarantees require independent tests.

## Maintenance
Reviewed 2026-11-07. Revisit for broker tiers/SDK versions, changed consumer contracts, delivery incidents, or source updates. An independent claim-to-source audit and application-specific validation remain open.
