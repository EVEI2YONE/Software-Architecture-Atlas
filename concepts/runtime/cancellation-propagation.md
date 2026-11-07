---
id: cancellation-propagation
title: "Cancellation propagation and cleanup"
category: runtime
status: reviewed
reviewed_at: 2026-11-07
---

# Cancellation propagation and cleanup

> **Reviewed: platform-scoped decision guidance, not a measured target-system result.** Claims about .NET, Python, Java or Node features apply to the stated runtime; do not transfer API guarantees across languages.

## Problem and context
A cancelled HTTP request leaves downstream work or a queued job running, or cleanup swallows cancellation and traps shutdown.

## Applicability and preconditions
Gather runtime/language versions, API/Functions/WebJobs/worker execution model, workload distribution, shared resource ownership, cancellation/shutdown contract and actual latency/error evidence. A prototype may need only direct awaited I/O; independent worker deployments or advanced concurrency tools require measured need and ownership.

## Decision and trade-offs
Define cancellation ownership, deadline budget and points of propagation across I/O and child tasks. Use finally/defer cleanup and preserve cancellation signals unless a specifically documented shield is necessary.

### Simpler/no-change option
For a tiny bounded operation, a simple request timeout with local cleanup may suffice; avoid passing tokens indiscriminately into post-commit durability work that must complete or be retried.

### Risks, failure modes and counterexamples
Cancellation is cooperative: abandoned partial external effects still require idempotency/reconciliation. Python TaskGroup and timeout use cancellation internally and can misbehave when CancelledError is suppressed.

## Illustrative execution flow
A request or job enters its owning scope, checks cancellation/deadline, acquires only necessary concurrency budget, performs I/O or work, propagates result/error, and performs cleanup. For bounded producers, define a full-capacity policy and an explicit observation of lost/rejected work. This is an illustration—not verified code or prescribed queue architecture.

## Implementation, verification and rollback
Inject cancellation before start, mid-I/O, before commit and during shutdown; assert cleanup, persisted state and no orphan tasks. Test timeout precedence; restore previous behavior if recovery guarantees worsen. Preserve business invariants, security and data safety over throughput gains. Identify open assumptions and distinguish observed measurement from reasoned hypothesis.

## Search aliases
cancellation propagation; cancellation propagation and cleanup; async worker; concurrent requests; resource budgets; runtime safety

## Related concepts
- [async-await](../runtime/async-await.md)
- [structured-concurrency](../runtime/structured-concurrency.md)
- [resilience](../operations/resilience.md)

## Evidence and sources
1. Python 3.14 asyncio tasks, https://docs.python.org/3/library/asyncio-task.html (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.
2. Microsoft Learn, Task cancellation, https://learn.microsoft.com/en-us/dotnet/standard/parallel-programming/task-cancellation (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.

## Maintenance
Reviewed 2026-11-07. Revisit when concurrency/runtime APIs change, overload incidents occur, external delivery requirements change or code-specific test evidence contradicts assumptions. Independent claim-to-source audit remains open.
