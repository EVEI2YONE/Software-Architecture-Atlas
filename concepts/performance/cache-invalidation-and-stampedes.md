---
id: cache-invalidation-and-stampedes
title: "Cache invalidation and stampede control"
category: performance
status: reviewed
reviewed_at: 2026-11-07
---

# Cache invalidation and stampede control

> **Reviewed, scoped source-backed guidance.** Do not infer measured speedups, cache safety, availability, cost reduction or target-system capacity from these design options.

## Problem and context
Popular keys expire simultaneously and many clients reconstruct the same expensive value.

## Applicability and scope
Collect actual UI/API/Functions/WebJobs workload mix, database engine, cache technology and version, baseline traffic, business freshness requirements, data sensitivity, per-tenant ownership, service objectives and cloud limits. A prototype, MVP or enterprise stage does not automatically justify a cache, sharding or autoscaling; first compare the no-change baseline.

## Decision and trade-offs
Define invalidation ownership, versioning and TTL. Where required use single-flight request coalescing, bounded fills, TTL jitter or background refresh, testing actual framework semantics.

### Simpler/no-change alternative
For small predictable data, skip cache; for modest concurrency, a short TTL plus measured per-key coalescing may suffice.

### Failure modes and counterexamples
Cache stampedes can worsen database load; a distributed lock may become a bottleneck or fail during partitions. Stale data after invalidation can cross tenant/permission boundaries.

## Illustrative application scenario
For a read-heavy catalog endpoint and background workers, identify the bottleneck using traces and profiling. Before adding a cache, admission control or new data partition, define an application-specific measurable hypothesis, a correctness boundary and rollback. Do not add a separate library or project just for a small performance helper when the feature owner can keep it coherent.

## Verification, migration and rollback
Replay synchronized misses, cache outage and concurrent writes; measure origin calls per key, stale-read window, hit rate and p99. Revert on correctness or overload regressions. Record initial values and repeated measurements, compare workloads fairly and preserve data-integrity checks. A successful catalog test is not a performance test of any application.

## Search aliases
cache invalidation and stampede control; cache invalidation and stampedes; performance efficiency; scalability; capacity; latency; cost; architecture trade-offs

## Related concepts
- [caching](../performance/caching.md)
- [backpressure](../runtime/backpressure.md)
- [consistency](../distributed-systems/consistency.md)

## Evidence and sources
1. Azure Architecture Center, Cache-Aside pattern: https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside (accessed 2026-11-07). Product/platform-specific scope; performance and safety outcomes require actual tests.
2. Microsoft Learn, HybridCache in ASP.NET Core: https://learn.microsoft.com/en-us/aspnet/core/performance/caching/hybrid (accessed 2026-11-07). Product/platform-specific scope; performance and safety outcomes require actual tests.

## Maintenance
Reviewed 2026-11-07. Revisit after platform/tool version changes, observed workloads or source contradictions. This is scoped research; target-system validation and independent claim-to-source audits remain open.
