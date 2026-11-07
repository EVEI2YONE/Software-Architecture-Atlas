# B11 — Asynchronous programming and concurrency safety

**Date:** 2026-11-07. **Branch:** `curation/b7-b14-knowledge-gaps-20261107`. **Shared draft PR:** #3. **Scope:** reference catalog; no target application was inspected.

## Context and deduplication gathered before concept edits
The B10 branch had 71 indexed concepts, 64 reviewed and 7 stubs. B11 specifically inherited three runtime stubs: `async-await`, `thread-safety`, and `backpressure`. The existing reviewed `workload-admission` in `concepts/runtime/` and `resilience` in `concepts/operations/` already cover parts of admission and retry amplification. This batch does not recreate those topics; it adds narrower decision guidance around task ownership, cancellation, locks, workload isolation and local channels.

Primary authoritative material consulted on 2026-11-07:
- [.NET asynchronous programming](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/), [.NET task cancellation](https://learn.microsoft.com/en-us/dotnet/standard/parallel-programming/task-cancellation), [.NET managed threading](https://learn.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices) and [.NET channels](https://learn.microsoft.com/en-us/dotnet/core/extensions/channels).
- [Python 3.14 asyncio TaskGroup and cancellation](https://docs.python.org/3/library/asyncio-task.html).
- [Oracle Java 25 structured concurrency](https://docs.oracle.com/en/java/javase/25/core/structured-concurrency.html) (preview API; do not imply universally available/stable).
- [Node.js streams backpressure](https://nodejs.org/en/learn/modules/backpressuring-in-streams).
- [Google SRE cascading failures](https://sre.google/sre-book/addressing-cascading-failures/).

These support runtime-specific semantics and failure modes, not real-world benefits for an uninspected application. Concurrency bugs and timings require actual workload tests.

## Scope decisions
1. `async-await`: awaiting, exceptions and async I/O versus CPU parallelism. Do not assume async improves CPU throughput.
2. `thread-safety`: shared mutable state, memory safety and synchronization. Do not equate a thread-safe collection with an atomic business transaction.
3. `backpressure`: overload behavior, queue capacity and explicit wait/reject/drop policy. Durable broker semantics remain B12 `queues`.
4. `cancellation-propagation`: cooperative stop, cleanup and partial effects.
5. `structured-concurrency`: parent/child task lifetime and errors. Python TaskGroup is a different API from Java 25 preview structured concurrency.
6. `lock-contention-and-deadlocks`: ordering, lock scope and contention diagnosis.
7. `workload-isolation`: budget separate classes of API/worker work; reuse `workload-admission` for generic overload guidance.
8. `async-streams-and-channels`: incremental local producer-consumer processing, bounded channels and termination. Do not imply persistence across a process crash.

## Decision/experiment matrix — hypothetical
| Situation | Simpler/no-change candidate | When to add control | Actual verification required |
| --- | --- | --- | --- |
| API awaits one outbound request | Direct awaited call with timeout | Parallel independent I/O only after latency evidence | Failure, timeout, cancellation and task ownership tests |
| WebJob writes shared state | Per-job state, immutable message or one owner | Synchronization needed across shared writes | Stress and interleaving tests, race/deadlock tracking |
| Function overload | Reject/defer when overloaded | Bounded channel or controlled pool for sustained consumer mismatch | Queue depth/age, full-capacity behavior and loss policy |
| Nested workers | Sequential work | Structured scope if child concurrency helps | Parent cancel, child fault, cleanup and no orphan tasks |
| Mixed critical and bulk jobs | Limit global concurrency | Per-class isolation after proven starvation | p95/p99 per class, memory, errors and fairness |
| Stream of events | Finite list for small bounded data | Streaming/channel when incremental processing lowers peak buffering | Slow reader, writer closure, cancellation and memory |

## Deliverables
- Promoted three existing stubs and added five narrowly scoped runtime concepts.
- Updated canonical index and runtime README.
- Target branch index after concept curation: **76 concepts, 72 reviewed, 4 stubs**.
- Retrieval tests and golden-query fixture require status updates because all runtime stubs are now reviewed; retain `caching` or another genuine remaining stub for negative evidence tests.

## Validation and limitations
Run `python scripts/validate_catalog.py` and `python -m unittest discover -s tests -v` using PR GitHub Actions and record actual workflow result. Cross-check all eight pages for source count, links and frontmatter. No application build, load test, resource measurement, race repro, security assessment or production incident response was performed. Thus all benefit estimates are inferred, not observed.
