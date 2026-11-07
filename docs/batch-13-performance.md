# B13 — Caching and performance optimization

**Date:** 2026-11-07. **Branch:** `curation/b7-b14-knowledge-gaps-20261107`. Shared draft **PR #3**. Research and catalog curation only; no target application benchmarks.

## Context collected before implementation
At B12 completion the canonical branch index had **81 concepts, 80 reviewed, 1 stub**, with `caching` the final stub. Relevant reviewed neighbors: `scalability`, `workload-admission`, `backpressure`, `observability`, `operational-costs`, `consistency` and `data-access-boundaries`. Reviewed these pages and the B7–B14 research matrix before creating new concepts; no duplicate IDs or target application evidence was found.

Primary evidence consulted on 2026-11-07:
- Azure Architecture Center [Cache-Aside](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside), [Rate Limiting](https://learn.microsoft.com/en-us/azure/architecture/patterns/rate-limiting-pattern) and [Throttling](https://learn.microsoft.com/en-us/azure/architecture/patterns/throttling/) patterns — freshness, admission and retry behavior.
- Microsoft Learn [ASP.NET Core HybridCache](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/hybrid) — framework-dependent single-flight/cache stampede mitigation (not universal to all caches).
- Grafana k6 [Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) — express test pass/fail against metrics; thresholds must be workload-specific.
- PostgreSQL [Table Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html) — in-database partitioning rules, not generic cross-service sharding.
- Azure Well-Architected [Capacity planning](https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/capacity-planning) and [Google SRE cascading failures](https://sre.google/sre-book/addressing-cascading-failures/) — capacity and failure pressure.

These docs support scoped patterns, not measured improvements in an uninspected system.

## Topic boundaries and deduplication
1. `caching` selects whether, where and what to cache; reuse `consistency` for distributed invariants.
2. `cache-invalidation-and-stampedes` covers freshness and coordinated refill under concurrent misses.
3. `load-testing-and-baselines` captures workload shape, reproducible measurements and performance hypothesis validation; reuse `observability` for generic telemetry.
4. `rate-limiting` focuses limits by rate, principal and time; reuse `workload-admission` for broader saturation and concurrency control.
5. `partitioning-and-sharding` distinguishes PostgreSQL table partitioning from ownership of distributed shards. Reuse existing `scalability` for high-level capacity planning.
6. `resource-budgets` turns performance objectives into CPU/memory/IO/queue limits, using observed bottlenecks; reuse existing operational-cost guidance.

## Example decision matrix (illustrative only)
| Candidate | No-change or simpler option | Evidence justifying it | Essential test |
| --- | --- | --- | --- |
| Read cache | Improve origin query and index | Stable read reuse, acceptable staleness and proven cache hit benefit | Miss storms, invalidation, confidentiality, origin fallback |
| Stampede control | Short TTL and small pool | Many simultaneous expensive misses for same key | Per-key concurrent miss tests and origin request counts |
| Load testing | Small representative scenario | Performance-sensitive release/change under known demand | p95/p99, errors, throughput, resource and cost baselines |
| Rate limiting | Worker concurrency cap | Clear per-principal or downstream throughput limit | Multi-instance burst, fairness, 429/503 and retry storm |
| Data partitioning | Query/index improvements | Measured hotspot or lifecycle/maintenance boundaries | Query plans, skew, migrations and cross-partition correctness |
| Resource budget | Right-size one deployable | Known workload SLO and shared capacity bottlenecks | Sustained/burst/degraded load, queue age and recovery |

## Outputs
Upgraded `caching` from stub; added `cache-invalidation-and-stampedes`, `load-testing-and-baselines`, `rate-limiting`, `partitioning-and-sharding` and `resource-budgets` as reviewed, scoped concepts. Canonical index and performance navigation updated. Expected branch inventory: **86 total / 86 reviewed / 0 stubs**.

## Verification, migration and known gaps
The catalog validator and retrieval tests check metadata and search—not load, privacy, correctness or cost of an application. Run GitHub Actions on the PR, reconcile all golden retrieval assertions, verify source counts, link integrity and statuses. No universal hit-rate, p99, rate limit, partition number or resource cap is recommended without actual measurements. Source-to-claim assessment and application-specific tests remain open.
