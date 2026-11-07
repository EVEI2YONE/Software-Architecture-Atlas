---
id: resilience
title: "Resilience patterns"
category: operations
status: reviewed
reviewed_at: 2026-11-07
---

# Resilience patterns

> **Reviewed — scoped source-backed method, not a performance or reliability audit of any target system.**

## Supported scope
Google SRE documents overload and retry amplification as causes of cascading failure, and recommends capacity tests, load shedding, limited retries, backoff and jitter where appropriate. None of these patterns should be introduced by default without a failure scenario.

## Context and alternatives
For each dependency record timeout budget, idempotency, error classification, load profile and who owns recovery. A bounded timeout may be enough for a simple direct call. Retry only operations whose effects are safe to repeat, with attempt limits, jitter and one intentionally chosen retry layer. Circuit breakers and bulkheads add complexity; use only when they demonstrably prevent a particular overload or failure-propagation problem.

## Failure modes
Nested retries can multiply requests into an already failing service. Queues without bounds hide overload. Misconfigured health checks may worsen restarts; shedding load can harm lower-priority users. A feature flag alone does not restore data after corruption.

## Verification and rollback
Fault-inject latency, connection refusal, duplicate delivery and partial dependency failure. Verify bounded concurrency, upstream response, recovery and alerting. Preserve an escape hatch for bad resilience configuration. Do not claim a circuit breaker or retry policy improves reliability without a test against the target workload.

## Search aliases
resilience; operational diagnostics; application performance; incident investigation; runtime architecture

## Related concepts
- [idempotency](../distributed-systems/idempotency.md)
- [observability](../operations/observability.md)

## Trading data failure behavior

For source timeouts, stale observations, missing candles and explicit SKIP decisions rather than unverified fallback prices, see [Trading market-data integrity](../data/trading-market-data-integrity.md). Retry policies must not make stale trading data appear current.

## Evidence and sources
1. Google SRE Addressing Cascading Failures: https://sre.google/sre-book/addressing-cascading-failures/ (accessed 2026-11-07).
2. Google SRE Production Services Best Practices: https://sre.google/sre-book/service-best-practices/ (accessed 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Revisit on new source revisions, platform migration, observed incidents or workload changes.
