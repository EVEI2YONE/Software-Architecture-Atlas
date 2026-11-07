---
id: incremental-boundary-migration
title: "Incremental module extraction and consolidation"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Incremental module extraction and consolidation

> **Reviewed, scoped sources and clearly marked inferred decision heuristics.** No real application or migration was evaluated.

## Purpose and scope
Move one cohesive capability across module, package or deployment boundaries without a risky big-bang rewrite. AWS documents two alternatives: **strangler fig** for interceptable external traffic and **branch by abstraction** for deeply embedded internals. These are candidate migration methods, not requirements to convert a monolith into services.

## Decision method
1. **Stay put:** When navigation, change lead time and release safety already meet requirements, do not extract.
2. **Internal module:** First try grouping a cohesive capability in the same deployable and enforcing public imports without network overhead.
3. **Branch by abstraction:** If an internal implementation has many upstream callers, introduce a minimal seam to support old/new implementations, gradually switch consumers and remove the temporary compatibility layer.
4. **Strangler fig:** When traffic can be intercepted, gradually route selected entrypoints to a replacement, run new/old systems in parallel and retire legacy paths after verified cutover. AWS identifies proxy bottlenecks and unsuitable small systems as counterexamples.
5. **Consolidate:** If independently deployed pieces create more coordination than value, evaluate merging while preserving contracts and ownership.

## Illustration (not a target project)
```text
before: api -> legacy Orders module -> shared database
during: api -> small boundary -> legacy Orders OR new Orders
after:  api -> new Orders module
```
This tree is conceptual. Moving data ownership or routing between processes additionally requires authentication, migration, retries, idempotency and failure semantics.

## Tests and decision evidence
Capture dependency graph, entrypoints, API and event consumers, storage ownership, caller-side assumptions and release topology. Run contract tests against both implementations, compare outputs and error behavior, confirm rollback route, and monitor latency/throughput and error budgets in production. Remove temporary proxies and adapters after confidence is established.

## Failure modes
Premature boundaries fracture transactions and introduce outages; long-lived adapters become permanent accidental complexity; duplicated writes diverge; routing bridges create a new critical dependency. No migration should be declared complete until ownership, data, rollout, observability and rollback are verified.

## Evidence limits
AWS guidance supports migration **mechanisms**, not a proof that decomposing or consolidating is universally beneficial. Exact architecture decisions require the real system context.

## Search aliases
incremental boundary migration; prototype MVP growth enterprise; project splitting; consolidation; modular monolith; business scaling

## Related concepts
- [architecture-evolution](../code-organization/architecture-evolution.md)
- [modularity](../code-organization/modularity.md)
- [api-contracts](../distributed-systems/api-contracts.md)
- [schema-evolution](../data/schema-evolution.md)

## Sources
1. AWS Strangler fig pattern: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/strangler-fig.html (consulted 2026-11-07).
2. AWS Branch by abstraction: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/branch-by-abstraction.html (consulted 2026-11-07).
3. AWS Decompose by subdomain: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/decompose-subdomain.html (consulted 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Revisit after relevant platform or migration-guidance changes or contradictory measured results.
