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

## B18: durable worker observability overlay

Instrument **business progress**, not merely HTTP process health. A responding worker can still have an expired lease or an indefinitely stale due queue. Proposed monitored signals include oldest due-job age, last successfully persisted evaluation age, lease renewal failures, claim conflicts, expired lease count, retry/terminal-failure counts and B17 market-data rejection reasons. Treat metric names, units, bounds and alert thresholds as **application choices**, not predefined OpenTelemetry conventions. Keep customer identifiers and credentials out of public/high-cardinality metric labels. Verify actual alert delivery and redaction with failure injection before asserting readiness.

See the [B18 monitoring and verification runbook](../../docs/batch-18-production-verification.md) for a proposed telemetry table and restart/recovery drills. B16 owns lease fencing; instrumentation does not prove it is correct. References: [OpenTelemetry Metrics Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/general/metrics/) and [Google SRE SLOs](https://sre.google/sre-book/service-level-objectives/), checked 2026-11-07.

## Evidence and sources
1. OpenTelemetry Documentation: https://opentelemetry.io/docs/ (accessed 2026-11-07).
2. OpenTelemetry Semantic Conventions: https://opentelemetry.io/docs/concepts/semantic-conventions/ (accessed 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Revisit on new source revisions, platform migration, observed incidents or workload changes.
