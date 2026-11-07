---
id: structured-concurrency
title: "Structured concurrency and task ownership"
category: runtime
status: reviewed
reviewed_at: 2026-11-07
---

# Structured concurrency and task ownership

> **Reviewed: platform-scoped decision guidance, not a measured target-system result.** Claims about .NET, Python, Java or Node features apply to the stated runtime; do not transfer API guarantees across languages.

## Problem and context
Spawned child tasks outlive their originating request or job; parent failure leaves incomplete tasks unobserved.

## Applicability and preconditions
Gather runtime/language versions, API/Functions/WebJobs/worker execution model, workload distribution, shared resource ownership, cancellation/shutdown contract and actual latency/error evidence. A prototype may need only direct awaited I/O; independent worker deployments or advanced concurrency tools require measured need and ownership.

## Decision and trade-offs
Tie related child tasks to a lexical/owned scope whose exit awaits, cancels and observes child outcomes according to documented policy. Python 3.14 asyncio.TaskGroup and Java 25 structured concurrency are concrete but not interchangeable APIs.

### Simpler/no-change option
Sequential await is simplest when parallelism provides no meaningful latency benefit; explicit awaited tasks can suffice when structured scope primitives are unavailable.

### Risks, failure modes and counterexamples
Java 25 structured concurrency uses a preview API, requiring version and preview support checks. Python cancellation suppression can break TaskGroup semantics; scope completion alone does not guarantee external transaction atomicity.

## Illustrative execution flow
A request or job enters its owning scope, checks cancellation/deadline, acquires only necessary concurrency budget, performs I/O or work, propagates result/error, and performs cleanup. For bounded producers, define a full-capacity policy and an explicit observation of lost/rejected work. This is an illustration—not verified code or prescribed queue architecture.

## Implementation, verification and rollback
Test one-child failure, parent cancellation, slow child, deadline and cleanup; assert all children settle and failure surfaces. Measure parallelism benefit against resource cost and roll back excess concurrency. Preserve business invariants, security and data safety over throughput gains. Identify open assumptions and distinguish observed measurement from reasoned hypothesis.

## Search aliases
structured concurrency; structured concurrency and task ownership; async worker; concurrent requests; resource budgets; runtime safety

## Related concepts
- [async-await](../runtime/async-await.md)
- [cancellation-propagation](../runtime/cancellation-propagation.md)
- [workload-isolation](../runtime/workload-isolation.md)

## Evidence and sources
1. Python 3.14 asyncio tasks, https://docs.python.org/3/library/asyncio-task.html (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.
2. Oracle Java 25, Structured concurrency, https://docs.oracle.com/en/java/javase/25/core/structured-concurrency.html (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.

## Maintenance
Reviewed 2026-11-07. Revisit when concurrency/runtime APIs change, overload incidents occur, external delivery requirements change or code-specific test evidence contradicts assumptions. Independent claim-to-source audit remains open.
