# B8 — Application structure, modularity and navigation

Date: 2026-11-07. Campaign: [B7–B14 context and progress](b7-b14-campaign.md). Branch: `curation/b7-b14-knowledge-gaps-20261107`, shared PR #3.

## Context gathered before implementation
- Reviewed canonical index on the campaign branch: 52 entries (35 reviewed, 17 stubs). `project-structure-selection` remained the sole code-organization stub.
- Existing relevant reviewed guidance: [feature-first folders](../concepts/code-organization/feature-first-folders.md), [modularity](../concepts/code-organization/modularity.md), [multi-project solution](../concepts/code-organization/multi-project-structure.md), [architecture evolution](../concepts/code-organization/architecture-evolution.md), [incremental boundary migration](../concepts/code-organization/incremental-boundary-migration.md), and six application-type archetypes.
- Source review: Microsoft Learn [Common web application architectures](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures) and [Developing ASP.NET Core MVC apps](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/develop-asp-net-core-mvc-apps), Nx [Enforce Module Boundaries](https://nx.dev/docs/features/enforce-module-boundaries) and [Monorepo vs Polyrepo](https://nx.dev/docs/kb/monorepo-vs-polyrepo). Sources accessed 2026-11-07. The Nx comparisons are product-vendor documentation, not independent productivity evidence.
- Existing research: [B1 code-organization](batch-1-code-organization.md), [B4 archetypes](batch-4-project-archetypes.md), [B5 architecture maturity](batch-5-maturity-evolution.md). No application was supplied for empirical evaluation.

## Deduplication decision
Keep existing broad `feature-first-folders`, `modularity` and framework archetype IDs intact. Promote `project-structure-selection` to a scoped *selector* pointing to them. Add five narrowly scoped canonical decision topics rather than duplicating each archetype or claiming a mandatory layout:
1. `vertical-slice-architecture`: unit of feature-change ownership, not a mandatory mediator framework.
2. `package-by-feature-vs-layer`: compare layout axis and framework constraints.
3. `module-public-contracts`: consumer-facing API and ownership policy.
4. `architecture-dependency-rules`: explicit enforceable dependency graph.
5. `monorepo-vs-multirepo`: repository governance distinct from deployability.

## Structure-selection decision matrix (inferred candidates, not platform mandates)

| Context | No-change candidate | When to evaluate a different boundary | Validation required |
| --- | --- | --- | --- |
| Prototype UI or API | Single framework-native project, basic behavior tests | Repeated cross-folder feature changes or multiple owners | Navigation task, route/runtime discovery, build/test |
| MVP with Functions/WebJobs | Keep trigger/job entrypoints per runtime, focused feature modules | Independent scheduling, retries, deployment or operational requirements | Trigger/schedule/DI registration and integration behavior |
| Growing UI/API/workers/libraries | Cohesive internal modules and stable entrypoints inside one repo | Proven shared business behavior, contract consumers, independent release need | Dependency graph, public API and version compatibility, CI impacts |
| Enterprise / multiple teams | Explicit ownership/contract rules in one or several repositories | Regulatory access control, independent lifecycles, repository/CI governance | Threat/access constraints, build/release cadence, cross-repo migration costs |

Important: `prototype`, `MVP`, `growth`, `enterprise` describe context; they do **not** require specific folder depth, number of repos or microservices.

## Example navigation experiment (not executed)
1. Choose two real changes (e.g. add Order cancellation; fix a scheduled invoice job) and identify entrypoint -> domain decision -> storage/integration -> tests.
2. Baseline time to first relevant file, unique files opened, cross-directory hops, files edited per change, import cycles and CI runtime. Exclude generated code from maintained LOC.
3. Compare retaining current organization, one feature-first relocation and one explicit module public API. No new shared library without at least one stable cross-feature responsibility and real consumers.
4. Run route/trigger discovery, builds, unit/integration/contract tests and security checks for actual target runtime; record before/after data; restore original layout if behavior, discoverability or ownership worsens.

## Outputs
- Upgraded [project structure selection](../concepts/code-organization/project-structure-selection.md) from research stub to scoped reviewed decision framework.
- Added [vertical slices](../concepts/code-organization/vertical-slice-architecture.md), [feature vs layer](../concepts/code-organization/package-by-feature-vs-layer.md), [module contracts](../concepts/code-organization/module-public-contracts.md), [dependency rules](../concepts/code-organization/architecture-dependency-rules.md) and [monorepo vs multirepo](../concepts/code-organization/monorepo-vs-multirepo.md).
- Index and code-organization category navigation updated. Expected new inventory: **57 indexed, 41 reviewed, 16 stubs**.

## Open limitations and acceptance
All six pages contain scoped references, applicability, no-change option, trade-offs, counterexamples, verification and rollback. The source material establishes *candidate methods and framework/tool constraints*, not proven performance, security, maintainability or reduced code for a real application.

Validation results are tracked in the campaign report. Independent manual review of every citation's exact source-claim mapping and empirical target-app validation remain future tasks. Do not report Sonar compliance from catalog-only work.
