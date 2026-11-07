---
id: backpressure
title: "Backpressure and bounded concurrency"
category: runtime
status: reviewed
reviewed_at: 2026-11-07
---

# Backpressure and bounded concurrency

> **Reviewed: platform-scoped decision guidance, not a measured target-system result.** Claims about .NET, Python, Java or Node features apply to the stated runtime; do not transfer API guarantees across languages.

## Problem and context
Producers generate API or job work faster than workers can consume it, causing unbounded queues and memory growth.

## Applicability and preconditions
Gather runtime/language versions, API/Functions/WebJobs/worker execution model, workload distribution, shared resource ownership, cancellation/shutdown contract and actual latency/error evidence. A prototype may need only direct awaited I/O; independent worker deployments or advanced concurrency tools require measured need and ownership.

## Decision and trade-offs
Choose bounded work admission and an explicit full-capacity policy—wait, reject or drop only if business semantics permit it. Couple queue depth with consumer concurrency, timeouts and cancellation; distinguish local in-process channels from durable broker queues.

### Simpler/no-change option
A small bounded pool or simply declining extra requests may be enough; avoid introducing a broker solely to smooth an unmeasured burst.

### Risks, failure modes and counterexamples
Dropping financial/job tasks is unsafe if loss is not acceptable. Waiting without a deadline may merely shift saturation upstream; retry amplification can worsen overload.

## Illustrative execution flow
A request or job enters its owning scope, checks cancellation/deadline, acquires only necessary concurrency budget, performs I/O or work, propagates result/error, and performs cleanup. For bounded producers, define a full-capacity policy and an explicit observation of lost/rejected work. This is an illustration—not verified code or prescribed queue architecture.

## Implementation, verification and rollback
Load-test sustained and burst arrival rates; record queue depth, backlog age, rejection/drop count, latency and resource use. Test full queue, cancellation and shutdown; revert if loss or overload behavior violates requirements. Preserve business invariants, security and data safety over throughput gains. Identify open assumptions and distinguish observed measurement from reasoned hypothesis.

## Search aliases
backpressure; backpressure and bounded concurrency; async worker; concurrent requests; resource budgets; runtime safety

## Related concepts
- [async-streams-and-channels](../runtime/async-streams-and-channels.md)
- [workload-admission](../runtime/workload-admission.md)
- [queues](../distributed-systems/queues.md)

## Evidence and sources
1. Microsoft Learn, Channels, https://learn.microsoft.com/en-us/dotnet/core/extensions/channels (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.
2. Google SRE, Addressing cascading failures, https://sre.google/sre-book/addressing-cascading-failures/ (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.
3. Node.js, Streams backpressure, https://nodejs.org/en/learn/modules/backpressuring-in-streams (accessed 2026-11-07). Primary platform documentation or original SRE guidance; check runtime/version support and exact applicable behavior.

## Maintenance
Reviewed 2026-11-07. Revisit when concurrency/runtime APIs change, overload incidents occur, external delivery requirements change or code-specific test evidence contradicts assumptions. Independent claim-to-source audit remains open.
