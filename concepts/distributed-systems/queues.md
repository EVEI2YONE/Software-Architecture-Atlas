---
id: queues
title: "Queues and messaging"
category: distributed-systems
status: reviewed
reviewed_at: 2026-11-07
---

# Queues and messaging

> **Reviewed, scoped source-backed guidance.** Broker features and guarantees apply only to specified products, tiers and configurations. This page does not certify any target system's delivery, consistency or resilience.

## Problem and context
A scheduled worker consumes orders from a durable queue while retries and multiple consumers can change processing order.

## Applicability
Record real service/data owners, message broker and edition, runtime and SDK, contractual consistency and security requirements, consumer deployment lifecycles, backlog and incident evidence. For a prototype or MVP, compare no change and a simpler direct or local transaction. For growing/enterprise systems, do not confuse independent modules with separate network deployables.

## Decision and trade-offs
Specify broker/tier, message lock and acknowledgment, retry policy, TTL, dead-letter ownership, session/partition ordering and consumer concurrency. Azure Service Bus sessions can preserve per-session ordered processing; default general queues do not automatically preserve completion order across consumers.

### Simpler/no-change alternative
A bounded in-process channel is simpler for disposable work inside one process; direct calls can fit immediate-response flows. Use a durable queue only where asynchronous recovery or decoupling is justified.

### Failure modes and counterexamples
Dead-lettering is operational debt unless monitored and replayed safely. Broker duplicate-detection windows and tier limits do not make downstream side effects exactly once. Acknowledging before durable effects risks loss, after effects risks duplicates.

## Illustrative workflow
An Orders API commits its own business state, then downstream inventory and notification responsibilities react through explicitly versioned contracts if asynchronous integration is justified. Each separate consumer defines its duplicate-handling, ordering, error, recovery and observability policy. These are conceptual choices, not tested implementation or a guarantee of exactly-once business effects.

## Verification, migration and rollback
Test consumer crash after DB commit before ack, lock expiry, poison messages, duplicate IDs, sessions and dead-letter replay; measure backlog age/throughput and ensure replay is idempotent. Record expected versus observed results, supported versions, unacceptable loss/latency, explicit owners and fallback. Use smaller reversible increments and preserve existing consumers during compatibility windows.

## Search aliases
queues and messaging; queues; distributed delivery; integration reliability; messaging failures; service autonomy

## Related concepts
- [backpressure](../runtime/backpressure.md)
- [idempotency](../distributed-systems/idempotency.md)
- [delivery-guarantees](../distributed-systems/delivery-guarantees.md)
- [event-driven](../distributed-systems/event-driven.md)

## Durable worker ownership

Broker delivery, message visibility and acknowledgment do not themselves fence a stale application's database writes. See [Durable worker leases and fencing](durable-worker-leases-and-fencing.md) for a database-backed coordination alternative and its limitations.

## Evidence and sources
1. Microsoft Learn, Azure Service Bus message sessions, https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions (accessed 2026-11-07). Primary vendor/platform guidance supports scoped technology behavior; real application guarantees require independent tests.
2. Microsoft Learn, Azure Service Bus duplicate detection, https://learn.microsoft.com/en-us/azure/service-bus-messaging/duplicate-detection (accessed 2026-11-07). Primary vendor/platform guidance supports scoped technology behavior; real application guarantees require independent tests.

## Maintenance
Reviewed 2026-11-07. Revisit for broker tiers/SDK versions, changed consumer contracts, delivery incidents, or source updates. An independent claim-to-source audit and application-specific validation remain open.
