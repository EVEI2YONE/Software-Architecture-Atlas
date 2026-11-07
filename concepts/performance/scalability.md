---
id: scalability
title: "Scalability and capacity planning"
category: performance
status: reviewed
reviewed_at: 2026-11-07
---

# Scalability and capacity planning

> **Reviewed — scoped source-backed method, not a performance or reliability audit of any target system.**

## Supported scope
Azure Well-Architected guidance calls for negotiated performance targets, demand forecasts, capacity planning and performance tests. Google SRE cautions against relying on historical resource-to-throughput assumptions without retesting. Scaling architecture is workload-specific.

## Baseline first
Record representative request/job mix, arrival burst shape, request/queue latency distribution (including high percentiles), useful throughput, CPU/memory/IO saturation, cost per useful outcome and downstream limits. Collect production evidence when permitted; otherwise label synthetic load assumptions.

## Candidate interventions
1. Profile hot paths and query efficiency before adding nodes or caches.
2. Reduce unnecessary work, payloads and allocations where evidence identifies bottlenecks.
3. Consider admission control, bounded queues and workload isolation for saturation.
4. Compare vertical scaling, horizontal scaling, partitioning and caching based on measured bottlenecks and consistency costs.

## Counterexamples and verification
A cache may add invalidation complexity without lowering total cost, while autoscaling a CPU-bound frontend will not fix an overloaded single database. Test normal peak, bursts, degraded dependencies and recovery after overload. Compare against a no-change baseline and document why any resource budget or threshold was selected. Roll back a change that worsens tail latency, correctness or resource cost.

## Search aliases
scalability; operational diagnostics; application performance; incident investigation; runtime architecture

## Related concepts
- [backpressure](../runtime/backpressure.md)
- [caching](../performance/caching.md)

## Evidence and sources
1. Azure Well-Architected Performance Efficiency: https://learn.microsoft.com/en-us/azure/architecture/checklist/scalability (accessed 2026-11-07).
2. Google SRE Production Services Best Practices: https://sre.google/sre-book/service-best-practices/ (accessed 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Revisit on new source revisions, platform migration, observed incidents or workload changes.
