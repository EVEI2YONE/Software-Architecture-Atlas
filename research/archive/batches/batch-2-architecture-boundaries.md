# B2 — Architectural drivers and boundaries research

**Batch:** B2; **gaps:** GAP-02, GAP-05, GAP-01  
**Research date:** 2026-11-07  
**Outcome:** Scoped concepts curated and comparative decision method documented. **No application-specific architecture evaluated or changed.**

## Context gathered

The Atlas catalog had stubs for module boundaries, dependency inversion, ADRs, bounded contexts and separation of concerns. B1 added scoped guidance for feature grouping and simplification but did not measure an actual application. The Atlas is a knowledge repository; no target system, business drivers, workload data, team/deployment arrangements or runtime constraints were supplied. Thus *which architecture to choose for a real application remains unknown*.

## Checked primary and original research sources

- Microsoft Learn, *Common web application architectures*: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures — logical vs physical separation, monolithic project/solution, layers, Clean Architecture and deployment trade-offs. Reviewed 2026-11-07.
- Microsoft Learn, *Dependency injection guidelines*: https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection-guidelines — service locator avoidance and lifecycle pitfalls. Reviewed 2026-11-07.
- AWS Prescriptive Guidance, *Decompose by subdomain*: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/decompose-subdomain.html — business-domain split, with explicit risk of excess services. Reviewed 2026-11-07.
- AWS Prescriptive Guidance, *Architectural decision record process*: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html — decisions, context, consequences and review lifecycle. Reviewed 2026-11-07.
- Martin Fowler, *Architecture Decision Record* (2026-03-24): https://martinfowler.com/bliki/ArchitectureDecisionRecord.html — alternatives, confidence and superseding decisions. Reviewed 2026-11-07.
- Martin Fowler, *Monolith First* (2015-06-03): https://martinfowler.com/bliki/MonolithFirst.html — experience-based argument for considering the operational cost of distribution. Compare with Stefan Tilkov, *Don't start with a monolith* (2015-06-09): https://www.martinfowler.com/articles/dont-start-monolith.html — explicitly competing view. Neither provides a universal rule.

## Architecture drivers: collect before choosing a boundary

For an application review, ask for:
1. Critical user journeys, failure impact, domain vocabulary and integrity constraints.
2. **Quality scenarios**, not just adjectives: e.g., "under a stated peak workload, 95% of requests complete within a specified latency" or "a team can independently release a feature without redeploying unrelated functionality".
3. Security boundaries, data ownership, uptime/recovery objectives and compliance constraints.
4. Team size and ownership, deployment cadence, build/test duration, runtime/framework and operational skill.
5. Existing dependency graph, cyclic references, shared database usage, changing code hotspots, production traces and release incidents.

All example thresholds must come from stakeholder objectives or real measurements; do not fabricate metrics.

## Candidate styles and falsifiable decision matrix

| Candidate | Trigger to investigate | Main benefit sought | Primary downside | Simpler/no-change comparison |
| --- | --- | --- | --- | --- |
| Keep single project | Small coherent app and few navigation issues | Lowest overhead | Weak enforced boundaries as complexity grows | Baseline |
| Feature or domain folders inside one deployment | Changes span distant technical folders | Developer navigation and ownership | Framework conventions can constrain moves | Rename/move just one feature |
| Multiple internal modules/projects, one deployable | Cycles or unclear dependency direction; stable domain seams | Compile-time dependency rules, cohesion | Extra project references and composition | Logical modules within same project |
| Layered/ports-adapters layout | Core behavior must be insulated from replaceable infrastructure | Test seams and dependency control | Interfaces, indirection and boilerplate | Direct calls where stable and harmless |
| Independently deployed services | Demonstrated autonomous release/scale needs plus operational readiness | Isolated release/scaling/failure domains | Network failures, contracts, data consistency, on-call costs | Modular monolith or worker boundary |

**No winner is implied**; weigh actual business and engineering constraints. Distribution is not inherently modularity, and enterprise size does not automatically require separate deployables.

## Worked hypothetical decision

A growing commerce API has Orders and Billing features in one deployment. Both are edited frequently, but there is no demonstrated need for independent release or scaling. Option 1: keep current structure. Option 2: group Orders and Billing into internal modules and prevent circular references. Option 3: extract services. **Provisional experiment:** test option 2 first, preserve public behavior, compare feature change paths, dependency cycles and integration tests. Reject the change if it adds overhead without measurable improvement. Option 3 requires separate evidence of deployment autonomy and willingness to own network/reliability overhead. This is an illustration, **not observed system evidence**.

## Evidence/verification checklist

- **Observed:** repository tree, dependency direction, deployment boundaries, logs, tests, actual timing data.
- **Supported:** the cited sources and their stated applicability; do not extend .NET-specific DI rules uncritically to every runtime.
- **Inferred:** boundary candidates, expected navigation improvements and whether an interface is useful.
- **Unknown:** real target value, exact cut lines, LOC/build savings, security and recovery impacts.

Baseline a representative change task, navigation hops, touched files, dependency cycles, test/run results and release friction; run reversible small-scale changes and collect comparative evidence. Roll back if behavior, build, onboarding or operations worsen.

## B2 deliverables and residual gaps

**Curated:** [modularity](../concepts/code-organization/modularity.md), [dependency inversion](../concepts/code-organization/dependency-inversion.md), [decision records](../concepts/governance/decision-records.md). These are individually sourced, scoped guidance pages.

**Still open:** GAP-02 (`architecture-drivers` dedicated canonical concept), GAP-05 (`architecture-styles` dedicated canonical concept); `bounded-contexts`, `separation-of-concerns`, `solid` and `aggregates` remain research stubs. The decision framework in this report is **provisional** pending dedicated primary-source comparison and project-specific examples. Batch state is **partially curated**, not complete.

## Agent-oriented task contract

Given a request to "split this codebase", an agent must retrieve `modularity`, `dependency-inversion`, `decision-records`, `project-structure-selection`, inspect evidence, preserve unknowns, consider no-change, then supply options/trade-offs/tests/rollback, citing exact paths. Never treat a stub as verified evidence or claim automatic microservice recommendations.
