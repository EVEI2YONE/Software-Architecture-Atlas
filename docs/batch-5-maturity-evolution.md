# B5 — Product maturity, architecture evolution and consolidation

**Batch:** B5 · **Gaps:** GAP-13 (growth axis), GAP-05 (boundary selection), GAP-11 (operational ownership).  
**Research date:** 2026-11-07. **Result:** Source-based evolution and migration methods documented; real-system evidence remains unknown.

## Context gathered first

The Atlas now covers file structure across six project types (B4), source-backed navigability and simpler code (B1), module/deployable boundaries (B2), and contracts/security/data (B3). Its cross-cutting `project-structure-selection` remains an unverified research stub. No real prototype, MVP, growing-business or enterprise application was supplied for objective navigation, build or release measurements.

**Research sources and applicability:**
- [Microsoft: Common web application architectures](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures) compares one-project and multi-project solutions and emphasizes logical/physical separation. It is .NET-web-app-oriented.
- [AWS: Decompose by subdomain](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/decompose-subdomain.html) evaluates subdomain boundaries and warns of too many services; it is migration guidance, not proof every growing business should split.
- [AWS: Strangler fig](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/strangler-fig.html) addresses incremental coexistence, routing and rollback; it notes small-system and proxy constraints.
- [AWS: Branch by abstraction](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/branch-by-abstraction.html) describes replacing deeply embedded components through a temporary seam.

All consulted 2026-11-07. The **stage mapping below is an inferred decision aid**; no referenced source prescribes a fixed project layout by company size.

## Stage × project-type evolution matrix (illustrative)

| Project type | Prototype | MVP | Growing business | Enterprise |
| --- | --- | --- | --- | --- |
| UI | Framework-native routes/components, few folders | Group proven features and tests | Shared design system only for stable cross-feature requirements | Explicit ownership, accessible common components and versioned consumer contracts |
| API | Clear few endpoints in one deployable | Validated contracts, concise domain features | Internal modules and explicit domain ownership | Independent services only for demonstrated scale/release/security boundaries |
| Functions | Trigger-local logic in one supported host | Test retries and permissions | Split hosts if scale, settings or release cadence warrant | Independent operational owners, deployment pipelines and runtime budgets |
| WebJobs / workers | Focused job entrypoint and tests | Safe scheduling and retry behavior | Separate job packages for distinct deploy/recovery requirements | Auditable workload isolation, runbooks and operational ownership |
| Libraries | Internal function/module first | Extract when multiple actual consumers emerge | Stable public APIs and consumer-compatibility tests | Versioning and ownership agreements, not a single mega-shared library |
| Multi-project | Minimal projects, possibly one | Only necessary UI/API/job execution units | Capability modules with selective independent deployment | Enforced dependency contracts and lifecycle; modular monolith remains viable |

**These are candidate structures, not rules or guaranteed productivity improvements.** Runtime-specific conventions in B4 override hypothetical trees.

## Evidence-based transition gates

1. **Navigation:** a representative feature change repeatedly crosses unrelated technical folders. Try moving files within the same deployable before adding projects.
2. **Cohesion/coupling:** independently changing business capabilities share circular references or unstable common packages. Try narrow module boundaries; measure cycles and files touched.
3. **Reuse:** two real consumers share semantics, version expectations and ownership. Evaluate a local shared module against a published package.
4. **Deployment:** measured release coordination, scaling needs, or separate availability/security requirements exceed the cost of service networking, contracts and operations.
5. **Consolidation:** multiple services/packages repeatedly require synchronized releases, duplicate auth/observability and operational support. Evaluate merging rather than assuming growth only means splitting.

Compare each trigger against **no change**; gather team ownership, release cadence, build/test time, incident and workload data before selecting an architecture. There are no universal numeric thresholds.

## Two migration paths

**Path A — grow without distribution:** preserve one deployable; group stable capabilities; map dependencies; use internal interfaces only at meaningful boundaries; run integration tests; evaluate task navigation; revert if overhead increases.

**Path B — isolate only a justified capability:** record the autonomous release/scaling driver; define contract, identity and data compatibility; if traffic interceptable consider strangler fig, if deeply embedded consider branch by abstraction; measure behavior while old and new coexist; plan rollback and deletion of temporary adapters. Reject extraction if an internal module meets the need more cheaply.

## Worked example (hypothetical)

A shop starts as an API with payment callback and settlement worker. At MVP, tests and idempotency become necessary; do not automatically create a dedicated payments service. During growth, Orders and Billing are frequently changed together. First measure and align internal modules. At enterprise scale, the same modules may remain within a deployable if release and scaling constraints allow. If a separate settlement team's release needs repeatedly block changes, evaluate a job/deployable boundary with explicit contracts and operational ownership. **Not evidence of a real repository.**

## Verification and acceptance

Record baseline and paired experiments: file hops to change a feature, touched files, net maintained LOC (exclude generated code), module cycles, package/deployable count, build and release duration, consumer contract tests, security, failover, costs and rollback. Pilot one reversible change and seek developer feedback. A stage label alone is **not** an acceptance criterion.

## Curated artifacts

- [Architecture evolution by product maturity](../concepts/code-organization/architecture-evolution.md) — source-backed alternatives, inferred stage triggers and consolidation.
- [Incremental module extraction and consolidation](../concepts/code-organization/incremental-boundary-migration.md) — strangler fig, branch-by-abstraction, no-change and rollback.

**B5 state: partially curated.** No real project evolution or metrics evaluated. GAP-11 operational costs/ownership remain in B6; GAP-13 cross-type structure-selection remains a stub until target applicability and migration measurements are established.

## Agent retrieval instructions

Run `python scripts/search_catalog.py "prototype MVP enterprise architecture" --json` or `python scripts/search_catalog.py "strangler migration" --json`. Inspect sources and distinguish reviewed *method* from an unmeasured architecture recommendation; do not use company-size labels as automatic microservice triggers.
