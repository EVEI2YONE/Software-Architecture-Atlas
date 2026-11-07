---
id: event-driven
title: "Event-driven integration"
category: distributed-systems
status: reviewed
reviewed_at: 2026-11-07
---

# Event-driven integration

> **Reviewed, scoped source-backed guidance.** Broker features and guarantees apply only to specified products, tiers and configurations. This page does not certify any target system's delivery, consistency or resilience.

## Problem and context
Multiple independent services need to react to a business event without the producer synchronously calling every consumer.

## Applicability
Record real service/data owners, message broker and edition, runtime and SDK, contractual consistency and security requirements, consumer deployment lifecycles, backlog and incident evidence. For a prototype or MVP, compare no change and a simpler direct or local transaction. For growing/enterprise systems, do not confuse independent modules with separate network deployables.

## Decision and trade-offs
Separate past-tense integration event facts from commands and in-process domain events. Choose publish-subscribe or streaming based on consumers, durability and replay requirements; design for schema compatibility, observable lag and independently failing handlers.

### Simpler/no-change alternative
Use a direct HTTP call or local function when one owner needs an immediate answer and synchronous workflow meets reliability and latency constraints. A broker is not mandatory for every asynchronous action.

### Failure modes and counterexamples
Hidden consumers, ordering assumptions, duplicate messages, stale read models and weak tracing can increase incident cost. Domain-event dispatch is not by itself durable cross-process delivery.

## Illustrative workflow
An Orders API commits its own business state, then downstream inventory and notification responsibilities react through explicitly versioned contracts if asynchronous integration is justified. Each separate consumer defines its duplicate-handling, ordering, error, recovery and observability policy. These are conceptual choices, not tested implementation or a guarantee of exactly-once business effects.

## Verification, migration and rollback
Map producer and consumer contracts; simulate consumer outage, delayed/replayed messages, authorization and schema changes. Validate backfill, dead-letter handling, deduplication and correlation ID tracing before cutover. Record expected versus observed results, supported versions, unacceptable loss/latency, explicit owners and fallback. Use smaller reversible increments and preserve existing consumers during compatibility windows.

## Search aliases
event-driven integration; event driven; distributed delivery; integration reliability; messaging failures; service autonomy

## Related concepts
- [domain-events](../domain-design/domain-events.md)
- [queues](../distributed-systems/queues.md)
- [schema-and-event-versioning](../distributed-systems/schema-and-event-versioning.md)
- [outbox-pattern](../distributed-systems/outbox-pattern.md)

## Evidence and sources
1. Microsoft Azure Architecture Center, Event-driven architecture style, https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven (accessed 2026-11-07). Primary vendor/platform guidance supports scoped technology behavior; real application guarantees require independent tests.
2. Microsoft Azure Architecture Center, Microservices architecture, https://learn.microsoft.com/en-us/azure/architecture/microservices/ (accessed 2026-11-07). Primary vendor/platform guidance supports scoped technology behavior; real application guarantees require independent tests.

## Maintenance
Reviewed 2026-11-07. Revisit for broker tiers/SDK versions, changed consumer contracts, delivery incidents, or source updates. An independent claim-to-source audit and application-specific validation remain open.
