---
id: delivery-guarantees
title: "Message delivery guarantees"
category: distributed-systems
status: reviewed
reviewed_at: 2026-11-07
---

# Message delivery guarantees

> **Reviewed, scoped source-backed guidance.** Broker features and guarantees apply only to specified products, tiers and configurations. This page does not certify any target system's delivery, consistency or resilience.

## Problem and context
After a sender timeout, neither sender nor consumer knows whether a message or side effect committed.

## Applicability
Record real service/data owners, message broker and edition, runtime and SDK, contractual consistency and security requirements, consumer deployment lifecycles, backlog and incident evidence. For a prototype or MVP, compare no change and a simpler direct or local transaction. For growing/enterprise systems, do not confuse independent modules with separate network deployables.

## Decision and trade-offs
Define the guarantee separately at producer→broker, broker→consumer and consumer→database/external effects. At-least-once delivery implies duplicates; at-most-once risks loss. Broker deduplication and transaction semantics have bounded scope and do not provide universal end-to-end exactly-once effects.

### Simpler/no-change alternative
Directly perform a local idempotent operation when durable messaging is unnecessary. For messages, choose stable IDs and consumer deduplication before pursuing expensive transactional coordination.

### Failure modes and counterexamples
Azure Service Bus duplicate detection uses configurable windows and depends on tier/message IDs. An exactly-once marketing phrase can refer to broker storage, not external payment effects. Redelivery after a consumer crash is normal.

## Illustrative workflow
An Orders API commits its own business state, then downstream inventory and notification responsibilities react through explicitly versioned contracts if asynchronous integration is justified. Each separate consumer defines its duplicate-handling, ordering, error, recovery and observability policy. These are conceptual choices, not tested implementation or a guarantee of exactly-once business effects.

## Verification, migration and rollback
Inject acknowledgment loss, broker failover, consumer crash between effect and ack, delayed retries and deduplication expiration. Count duplicate business effects and lost work rather than only message deliveries. Record expected versus observed results, supported versions, unacceptable loss/latency, explicit owners and fallback. Use smaller reversible increments and preserve existing consumers during compatibility windows.

## Search aliases
message delivery guarantees; delivery guarantees; distributed delivery; integration reliability; messaging failures; service autonomy

## Related concepts
- [idempotency](../distributed-systems/idempotency.md)
- [queues](../distributed-systems/queues.md)
- [outbox-pattern](../distributed-systems/outbox-pattern.md)

## Reclaimed worker boundary

A message redelivery or reclaimed job may carry a new lease generation but the same business operation. See [Durable worker leases and fencing](durable-worker-leases-and-fencing.md) for a concrete crash-after-commit and stale-generation verification plan.

## Evidence and sources
1. Microsoft Learn, Azure Service Bus duplicate detection, https://learn.microsoft.com/en-us/azure/service-bus-messaging/duplicate-detection (accessed 2026-11-07). Primary vendor/platform guidance supports scoped technology behavior; real application guarantees require independent tests.
2. AWS Prescriptive Guidance, Transactional outbox pattern, https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html (accessed 2026-11-07). Primary vendor/platform guidance supports scoped technology behavior; real application guarantees require independent tests.

## Maintenance
Reviewed 2026-11-07. Revisit for broker tiers/SDK versions, changed consumer contracts, delivery incidents, or source updates. An independent claim-to-source audit and application-specific validation remain open.
