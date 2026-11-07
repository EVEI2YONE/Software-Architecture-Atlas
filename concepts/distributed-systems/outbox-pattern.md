---
id: outbox-pattern
title: "Transactional outbox pattern"
category: distributed-systems
status: reviewed
reviewed_at: 2026-11-07
---

# Transactional outbox pattern

> **Reviewed, scoped source-backed guidance.** Broker features and guarantees apply only to specified products, tiers and configurations. This page does not certify any target system's delivery, consistency or resilience.

## Problem and context
A database commit succeeds but emitting its integration event fails, or the event emits before the database transaction rolls back.

## Applicability
Record real service/data owners, message broker and edition, runtime and SDK, contractual consistency and security requirements, consumer deployment lifecycles, backlog and incident evidence. For a prototype or MVP, compare no change and a simpler direct or local transaction. For growing/enterprise systems, do not confuse independent modules with separate network deployables.

## Decision and trade-offs
Store the business update and outgoing event record in one local database transaction, then have a separately recoverable publisher relay records with stable IDs, retry policy and observability. This solves the local dual-write gap, not an arbitrary two-service atomic commit.

### Simpler/no-change alternative
Keep the business operation in one database and make local calls where external notification is not needed. Do not introduce outbox polling or CDC before a concrete reliability requirement.

### Failure modes and counterexamples
The relay can publish the same event more than once after a crash, so consumers still require idempotency. Order may need aggregate sequence and partition guarantees; outbox retention and stuck records demand operational ownership.

## Illustrative workflow
An Orders API commits its own business state, then downstream inventory and notification responsibilities react through explicitly versioned contracts if asynchronous integration is justified. Each separate consumer defines its duplicate-handling, ordering, error, recovery and observability policy. These are conceptual choices, not tested implementation or a guarantee of exactly-once business effects.

## Verification, migration and rollback
Kill the process before commit, after commit before publish and after publish before acknowledgment; confirm no phantom events, eventual publication and deduplicated effects. Verify replays, schema versions and rollback of publisher migration. Record expected versus observed results, supported versions, unacceptable loss/latency, explicit owners and fallback. Use smaller reversible increments and preserve existing consumers during compatibility windows.

## Search aliases
transactional outbox pattern; outbox pattern; distributed delivery; integration reliability; messaging failures; service autonomy

## Related concepts
- [transactions](../data/transactions.md)
- [idempotency](../distributed-systems/idempotency.md)
- [delivery-guarantees](../distributed-systems/delivery-guarantees.md)
- [event-driven](../distributed-systems/event-driven.md)

## Evidence and sources
1. AWS Prescriptive Guidance, Transactional outbox pattern, https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html (accessed 2026-11-07). Primary vendor/platform guidance supports scoped technology behavior; real application guarantees require independent tests.
2. Microsoft Azure Architecture Center, Event-driven architecture style, https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven (accessed 2026-11-07). Primary vendor/platform guidance supports scoped technology behavior; real application guarantees require independent tests.

## Maintenance
Reviewed 2026-11-07. Revisit for broker tiers/SDK versions, changed consumer contracts, delivery incidents, or source updates. An independent claim-to-source audit and application-specific validation remain open.
