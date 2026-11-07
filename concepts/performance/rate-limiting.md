---
id: rate-limiting
title: "Rate limiting and throttling"
category: performance
status: reviewed
reviewed_at: 2026-11-07
---

# Rate limiting and throttling

> **Reviewed, scoped source-backed guidance.** Do not infer measured speedups, cache safety, availability, cost reduction or target-system capacity from these design options.

## Problem and context
An API or scheduled ingestion job overloads a shared dependency or lets one principal consume all capacity.

## Applicability and scope
Collect actual UI/API/Functions/WebJobs workload mix, database engine, cache technology and version, baseline traffic, business freshness requirements, data sensitivity, per-tenant ownership, service objectives and cloud limits. A prototype, MVP or enterprise stage does not automatically justify a cache, sharding or autoscaling; first compare the no-change baseline.

## Decision and trade-offs
Limit requests at the bottleneck dimension (rate, concurrency, data volume or cost). Choose per-key scope and window/token behavior; return meaningful 429/503 and retry guidance; coordinate downstream retry budgets.

### Simpler/no-change alternative
A simple local semaphore, lower worker concurrency or backpressure may suffice where request rate is not the constraint.

### Failure modes and counterexamples
Per-node counters do not enforce a global limit across replicas. Fixed windows admit boundary bursts; unlimited retries amplify load; throttling is not a substitute for authorization.

## Illustrative application scenario
For a read-heavy catalog endpoint and background workers, identify the bottleneck using traces and profiling. Before adding a cache, admission control or new data partition, define an application-specific measurable hypothesis, a correctness boundary and rollback. Do not add a separate library or project just for a small performance helper when the feature owner can keep it coherent.

## Verification, migration and rollback
Simulate bursts, multiple tenants/replicas, slowdown and retry storms; verify fairness, p99, rejection correctness and recovery. Revisit capacities and roll back limits that harm priority traffic. Record initial values and repeated measurements, compare workloads fairly and preserve data-integrity checks. A successful catalog test is not a performance test of any application.

## Search aliases
rate limiting and throttling; rate limiting; performance efficiency; scalability; capacity; latency; cost; architecture trade-offs

## Related concepts
- [workload-admission](../runtime/workload-admission.md)
- [backpressure](../runtime/backpressure.md)
- [resource-budgets](../performance/resource-budgets.md)

## Evidence and sources
1. Azure Architecture Center, Rate Limiting pattern: https://learn.microsoft.com/en-us/azure/architecture/patterns/rate-limiting-pattern (accessed 2026-11-07). Product/platform-specific scope; performance and safety outcomes require actual tests.
2. Azure Architecture Center, Throttling pattern: https://learn.microsoft.com/en-us/azure/architecture/patterns/throttling/ (accessed 2026-11-07). Product/platform-specific scope; performance and safety outcomes require actual tests.

## Maintenance
Reviewed 2026-11-07. Revisit after platform/tool version changes, observed workloads or source contradictions. This is scoped research; target-system validation and independent claim-to-source audits remain open.
