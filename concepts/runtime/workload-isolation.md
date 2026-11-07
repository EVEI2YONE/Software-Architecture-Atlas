---
id: workload-isolation
title: "Workload isolation and concurrency budgets"
category: runtime
status: reviewed
reviewed_at: 2026-11-07
---

# Workload isolation and concurrency budgets

> **Reviewed: platform-scoped decision guidance, not a measured target-system result.** Claims about .NET, Python, Java or Node features apply to the stated runtime; do not transfer API guarantees across languages.

## Problem and context
Long-running report generation consumes the same resources needed for latency-sensitive API requests.

## Applicability and preconditions
Gather runtime/language versions, API/Functions/WebJobs/worker execution model, workload distribution, shared resource ownership, cancellation/shutdown contract and actual latency/error evidence. A prototype may need only direct awaited I/O; independent worker deployments or advanced concurrency tools require measured need and ownership.

## Decision and trade-offs
Set explicit concurrency and resource budgets per workload class, with bounded admission and fair scheduling where supported. Isolation can be in-process pools, queues, process boundaries or separate deployments only if justified by resource contention and ownership.

### Simpler/no-change option
A per-operation semaphore or worker concurrency limit may solve the problem without new projects or infrastructure.

### Risks, failure modes and counterexamples
Independent queues can starve lower-priority users; too-small pools underutilize resources; process isolation adds operational cost and does not remove shared database saturation.

## Illustrative execution flow
A request or job enters its owning scope, checks cancellation/deadline, acquires only necessary concurrency budget, performs I/O or work, propagates result/error, and performs cleanup. For bounded producers, define a full-capacity policy and an explicit observation of lost/rejected work. This is an illustration—not verified code or prescribed queue architecture.

## Implementation, verification and rollback
Exercise mixed burst and steady loads; monitor p95/p99 by class, queue age, fairness, CPU/memory, errors and resource exhaustion. Compare baseline and rollback thresholds. Preserve business invariants, security and data safety over throughput gains. Identify open assumptions and distinguish observed measurement from reasoned hypothesis.

## Search aliases
workload isolation; workload isolation and concurrency budgets; async worker; concurrent requests; resource budgets; runtime safety

## Related concepts
- [backpressure](../runtime/backpressure.md)
- [workload-admission](../runtime/workload-admission.md)
- [resilience](../operations/resilience.md)

## Evidence and sources
1. Google SRE, Addressing cascading failures, https://sre.google/sre-book/addressing-cascading-failures/ (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.
2. Microsoft Learn, Channels, https://learn.microsoft.com/en-us/dotnet/core/extensions/channels (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.

## Maintenance
Reviewed 2026-11-07. Revisit when concurrency/runtime APIs change, overload incidents occur, external delivery requirements change or code-specific test evidence contradicts assumptions. Independent claim-to-source audit remains open.
