---
id: schema-and-event-versioning
title: "Event schema and contract versioning"
category: distributed-systems
status: reviewed
reviewed_at: 2026-11-07
---

# Event schema and contract versioning

> **Reviewed, scoped source-backed guidance.** Broker features and guarantees apply only to specified products, tiers and configurations. This page does not certify any target system's delivery, consistency or resilience.

## Problem and context
An independently deployed consumer fails when an event producer changes field requirements or semantic meaning.

## Applicability
Record real service/data owners, message broker and edition, runtime and SDK, contractual consistency and security requirements, consumer deployment lifecycles, backlog and incident evidence. For a prototype or MVP, compare no change and a simpler direct or local transaction. For growing/enterprise systems, do not confuse independent modules with separate network deployables.

## Decision and trade-offs
Inventory producers/consumers and retention/replay horizon; choose explicit compatibility policy appropriate to Avro/Protobuf/JSON Schema or custom payloads. Confluent's backward and forward compatibility are directional and may not be transitive unless configured.

### Simpler/no-change alternative
For one coordinated producer/consumer, a staged compatible release and contract tests may be enough without a registry. Keep additive changes when they are compatible with the actual consumer behavior.

### Failure modes and counterexamples
Registry compatibility checks may not detect semantic meaning changes or unrecognized enum values. Backward compatibility does not guarantee old consumers can read new messages; old retained events may be replayed years later.

## Illustrative workflow
An Orders API commits its own business state, then downstream inventory and notification responsibilities react through explicitly versioned contracts if asynchronous integration is justified. Each separate consumer defines its duplicate-handling, ordering, error, recovery and observability policy. These are conceptual choices, not tested implementation or a guarantee of exactly-once business effects.

## Verification, migration and rollback
Test old/new producers with old/new consumers, retained/replayed payloads, unknown-field handling and schema registry compatibility setting. Revert or dual-publish behind bounded windows if consumers fail. Record expected versus observed results, supported versions, unacceptable loss/latency, explicit owners and fallback. Use smaller reversible increments and preserve existing consumers during compatibility windows.

## Search aliases
event schema and contract versioning; schema and event versioning; distributed delivery; integration reliability; messaging failures; service autonomy

## Related concepts
- [event-driven](../distributed-systems/event-driven.md)
- [api-contracts](../distributed-systems/api-contracts.md)
- [schema-evolution](../data/schema-evolution.md)

## Evidence and sources
1. Confluent, Schema evolution and compatibility, https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html (accessed 2026-11-07). Primary vendor/platform guidance supports scoped technology behavior; real application guarantees require independent tests.
2. Microsoft Azure Architecture Center, Event-driven architecture style, https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven (accessed 2026-11-07). Primary vendor/platform guidance supports scoped technology behavior; real application guarantees require independent tests.

## Maintenance
Reviewed 2026-11-07. Revisit for broker tiers/SDK versions, changed consumer contracts, delivery incidents, or source updates. An independent claim-to-source audit and application-specific validation remain open.
