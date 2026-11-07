---
id: caching
title: "Caching and invalidation"
category: performance
status: reviewed
reviewed_at: 2026-11-07
---

# Caching and invalidation

> **Reviewed, scoped source-backed guidance.** Do not infer measured speedups, cache safety, availability, cost reduction or target-system capacity from these design options.

## Problem and context
Repeated expensive reads dominate origin load; users require different freshness and confidentiality guarantees.

## Applicability and scope
Collect actual UI/API/Functions/WebJobs workload mix, database engine, cache technology and version, baseline traffic, business freshness requirements, data sensitivity, per-tenant ownership, service objectives and cloud limits. A prototype, MVP or enterprise stage does not automatically justify a cache, sharding or autoscaling; first compare the no-change baseline.

## Decision and trade-offs
Select cache-aside only when hit rate and reuse can justify complexity; define key scope, TTL, eviction, consistency and failure fallback. Cache is an optimization, not the source of truth.

### Simpler/no-change alternative
Keep direct queries and optimize indexes first if reads are not a demonstrated bottleneck or responses cannot tolerate staleness.

### Failure modes and counterexamples
An outdated price or permission result may violate business requirements. Local caches diverge across replicas; stale reads and origin overload during misses must be tested.

## Illustrative application scenario
For a read-heavy catalog endpoint and background workers, identify the bottleneck using traces and profiling. Before adding a cache, admission control or new data partition, define an application-specific measurable hypothesis, a correctness boundary and rollback. Do not add a separate library or project just for a small performance helper when the feature owner can keep it coherent.

## Verification, migration and rollback
Measure hit/miss and p95/p99 latency, backend load, correctness, cache cost and stale-read age; inject cache outage and key expiration; stage and revert when gains do not exceed risk. Record initial values and repeated measurements, compare workloads fairly and preserve data-integrity checks. A successful catalog test is not a performance test of any application.

## Search aliases
caching and invalidation; caching; performance efficiency; scalability; capacity; latency; cost; architecture trade-offs

## Related concepts
- [cache-invalidation-and-stampedes](../performance/cache-invalidation-and-stampedes.md)
- [consistency](../distributed-systems/consistency.md)
- [observability](../operations/observability.md)

## Evidence and sources
1. Azure Architecture Center, Cache-Aside pattern: https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside (accessed 2026-11-07). Product/platform-specific scope; performance and safety outcomes require actual tests.
2. Azure Well-Architected Framework, Capacity planning: https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/capacity-planning (accessed 2026-11-07). Product/platform-specific scope; performance and safety outcomes require actual tests.

## Maintenance
Reviewed 2026-11-07. Revisit after platform/tool version changes, observed workloads or source contradictions. This is scoped research; target-system validation and independent claim-to-source audits remain open.
