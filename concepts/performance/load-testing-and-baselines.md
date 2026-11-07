---
id: load-testing-and-baselines
title: "Load testing and performance baselines"
category: performance
status: reviewed
reviewed_at: 2026-11-07
---

# Load testing and performance baselines

> **Reviewed, scoped source-backed guidance.** Do not infer measured speedups, cache safety, availability, cost reduction or target-system capacity from these design options.

## Problem and context
A proposed architecture upgrade claims it improves throughput without a reproducible reference workload.

## Applicability and scope
Collect actual UI/API/Functions/WebJobs workload mix, database engine, cache technology and version, baseline traffic, business freshness requirements, data sensitivity, per-tenant ownership, service objectives and cloud limits. A prototype, MVP or enterprise stage does not automatically justify a cache, sharding or autoscaling; first compare the no-change baseline.

## Decision and trade-offs
Collect baseline traffic mix, expected arrival model, data cardinality, latency percentiles, error rate, saturation and cost. Use load scenarios with explicit stop conditions and threshold assertions; compare the same code and environment constraints.

### Simpler/no-change alternative
Use profiling and a small smoke/load scenario before investing in a full distributed harness; use historical production telemetry only when privacy and representativeness permit.

### Failure modes and counterexamples
Synthetic benchmarks can hide cold starts, production contention and downstream quotas. A passing mean latency hides tail regressions; load tests can overwhelm dependencies.

## Illustrative application scenario
For a read-heavy catalog endpoint and background workers, identify the bottleneck using traces and profiling. Before adding a cache, admission control or new data partition, define an application-specific measurable hypothesis, a correctness boundary and rollback. Do not add a separate library or project just for a small performance helper when the feature owner can keep it coherent.

## Verification, migration and rollback
Record hardware, configuration, dataset, concurrency/arrival distribution, warmup, repetitions and confidence range. Run baseline then candidate then rollback; verify p95/p99, error budget and cost per useful operation. Record initial values and repeated measurements, compare workloads fairly and preserve data-integrity checks. A successful catalog test is not a performance test of any application.

## Search aliases
load testing and performance baselines; load testing and baselines; performance efficiency; scalability; capacity; latency; cost; architecture trade-offs

## Related concepts
- [scalability](../performance/scalability.md)
- [observability](../operations/observability.md)
- [resource-budgets](../performance/resource-budgets.md)

## Evidence and sources
1. Grafana k6, thresholds: https://grafana.com/docs/k6/latest/using-k6/thresholds/ (accessed 2026-11-07). Product/platform-specific scope; performance and safety outcomes require actual tests.
2. Azure Well-Architected Framework, Capacity planning: https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/capacity-planning (accessed 2026-11-07). Product/platform-specific scope; performance and safety outcomes require actual tests.

## Maintenance
Reviewed 2026-11-07. Revisit after platform/tool version changes, observed workloads or source contradictions. This is scoped research; target-system validation and independent claim-to-source audits remain open.
