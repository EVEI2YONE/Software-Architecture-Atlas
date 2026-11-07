---
id: lock-contention-and-deadlocks
title: "Lock contention and deadlocks"
category: runtime
status: reviewed
reviewed_at: 2026-11-07
---

# Lock contention and deadlocks

> **Reviewed: platform-scoped decision guidance, not a measured target-system result.** Claims about .NET, Python, Java or Node features apply to the stated runtime; do not transfer API guarantees across languages.

## Problem and context
Two workers acquire shared locks in opposite order, or hold a lock while awaiting slow I/O.

## Applicability and preconditions
Gather runtime/language versions, API/Functions/WebJobs/worker execution model, workload distribution, shared resource ownership, cancellation/shutdown contract and actual latency/error evidence. A prototype may need only direct awaited I/O; independent worker deployments or advanced concurrency tools require measured need and ownership.

## Decision and trade-offs
Prefer fewer shared mutable owners, narrow lock scopes and a consistent acquisition order when multiple locks are unavoidable. Diagnose actual blocking, contention and queueing rather than automatically replacing locks with custom concurrency layers.

### Simpler/no-change option
Use immutable data or a single owner/queue instead of locks where feasible; retain a simple private lock for short critical sections.

### Risks, failure modes and counterexamples
Locking on globally visible objects admits unrelated callers; reentrant or async waiting behavior differs by runtime. Removing a lock without proving invariants introduces races.

## Illustrative execution flow
A request or job enters its owning scope, checks cancellation/deadline, acquires only necessary concurrency budget, performs I/O or work, propagates result/error, and performs cleanup. For bounded producers, define a full-capacity policy and an explicit observation of lost/rejected work. This is an illustration—not verified code or prescribed queue architecture.

## Implementation, verification and rollback
Capture thread dumps, lock metrics and reproducible interleavings; test concurrent updates and fairness/cancellation. Change one lock boundary and roll back on races or starvation. Preserve business invariants, security and data safety over throughput gains. Identify open assumptions and distinguish observed measurement from reasoned hypothesis.

## Search aliases
lock contention and deadlocks; lock contention and deadlocks; async worker; concurrent requests; resource budgets; runtime safety

## Related concepts
- [thread-safety](../runtime/thread-safety.md)
- [workload-isolation](../runtime/workload-isolation.md)
- [async-streams-and-channels](../runtime/async-streams-and-channels.md)

## Evidence and sources
1. Microsoft Learn, Managed threading best practices, https://learn.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.
2. Microsoft Learn, Channels, https://learn.microsoft.com/en-us/dotnet/core/extensions/channels (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.

## Maintenance
Reviewed 2026-11-07. Revisit when concurrency/runtime APIs change, overload incidents occur, external delivery requirements change or code-specific test evidence contradicts assumptions. Independent claim-to-source audit remains open.
