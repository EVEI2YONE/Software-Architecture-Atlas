---
id: monorepo-vs-multirepo
title: "Monorepo versus multiple repositories"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Monorepo versus multiple repositories

> **Reviewed, scoped guidance.** Sources establish platform choices or tooling behavior; decision examples and stage recommendations are inferences pending evaluation in a real application.

## Problem and context
UI, API and jobs require coordinated contract changes, but some teams need distinct permissions and independent tooling.

## Applicability
Compare project kind (UI/API/Functions/WebJobs/libraries/multi-project), framework and version, prototype/MVP/growth/enterprise stage, business ownership, execution and deployment topology. Source-specific claims apply only to the named platform or tool. No runtime results or developer navigation measurements were observed for a target application.

## Decision and trade-offs
A monorepo enables atomic cross-project edits, shared tools and visibility; multiple repositories provide clearer repository-level access separation and independent workflows at the cost of cross-repo version coordination. Repository boundaries are not deployment boundaries.

### No-change and alternative approaches
Keep one repository for a small or strongly coupled product; use workspace-aware affected-project CI as the repository grows; separate repositories if access control, lifecycle or organizational independence outweighs coordination cost.

### Failure modes, costs and counterexamples
A monorepo with unrestricted imports and full builds on every PR can become costly. Polyrepos can hide downstream consumers and encourage drifting compatibility. Neither automatically guarantees independent deployment.

## Worked example (illustrative, not prescribed)
Illustrative: one repository with `apps/ui`, `apps/api`, `apps/jobs` and `packages/contracts` can still release apps separately; in polyrepos the contracts must be versioned and compatibility tested across releases.

## Verification, migration and rollback
Measure cross-repo PR count per feature, build duration, changed-project CI accuracy, access requirements, dependency drift and incident ownership. Try one representative cross-project change before migrating repositories; preserve history and plan rollback. Record no-change outcome, impacted files and evidence; if introducing a project/package, assess dependency versioning, builds and release overhead. Revisit on changed platform conventions, team ownership or measured navigation friction.

## Search aliases
monorepo vs multirepo; monorepo versus multiple repositories; developer navigation; module boundaries; code reuse; application code structure

## Related concepts
- [multi-project-structure](multi-project-structure.md)
- [module-public-contracts](module-public-contracts.md)
- [architecture-evolution](architecture-evolution.md)

## Evidence and sources
1. Nx, Monorepo vs Polyrepo: https://nx.dev/docs/kb/monorepo-vs-polyrepo (accessed 2026-11-07). Supports: Tool-vendor comparison of coordination, governance, CI and access; contextual rather than neutral evidence.
2. Nx, Enforce Module Boundaries: https://nx.dev/docs/features/enforce-module-boundaries (accessed 2026-11-07). Supports: One mechanism to govern imports inside a multi-project monorepo.

## Maintenance
Reviewed 2026-11-07. Do not infer measured code reduction, Sonar compliance or production readiness from this article. Independently recheck source versions and applicability on future reviews.
