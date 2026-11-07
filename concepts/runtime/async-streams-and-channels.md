---
id: async-streams-and-channels
title: "Async streams and channels"
category: runtime
status: reviewed
reviewed_at: 2026-11-07
---

# Async streams and channels

> **Reviewed: platform-scoped decision guidance, not a measured target-system result.** Claims about .NET, Python, Java or Node features apply to the stated runtime; do not transfer API guarantees across languages.

## Problem and context
A function buffers an entire result set or event batch before a consumer can process it, increasing memory and latency.

## Applicability and preconditions
Gather runtime/language versions, API/Functions/WebJobs/worker execution model, workload distribution, shared resource ownership, cancellation/shutdown contract and actual latency/error evidence. A prototype may need only direct awaited I/O; independent worker deployments or advanced concurrency tools require measured need and ownership.

## Decision and trade-offs
Choose streaming or bounded channels when incremental processing and backpressure are supported; specify completion, error propagation, cancellation and full-buffer behavior. Distinguish in-memory channels from durable queues requiring replay and delivery guarantees.

### Simpler/no-change option
A list or direct synchronous iterator is simpler for small finite data; do not introduce a channel without producer/consumer decoupling need.

### Risks, failure modes and counterexamples
Unbounded buffers hide load; drop modes can irrecoverably lose business work; a consumer crash may lose in-memory messages. Multi-reader/channel semantics vary by runtime.

## Illustrative execution flow
A request or job enters its owning scope, checks cancellation/deadline, acquires only necessary concurrency budget, performs I/O or work, propagates result/error, and performs cleanup. For bounded producers, define a full-capacity policy and an explicit observation of lost/rejected work. This is an illustration—not verified code or prescribed queue architecture.

## Implementation, verification and rollback
Test slow consumer, closed writer, cancellation, consumer faults and capacity limits. Measure memory footprint, throughput and lost-work policy; roll back if semantics or observability regress. Preserve business invariants, security and data safety over throughput gains. Identify open assumptions and distinguish observed measurement from reasoned hypothesis.

## Search aliases
async streams and channels; async streams and channels; async worker; concurrent requests; resource budgets; runtime safety

## Related concepts
- [backpressure](../runtime/backpressure.md)
- [async-await](../runtime/async-await.md)
- [queues](../distributed-systems/queues.md)

## Evidence and sources
1. Microsoft Learn, Channels, https://learn.microsoft.com/en-us/dotnet/core/extensions/channels (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.
2. Node.js, Streams backpressure, https://nodejs.org/en/learn/modules/backpressuring-in-streams (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.
3. Python 3.14 asyncio tasks, https://docs.python.org/3/library/asyncio-task.html (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.

## Maintenance
Reviewed 2026-11-07. Revisit when concurrency/runtime APIs change, overload incidents occur, external delivery requirements change or code-specific test evidence contradicts assumptions. Independent claim-to-source audit remains open.
