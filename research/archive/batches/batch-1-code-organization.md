# B1 — Research context, findings and application assessment

**Batch:** B1 — Code footprint and navigation  
**Date:** 2026-11-07  
**Gaps:** GAP-13 (project structure) and GAP-01 (evidence debt)  
**Status:** Research and scoped concept curation completed; **target-repository measurement remains open**. All directory examples are illustrative; no application repository was supplied.

## Context gathered before curation

The Atlas is a knowledge repository, not a UI/API/Functions/WebJobs application. It indexes 31 concept topics; before this batch, the relevant pages `feature-first-folders`, `code-simplification`, `modularity`, `dependency-inversion`, `dry-vs-abstraction`, and `project-structure-selection` were research stubs. The Atlas is designed for index-first agent retrieval, with `source_count`, `status` and `reviewed_at` governing trust. No actual developer navigation task, source tree of a target application, tests or LOC reduction exists to observe.

**Source review (accessed 2026-11-07):**
- Microsoft's ASP.NET Core guide explicitly discusses feature folders as an alternative to type-based folder structures when navigation becomes difficult: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/develop-asp-net-core-mvc-apps
- ASP.NET Core Areas support grouping related controllers and views while retaining platform conventions: https://learn.microsoft.com/en-us/aspnet/core/mvc/controllers/areas?view=aspnetcore-10.0
- React's official guide explains cohesive component hierarchies and responsibility: https://react.dev/learn/thinking-in-react (no asserted React filesystem mandate)
- Fowler's refactoring catalog lists Inline/Extract/Move/Remove Dead Code techniques: https://refactoring.com/catalog/
- Fowler's YAGNI essay argues against speculative capability and abstraction, while distinguishing refactoring that improves adaptability: https://martinfowler.com/bliki/Yagni.html

**Boundaries:** The references support only scoped methods and concrete alternatives; they do not provide controlled comparisons demonstrating that one directory style universally reduces LOC or feature implementation time. Runtime-specific project templates remain B4/B5 research, not B1 proof.

## Decision framework for an application assessment

| Observation | Smallest candidate action | Counterexample / no-change condition | Validation |
| --- | --- | --- | --- |
| Developer repeatedly opens distant type folders for one feature | Colocate one feature's handlers, models and tests where framework supports it | Framework routing/discovery requires current locations, or navigation is already quick | Record file hops, route/build tests and review with another developer |
| Pass-through service/repository layers add no policy or logic | Inline a layer or narrow the abstraction | Layer enforces auth, transactions, fault isolation, observability or test seam | Compare contracts, integration tests and dependency graph |
| Identical-looking helpers repeat | Evaluate shared behavior and change reasons before extracting | Implementations may diverge under distinct business rules | Compare change history, ownership and regression tests |
| One broad `Common`/`Utils` package serves unrelated features | Return feature-specific code to owner or define stable interfaces | Widely used, stable public APIs require shared ownership | Consumer map, versioning/build cost, compatibility test |
| Many small projects slow builds/releases | Consider merging cohesive projects and enforcing logical boundaries | Independent deployment/compliance/ownership justifies split | Measure build time, dependency edges, release coordination |
| Large file has cohesive, readable behavior | No change based on file length alone | Split only with demonstrated independent responsibilities | Representative change task and reviewer comprehension |

## Repeatable assessment template

1. **Context:** project type (UI, API, Functions, WebJobs, libraries, multi-project), maturity (prototype, MVP, growing, enterprise), stack/runtime versions, release topology, team ownership and constraints.
2. **Evidence:** path tree (excluding generated code), dependency graph, entrypoints, routing/runtime conventions, two representative changes, test results.
3. **Baseline:** task completion time, visited files/folder hops, files touched, LOC excluding generated output, dependency cycles, duplicated business behavior, build/test duration and quality profile (if provided).
4. **Options:** (a) no change, (b) minimal renames/moves/deletion, (c) feature grouping within same project, (d) selective module extraction. For each: estimated work, failure modes and applicability.
5. **Trial:** isolate one feature and preserve externally observable behavior; update imports/registrations and run framework/build/test checks. Capture paired navigation exercise, with comparable task complexity.
6. **Decision:** note observations, inferences, unresolved unknowns, test coverage, source support, reviewer feedback and regression risks.
7. **Migration/rollback:** small reversible steps, avoid breaking API/storage/deployment coupling, revert if navigation worsens or contracts break.

### Illustrative directory alternatives (not prescriptions)

```text
# Example A: flat, small, easy to navigate
src/
  app.ts
  orders.ts
  customers.ts
tests/
  orders.test.ts
  customers.test.ts

# Example B: grouped by feature in one deployable
src/
  app.ts
  features/
    orders/
      handler.ts
      model.ts
      handler.test.ts
    customers/
      handler.ts
      model.ts
      handler.test.ts

# Example C: conventional type folders, may be required by framework
src/
  controllers/
  services/
  models/
tests/
```

Each can be appropriate. Do not interpret these examples as compatible with any particular framework without checking its routing/packaging rules.

## Batch outputs and outstanding evidence

**Curated as scoped reviewed concepts:**
- [Feature-first file structure](../concepts/code-organization/feature-first-folders.md): concrete platform evidence, alternatives, counterexamples, verification and migration.
- [Code reduction and readability](../concepts/code-organization/code-simplification.md): supported refactoring operations, YAGNI limitations, metrics and rollback.

**Still research stubs (deliberate):**
- [Project-structure selection](../concepts/code-organization/project-structure-selection.md): full UI/API/Functions/WebJobs/library × prototype/MVP/growth/enterprise matrix requires B4/B5 and target-specific evidence.
- [Modularity](../concepts/code-organization/modularity.md), [Dependency inversion](../concepts/code-organization/dependency-inversion.md), [DRY vs abstraction](../concepts/principles/dry-vs-abstraction.md): no source review or promotion in this batch.

**Acceptance accounting:** Source-based general methods and illustrative alternatives are documented. Numerical navigation improvement, LOC reduction and target-code safety are **unknown** pending a supplied application repository and before/after experiment. B1 is therefore **partially completed**, not experimentally validated.

## Agent retrieval evaluation

Questions to try with `python scripts/search_catalog.py "<question>" --json`:
- `feature first folders`
- `reduce code unnecessary wrappers`
- `file structure for UI API Functions WebJobs enterprise`
- `modularity code sharing`

Agents must check `status` and sources before answering, and ask for or inspect project context when preparing concrete changes. Do not pass a stub into a verified recommendation solely because its search score is high.
