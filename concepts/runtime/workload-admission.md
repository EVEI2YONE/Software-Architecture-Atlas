---
id: workload-admission
title: "Workload admission, concurrency and overload"
category: runtime
status: reviewed
reviewed_at: 2026-11-07
---

# Workload admission, concurrency and overload

> **Reviewed — limited to cited source methods.** No real workload, incident recovery, financial cost or deployment has been measured.

## Supported scope
Google SRE documents overloaded services cascading through resource exhaustion and retry amplification. Concurrency limits, bounded queues, timeouts and admission control can help preserve useful work. Limits and shed policies must reflect actual workload and user priorities.

## Decision questions
What is arrival rate, service time, queue-depth trend, job deadline and per-request resource cost? What happens to consumers when full: wait, reject with meaningful status, defer or drop lower-priority work? Who owns dead-letter queues and retry budgets? Can requests safely be retried?

## Options and counterexamples
A small low-volume API might need no separate queue and benefit from keeping direct calls. A boundless queue conceals overload and increases latency; a circuit breaker without recovery testing might worsen the service. Overly aggressive shedding can reject priority traffic. Avoid unlimited retry layers.

## Verification
Test burst, sustained overload, downstream slowdown and recovery; capture throughput, p95/p99 latency, rejection rate, queue age, memory and retry amplification. Ensure backpressure crosses upstream boundaries and that retries respect idempotency. Stop changes that improve averages but harm tail behavior or correctness. Values must be measured per service; no universal queue depth is prescribed.

## Search aliases
workload admission; operations; service reliability; enterprise runtime; resource budgets

## Related concepts
- [backpressure](../runtime/backpressure.md)
- [queues](../distributed-systems/queues.md)
- [resilience](../operations/resilience.md)

## Evidence and sources
1. Google SRE Addressing Cascading Failures: https://sre.google/sre-book/addressing-cascading-failures/ (accessed 2026-11-07).
2. Google SRE Production Services Best Practices: https://sre.google/sre-book/service-best-practices/ (accessed 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Revisit on incident, major platform/version changes or conflicting measurements.
