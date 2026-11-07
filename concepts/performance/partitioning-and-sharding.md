---
id: partitioning-and-sharding
title: "Partitioning and sharding trade-offs"
category: performance
status: reviewed
reviewed_at: 2026-11-07
---

# Partitioning and sharding trade-offs

> **Reviewed, scoped source-backed guidance.** Do not infer measured speedups, cache safety, availability, cost reduction or target-system capacity from these design options.

## Problem and context
A database or worker workload is bottlenecked by specific data ranges or tenants.

## Applicability and scope
Collect actual UI/API/Functions/WebJobs workload mix, database engine, cache technology and version, baseline traffic, business freshness requirements, data sensitivity, per-tenant ownership, service objectives and cloud limits. A prototype, MVP or enterprise stage does not automatically justify a cache, sharding or autoscaling; first compare the no-change baseline.

## Decision and trade-offs
Distinguish in-database table partitioning from distributing data across independently operated shards. Choose keys by real access paths, skew, maintenance and transactional boundaries; document rebalancing and routing.

### Simpler/no-change alternative
Improve queries and indexes or vertically scale before splitting data when those options meet measured requirements.

### Failure modes and counterexamples
A hot tenant defeats naive hash/range partition schemes; distributed joins and cross-shard transactions complicate correctness. PostgreSQL partition pruning depends on query predicates and planner behavior.

## Illustrative application scenario
For a read-heavy catalog endpoint and background workers, identify the bottleneck using traces and profiling. Before adding a cache, admission control or new data partition, define an application-specific measurable hypothesis, a correctness boundary and rollback. Do not add a separate library or project just for a small performance helper when the feature owner can keep it coherent.

## Verification, migration and rollback
Capture query plans, data distribution, key skew and cross-partition operations; simulate hotspot, migration and rollback/rebalance with old and new app versions. Record initial values and repeated measurements, compare workloads fairly and preserve data-integrity checks. A successful catalog test is not a performance test of any application.

## Search aliases
partitioning and sharding trade-offs; partitioning and sharding; performance efficiency; scalability; capacity; latency; cost; architecture trade-offs

## Related concepts
- [scalability](../performance/scalability.md)
- [data-access-boundaries](../data/data-access-boundaries.md)
- [consistency](../distributed-systems/consistency.md)

## Evidence and sources
1. PostgreSQL documentation, Table Partitioning: https://www.postgresql.org/docs/current/ddl-partitioning.html (accessed 2026-11-07). Product/platform-specific scope; performance and safety outcomes require actual tests.
2. Azure Well-Architected Framework, Capacity planning: https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/capacity-planning (accessed 2026-11-07). Product/platform-specific scope; performance and safety outcomes require actual tests.

## Maintenance
Reviewed 2026-11-07. Revisit after platform/tool version changes, observed workloads or source contradictions. This is scoped research; target-system validation and independent claim-to-source audits remain open.
