---
id: async-await
title: "Async/await and cancellation"
category: runtime
status: reviewed
reviewed_at: 2026-11-07
---

# Async/await and cancellation

> **Reviewed: platform-scoped decision guidance, not a measured target-system result.** Claims about .NET, Python, Java or Node features apply to the stated runtime; do not transfer API guarantees across languages.

## Problem and context
An API or worker blocks an I/O-bound task on a thread, or launches a task without awaiting its failure.

## Applicability and preconditions
Gather runtime/language versions, API/Functions/WebJobs/worker execution model, workload distribution, shared resource ownership, cancellation/shutdown contract and actual latency/error evidence. A prototype may need only direct awaited I/O; independent worker deployments or advanced concurrency tools require measured need and ownership.

## Decision and trade-offs
Distinguish asynchronous I/O from CPU parallelism. Await returned tasks and propagate errors to the owning scope. Avoid synchronous blocking on async operations in execution contexts where it can deadlock or starve worker threads.

### Simpler/no-change option
A direct synchronous call is often simplest when it is truly cheap, nonblocking, and within an appropriate runtime model. Do not wrap synchronous CPU work in async merely to change its signature.

### Risks, failure modes and counterexamples
Fire-and-forget tasks may lose exceptions and outlive request scopes; excessive Task.Run around I/O can consume thread-pool workers. Cancellation is cooperative, not guaranteed immediate termination.

## Illustrative execution flow
A request or job enters its owning scope, checks cancellation/deadline, acquires only necessary concurrency budget, performs I/O or work, propagates result/error, and performs cleanup. For bounded producers, define a full-capacity policy and an explicit observation of lost/rejected work. This is an illustration—not verified code or prescribed queue architecture.

## Implementation, verification and rollback
Instrument task completion/errors and thread-pool saturation; test timeout, cancellation, exception and shutdown paths under realistic I/O. Refactor one call chain and roll back if latency, failure behavior or resource use worsens. Preserve business invariants, security and data safety over throughput gains. Identify open assumptions and distinguish observed measurement from reasoned hypothesis.

## Search aliases
async await; async/await and cancellation; async worker; concurrent requests; resource budgets; runtime safety

## Related concepts
- [cancellation-propagation](../runtime/cancellation-propagation.md)
- [structured-concurrency](../runtime/structured-concurrency.md)
- [thread-safety](../runtime/thread-safety.md)

## Evidence and sources
1. Microsoft Learn, Asynchronous programming with async and await, https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/ (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.
2. Microsoft Learn, Task cancellation, https://learn.microsoft.com/en-us/dotnet/standard/parallel-programming/task-cancellation (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.
3. Python 3.14 asyncio tasks, https://docs.python.org/3/library/asyncio-task.html (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.

## Maintenance
Reviewed 2026-11-07. Revisit when concurrency/runtime APIs change, overload incidents occur, external delivery requirements change or code-specific test evidence contradicts assumptions. Independent claim-to-source audit remains open.
