---
id: modularity
title: "Module boundaries and cohesion"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Module boundaries and cohesion

> **Reviewed: scoped architecture principles.** Sources support logical separation and documented trade-offs, not a universal ideal module count. No application-specific measurements were performed.

## Problem and applicability
A module groups behavior with coherent ownership and limits unwanted coupling. A module need not equal a package, project, process, deployable, or team. Microsoft's ASP.NET Core architecture guide distinguishes logical *layers* from physical *tiers*, and notes that a single-deployment monolith can maintain internal layers or libraries [1].

Use this approach when features change together, responsibility is unclear, or dependencies create recurring change friction. Check platform conventions and business ownership before moving code.

## Decision options

| Option | Suitable evidence | Cost or counterexample |
| --- | --- | --- |
| Keep current folders and one project | Low navigation friction, easy tests/releases | Boundary rules can be informal |
| Cohesive modules inside one deployable | Features have distinct reasons to change | APIs and dependencies still need discipline |
| Multi-project modular monolith | Compile-time project references enforce valuable boundaries | More build artifacts and interfaces, even with one deployment |
| Separate deployables | Independent release/scale/ownership outweigh communication overhead | Network failures, data contracts, deployment coordination and operations |

AWS's subdomain decomposition guidance offers a domain-based candidate when boundaries are already understood; it warns that excessive services create discovery/integration difficulty [2]. Treat it as an option rather than a mandate.

## Heuristic (inference, validate locally)
Prefer boundaries where internal changes remain inside a feature and cross-boundary calls are explicit. Do not extract a project solely because a directory or class is large. Avoid central `Common` packages that accumulate unrelated dependencies. Preserve convenient co-location for a small codebase.

## Illustrative comparison

```text
# One deployable with internal boundaries
src/
  orders/
    order_service.*
    order_rules.*
  billing/
    billing_service.*
    billing_rules.*
  app.*

# Later, only if justified:
apps/api/                  # entrypoint / deployment
modules/orders/            # bounded public interface
modules/billing/
```

These are examples, not framework-specific templates.

## Evidence, experiments and rollback
Capture actual project tree, dependency graph, import cycles, files touched per representative change, team ownership, release cadence and build/test costs. Compare **no change** with one reversible module boundary; run all relevant tests and verify imports, public APIs and runtime composition. If extracting increases cross-boundary hopping or breaks integration, revert. Do not claim LOC savings without measurement.

## Search aliases
module boundaries; cohesion; coupling; modular monolith; shared libraries; project split; multi project architecture

## Related concepts
- [separation of concerns](../principles/separation-of-concerns.md)
- [dependency inversion](dependency-inversion.md)
- [feature first folders](feature-first-folders.md)
- [project structure selection](project-structure-selection.md)

## Evidence and sources
1. Microsoft Learn, *Common web application architectures*, https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07). Applicability: .NET web application architecture; direct support for logical layering, single-project and multi-project trade-offs.
2. AWS Prescriptive Guidance, *Decompose by subdomain*, https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/decompose-subdomain.html (accessed 2026-11-07). Applicability: assessing subdomain-oriented decomposition of an existing monolith; warns about over-fragmentation.

## Maintenance
Reviewed: 2026-11-07. Revisit after changed release ownership, boundaries, tooling or measured developer friction.
