---
id: observability
title: "Observability and diagnostics"
category: operations
status: reviewed
reviewed_at: 2026-11-07
---

# Observability and diagnostics

> **Reviewed — scoped source-backed method, not a performance or reliability audit of any target system.**

## Supported scope
OpenTelemetry describes vendor-neutral traces, metrics and logs. Its semantic conventions define shared names across libraries and signals. Instrumentation is a means to inspect a system, not a guarantee that it meets a reliability objective.

## Minimal diagnostic path
Start with one important user journey and a clear service or job owner. Choose a small set of user-facing symptoms, including request success ratio or queue completion age. Add structured logs and correlation IDs and propagate trace context across API/worker boundaries **only where needed**. Choose labels with controlled cardinality, reasonable sampling and privacy controls; do not record passwords, tokens or sensitive payloads.

## Alternatives and trade-offs
A small prototype may need actionable logs and a couple of health metrics, not a full telemetry pipeline. Distributed traces become useful when user-visible latency or failures span services. Every telemetry signal adds storage, cost, instrumentation and possible data-exposure risk.

## Verification and rollback
Trace a representative request through an actual API, Function or WebJob; verify failure/timeout logs, redaction, alert delivery and missing-context behavior. Compare before/after diagnosis tasks, not metric counts. Roll back noisy or sensitive instrumentation while retaining critical incident signals. No target deployment was instrumented or evaluated.

## Search aliases
observability; operational diagnostics; application performance; incident investigation; runtime architecture

## Related concepts
- [scalability](../performance/scalability.md)
- [caching](../performance/caching.md)

## Evidence and sources
1. OpenTelemetry Documentation: https://opentelemetry.io/docs/ (accessed 2026-11-07).
2. OpenTelemetry Semantic Conventions: https://opentelemetry.io/docs/concepts/semantic-conventions/ (accessed 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Revisit on new source revisions, platform migration, observed incidents or workload changes.
