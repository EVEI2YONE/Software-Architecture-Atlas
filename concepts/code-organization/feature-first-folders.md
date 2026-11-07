---
id: feature-first-folders
title: "Feature-first file structure"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Feature-first file structure

> **Status: reviewed (scoped guidance).** Evidence supports feature grouping as a *candidate* for navigation friction in some applications, not a universal folder prescription. No target application has been examined or benchmarked.

## Problem and evidence

A folder structure grouped exclusively by technical type (for example, Controllers/, Views/, Models/) can require developers to visit distant folders to change one feature. Microsoft's ASP.NET Core architecture guide explicitly identifies this navigation cost in larger applications and describes feature folders / vertical slices as an alternative [1]. ASP.NET Core Areas provide a framework-supported way to partition related MVC functionality [2]. This evidence is specific to ASP.NET Core; other runtimes may impose different routing, packaging or build constraints.

React's component guidance recommends identifying cohesive UI components by responsibility and maintaining a component hierarchy [3]. It does **not** mandate an on-disk directory structure. Inferring that feature colocation might help navigation is therefore a hypothesis to validate, not a React requirement.

## Decision questions

- Can a newcomer find all code and tests for one user-visible feature with a small number of hops?
- Which directories reflect actual ownership and reasons to change, versus framework conventions that must be retained?
- Would moving files create confusing imports, routing behavior, circular dependencies, or hidden shared utilities?
- Do multiple features genuinely share stable behavior, or only look similar today?
- Can one representative change prove a measurable improvement without changing the public behavior?

## Alternatives and trade-offs

| Option | When to consider | Costs / counterexample |
| --- | --- | --- |
| Keep framework-native folders | Small applications; tooling depends on conventions; developer navigation already easy | May scatter feature changes as the application grows |
| Group related files by feature within the existing project | Repeated cross-folder traversal; clear feature ownership | Can duplicate tiny helpers; may conflict with framework-specific discovery |
| Organize around framework-native areas/routes | Routing and tooling natively support the grouping | Framework coupling; not necessarily a shared business module |
| Create separate projects/packages | Confirmed independent ownership, consumers, lifecycle or enforceable dependencies | Extra build, release, versioning and contract work; not justified by folder count alone |

**Practical rule (inference):** Start with the smallest reversible relocation that reduces observed navigation friction; do not split a deployable solely because a folder is large.

## Illustrative, not prescribed, before/after

```text
# Type-oriented example                  # Candidate feature-oriented example
src/                                      src/
  Controllers/OrdersController.cs           Features/Orders/
  Services/OrderService.cs                    OrdersController.cs
  Models/OrderDto.cs                          OrderService.cs
  Tests/OrderTests.cs                         OrderDto.cs
                                               OrderTests.cs
```

The feature-oriented example is only valid if the target framework resolves routes and other conventions correctly. Some stacks require particular files or names in specific locations.

## Verification and migration

1. Collect a real tree, routing conventions, representative tickets, test coverage and dependency graph.
2. Record baseline: files/folders opened and traversal count for two representative tasks; touched-file set; module cycles; build and test results.
3. Compare **no change** against moving one cohesive feature *without adding layers*.
4. Move in a small commit; update imports/registrations; run tests, route discovery and builds; solicit a second developer's navigation feedback.
5. Revert the relocation if discoverability, runtime conventions or dependency direction worsens. Keep a focused ADR noting the result.

## Search aliases

feature folders; vertical slice; group by feature; folder by feature; developer navigation; feature colocation; organize by type vs feature

## Related concepts

- [modularity](modularity.md)
- [code-simplification](code-simplification.md)
- [project-structure-selection](project-structure-selection.md)

## Evidence and sources

1. Microsoft Learn, *Developing ASP.NET Core MVC apps*, "Feature organization" and "Structuring the application": https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/develop-asp-net-core-mvc-apps (accessed 2026-11-07). **Direct support:** feature folders as an alternative for navigation difficulty in larger ASP.NET Core apps, with multi-project trade-offs.
2. Microsoft Learn, *Areas in ASP.NET Core*: https://learn.microsoft.com/en-us/aspnet/core/mvc/controllers/areas?view=aspnetcore-10.0 (accessed 2026-11-07). **Direct support:** runtime-specific option for grouping related MVC functionality.
3. React documentation, *Thinking in React*: https://react.dev/learn/thinking-in-react (accessed 2026-11-07). **Direct support:** component hierarchy and separation of concerns; **does not** establish on-disk layout.

## Maintenance

- Reviewed: 2026-11-07; applicable primarily to ASP.NET Core MVC and as a comparative *method* elsewhere.
- Revisit on major framework convention changes, contradictory evidence or measured developer-navigation regressions.
