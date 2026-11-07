---
id: architecture-dependency-rules
title: "Architecture dependency rules"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Architecture dependency rules

> **Reviewed, scoped guidance.** Sources establish platform choices or tooling behavior; decision examples and stage recommendations are inferences pending evaluation in a real application.

## Problem and context
Independent projects silently import deep private folders or develop cyclic references, increasing regression scope.

## Applicability
Compare project kind (UI/API/Functions/WebJobs/libraries/multi-project), framework and version, prototype/MVP/growth/enterprise stage, business ownership, execution and deployment topology. Source-specific claims apply only to the named platform or tool. No runtime results or developer navigation measurements were observed for a target application.

## Decision and trade-offs
Write an explicit allowed dependency matrix (for example entrypoints→application capabilities→domain contracts; infrastructure implements ports) for the actual build graph. Enforce only high-value invariants using imports, package visibility, compiler references or build/test tooling.

### No-change and alternative approaches
A small project may rely on documented ownership and code review; a workspace with growing cycles can add targeted lint restrictions. Avoid a bespoke architecture testing framework unless an observed failure justifies it.

### Failure modes, costs and counterexamples
Overly restrictive rules break valid test adapters or generated code; exemptions with no owner make rules ceremonial. Import lint can miss reflection, runtime plugin discovery and dynamically resolved dependencies.

## Worked example (illustrative, not prescribed)
Illustrative `web -> orders/public`, `jobs -> orders/public`, `orders -> shared-kernel`, but `shared-kernel -X-> web`; enforce via workspace tags or compiler/package checks where available.

## Verification, migration and rollback
Capture imports and project references; establish a failing example for a forbidden dependency; run CI and inspect exceptions and false positives. Migrate cycles incrementally, run integration tests and roll back rules if they block genuine platform constraints. Record no-change outcome, impacted files and evidence; if introducing a project/package, assess dependency versioning, builds and release overhead. Revisit on changed platform conventions, team ownership or measured navigation friction.

## Search aliases
architecture dependency rules; architecture dependency rules; developer navigation; module boundaries; code reuse; application code structure

## Related concepts
- [modularity](modularity.md)
- [module-public-contracts](module-public-contracts.md)
- [dependency-inversion](dependency-inversion.md)

## Evidence and sources
1. Nx, Enforce Module Boundaries: https://nx.dev/docs/features/enforce-module-boundaries (accessed 2026-11-07). Supports: Tagged dependency constraints; language-specific lint vs licensed language-agnostic conformance.
2. Microsoft Learn, Common web application architectures: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07). Supports: Layer direction and multi-project architectural boundaries.

## Maintenance
Reviewed 2026-11-07. Do not infer measured code reduction, Sonar compliance or production readiness from this article. Independently recheck source versions and applicability on future reviews.
