# Initial architecture coverage

**The original 30 topics began as research stubs.** In B1, `feature-first-folders` and `code-simplification` were promoted to scoped `reviewed` guidance with cited sources; the remaining 29 topics initially remained stubs. B2 subsequently curated `modularity`, `dependency-inversion`, and `decision-records`, bringing the catalog to **5 reviewed and 26 stubs** at that point. B3 now adds four canonical concepts and reviews two earlier stubs: **35 concepts total; 11 reviewed and 24 stubs**. Reviewed principles are not evidence of improvements in any target application.

| Category | Count | Scope |
|---|---:|---|
| [principles](../concepts/principles/README.md) | 4 | Design principles and practical trade-offs |
| [domain-design](../concepts/domain-design/README.md) | 3 | Domain-driven design and business boundaries |
| [code-organization](../concepts/code-organization/README.md) | 13 | Modularity, human navigation and code reduction |
| [dependencies](../concepts/dependencies/README.md) | 2 | Dependency resolution, third-party packages and supply chain |
| [runtime](../concepts/runtime/README.md) | 3 | Asynchrony, threading and concurrency safety |
| [distributed-systems](../concepts/distributed-systems/README.md) | 5 | Distributed communication, failure and consistency |
| [data](../concepts/data/README.md) | 3 | Data models, transactions and access patterns |
| [performance](../concepts/performance/README.md) | 2 | Caching, capacity and scalability |
| [quality](../concepts/quality/README.md) | 3 | Readability, tests, Sonar and static quality gates |
| [operations](../concepts/operations/README.md) | 2 | Resilience, observability and delivery |
| [governance](../concepts/governance/README.md) | 3 | Architecture decisions and lifecycle |

## Initial backlog beyond the scaffold
Language-specific implementation standards (C#/.NET, Java, Scala, JavaScript/TypeScript, Python), lockfile/package-manager examples, Sonar rule mapping, static complexity metrics by language, API versioning, data migration, security architecture, threat modeling, rate limiting, tenancy, resource budgets, deployment topology, integration contracts, and operational cost models. Add only when properly scoped and sourced.

See [B1 research context and findings](batch-1-code-organization.md) for source-backed file-navigation and simplification alternatives, measurement criteria and outstanding runtime-specific gaps.

## Added research gap: application code/file structure

[project-structure-selection](../concepts/code-organization/project-structure-selection.md) is a new **stub**, not reviewed guidance. It covers UI, API, Functions, WebJobs, libraries and multi-project layouts from prototype through enterprise, emphasizing navigation, net code reduction, reuse, modularity and extensibility. Validate alternatives against actual repositories and runtime conventions before recommending changes. See [GAP-13](foundational-gap-assessment.md#gap-13--application-code-and-file-structure-guidance-across-types-and-scale).

See [B2 architectural boundaries research](batch-2-architecture-boundaries.md) for scoped source review, options, quality-driver questions and open GAP-02/GAP-05 needs.

See [B3 research](batch-3-security-contracts-data.md) for new contract, security, identity and migration guidance and explicit unresolved application risks.

## B4 application archetype curation

Six platform-scoped `code-organization` concepts were added as reviewed guidance: UI (Next.js), API (ASP.NET Core Minimal APIs), Functions (.NET isolated worker), WebJobs (App Service), libraries (Python/.NET), and multi-project solutions. The current canonical index contains **41 concepts, 17 reviewed, 24 stubs**. Their directory trees are **illustrative** and no project-specific reduction in code or navigation time has been measured. See [B4 research](batch-4-project-archetypes.md).

## B5 evolution and maturity research

Two additional scoped source-backed concepts were indexed: `architecture-evolution` and `incremental-boundary-migration`. The current catalog has **43 concepts: 19 reviewed, 24 stubs**. Growth-stage guidance is explicitly *inferred*, not a mandate that project or enterprise size requires microservices. See [B5 research](batch-5-maturity-evolution.md).
