# B4 — Application-type file-structure archetypes

**Batch:** B4 · **Gaps:** GAP-13 (project type), GAP-12 (runtime-specific examples)  
**Research:** 2026-11-07 · **Status:** Six scoped example concepts reviewed; no real application benchmark or cross-stack universal recommendations.

## Context gathered before filling gaps

The catalog's existing `project-structure-selection` was deliberately a stub because UI, API, Functions, WebJobs, libraries and multi-project layouts must be assessed against runtime conventions and real developer navigation. B1 provides an evaluation method; B2 distinguishes logical module and deployment boundaries; B3 describes security/contracts. No real target application tree, framework lockfile, CI artifact, developer journey or build/test output was supplied. Therefore examples below are **illustrations**, not approved refactoring plans.

## Source survey and applicability

| Target type | Reviewed authoritative source | Observed supported constraint | Not proven |
| --- | --- | --- | --- |
| UI — Next.js App Router | [Next.js project structure](https://nextjs.org/docs/app/getting-started/project-structure); [route groups](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups) | Next.js uses file-based routing; route groups enable organization without a URL segment and can collide | That Next.js structure works for all UI frameworks |
| API — ASP.NET Core Minimal APIs | [Microsoft route handlers](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/route-handlers?view=aspnetcore-9.0) | `MapGroup` shares prefix and metadata/authorization policy | That grouping necessarily reduces application LOC |
| Functions — .NET isolated worker | [Microsoft isolated worker guide](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide) | Functions project requires supported .NET entrypoint, host and package configuration; local settings are local | That one Function should equal one project |
| WebJobs — App Service | [WebJobs operation guide](https://learn.microsoft.com/en-us/azure/app-service/webjobs-create); [SDK tutorial](https://learn.microsoft.com/en-us/azure/app-service/webjobs-sdk-get-started) | Continuous and triggered jobs differ in scheduling, deployment and scale behavior | That WebJobs are always preferable to Functions or separate workers |
| Libraries — Python, .NET | [PyPA src vs flat](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/); [.NET NuGet](https://learn.microsoft.com/en-us/dotnet/standard/library-guidance/nuget) | Python `src` layout changes import behavior; .NET libraries have packaging metadata | That separate packages improve reuse before consumer evidence |
| Multi-project solutions | [Microsoft architecture guide](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures); [Functions isolated worker](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide); [WebJobs overview](https://learn.microsoft.com/en-us/azure/app-service/overview-webjobs) | Internal modules can coexist with one deployment; independent runtimes have different build/host concerns | That enterprise always needs more projects or microservices |

All sources consulted 2026-11-07. Versions and hosting modes are explicit in each canonical page. Not every runtime is covered; mobile/desktop UI and Java/Scala/JS/TS/Python backend implementation variations remain an open GAP-12 extension.

## Newly curated canonical archetypes

- [UI project structure](../concepts/code-organization/ui-project-structure.md)
- [API endpoint structure](../concepts/code-organization/api-project-structure.md)
- [Functions structure](../concepts/code-organization/functions-project-structure.md)
- [WebJobs structure](../concepts/code-organization/webjobs-project-structure.md)
- [Library/package structure](../concepts/code-organization/libraries-project-structure.md)
- [Multi-project structure](../concepts/code-organization/multi-project-structure.md)

Each includes a scoped source, **illustrative** tree, simpler/no-change alternative, trade-offs, testing and rollback. Every page can be retrieved by a stable canonical ID from `catalog/index.json`; the original cross-cutting `project-structure-selection` remains a **stub** until B5's maturity axis and a real application analysis.

## Architecture decision matrix

| Type | Start with | Extract only if | Verify before merging |
| --- | --- | --- | --- |
| UI | Framework route conventions and cohesive local components | Stable shared UI with real consumers or an observed feature-navigation burden | Routing/layout tree, tests, build, client/server module boundaries |
| API | Simple, navigable endpoints in one deployable | Shared endpoint policies or meaningful capability ownership justify grouping | Route registration, auth, schemas, integration tests |
| Functions | One supported host project and focused trigger handlers | Separate deployment/runtime limits or ownership demands | Discovery, bindings, secrets, scale, retry/duplicate tests |
| WebJobs | Small job/worker with explicit schedule and operational owner | Job release, schedule, scale or isolation differs materially | Trigger mode, Always On, deployment artifact, concurrency |
| Libraries | Local shared module with clear consumers | Stable public API and independent version/release lifecycle | Packaged artifact import, contract compatibility, dependency lock |
| Multi-project | Fewest deployables consistent with actual release needs | Independently owned/scaled services or enforceable build boundaries | Dependency graph, versioned contracts, CI/runtime deployment, rollback |

**Inferred recommendation:** avoid project count as a proxy for maturity. Reuse is valuable only where semantics and change ownership are genuinely shared. A project-structure improvement is a hypothesis until before/after navigation and correctness checks run.

## Developer-navigation evaluation template

Record project type; maturity (prototype, MVP, growth, enterprise); runtime/framework/version; entrypoints and deployment topology; paths and feature ownership; two real representative tickets; dependency graph and public contracts. Compare no change, minimal relocation and modular extraction against:
1. Time and number of path/file hops required to find feature behavior.
2. Files touched per small change and accidental duplication.
3. Net **maintained** LOC excluding generated files; interfaces/wrappers added versus removed.
4. Cyclic project references and build/deployment/test duration.
5. Contract correctness, security, retries, monitoring, release and rollback costs.

Prefer reversible changes, intact framework conventions and a recorded rationale when the current structure already serves developers well.

## Remaining gaps and completion assessment

**B4 partially curated:** Six framework-scoped archetypes have sources, counterexamples and verification criteria. No actual application was restructured or measured. The **prototype/MVP/growth/enterprise** dimension is intentionally B5 and not a claim in these pages. Work remains for desktop/mobile UI, other API and serverless platforms, CI examples for actual stacks, and project-specific tests.

## Agent retrieval

Example:
```sh
python scripts/search_catalog.py "azure functions project structure" --json
python scripts/search_catalog.py "webjobs scheduled worker organization" --json
python scripts/search_catalog.py "python library src layout" --json
python scripts/search_catalog.py "multi project API UI deployables" --json
```
Read the top matching article and its sources, then follow `project-structure-selection` for the cross-type gaps. Never claim a file tree is verified against a target app without inspecting and testing it.
