---
id: thread-safety
title: "Thread safety and shared state"
category: runtime
status: reviewed
reviewed_at: 2026-11-07
---

# Thread safety and shared state

> **Reviewed: platform-scoped decision guidance, not a measured target-system result.** Claims about .NET, Python, Java or Node features apply to the stated runtime; do not transfer API guarantees across languages.

## Problem and context
Parallel API requests or background jobs mutate a shared cache or singleton and produce lost updates.

## Applicability and preconditions
Gather runtime/language versions, API/Functions/WebJobs/worker execution model, workload distribution, shared resource ownership, cancellation/shutdown contract and actual latency/error evidence. A prototype may need only direct awaited I/O; independent worker deployments or advanced concurrency tools require measured need and ownership.

## Decision and trade-offs
First minimize shared mutable state and make ownership explicit. When state must be shared, choose a runtime-appropriate synchronization primitive or immutable message transfer and document memory visibility and lock scope.

### Simpler/no-change option
Per-request or per-job immutable state may avoid locks entirely; use a concurrent collection only when its compound operations match the needed invariant.

### Risks, failure modes and counterexamples
A thread-safe collection does not make multi-step business transactions atomic. Locking public objects or awaiting while holding incompatible locks can cause deadlocks; excessive locking can collapse throughput.

## Illustrative execution flow
A request or job enters its owning scope, checks cancellation/deadline, acquires only necessary concurrency budget, performs I/O or work, propagates result/error, and performs cleanup. For bounded producers, define a full-capacity policy and an explicit observation of lost/rejected work. This is an illustration—not verified code or prescribed queue architecture.

## Implementation, verification and rollback
Create repeatable interleaving and parallel stress tests; check invariant preservation, deadlocks, lock waits and observable races; roll back if concurrency safety or performance regresses. Preserve business invariants, security and data safety over throughput gains. Identify open assumptions and distinguish observed measurement from reasoned hypothesis.

## Search aliases
thread safety; thread safety and shared state; async worker; concurrent requests; resource budgets; runtime safety

## Related concepts
- [lock-contention-and-deadlocks](../runtime/lock-contention-and-deadlocks.md)
- [async-await](../runtime/async-await.md)
- [async-streams-and-channels](../runtime/async-streams-and-channels.md)

## Evidence and sources
1. Microsoft Learn, Managed threading best practices, https://learn.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.
2. Python 3.14 asyncio tasks, https://docs.python.org/3/library/asyncio-task.html (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.

## Maintenance
Reviewed 2026-11-07. Revisit when concurrency/runtime APIs change, overload incidents occur, external delivery requirements change or code-specific test evidence contradicts assumptions. Independent claim-to-source audit remains open.
