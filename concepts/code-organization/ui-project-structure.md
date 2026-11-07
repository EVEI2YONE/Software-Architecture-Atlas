---
id: ui-project-structure
title: "UI application project structure"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# UI application project structure

> **Scoped reviewed guidance.** Sources substantiate framework conventions; directory trees and decisions below are illustrative **inferences**, not measured universal improvements.

## Applicability
UI web application (Next.js App Router example). Next.js App Router (documented in 2026), not a universal UI/mobile/desktop standard.

## Framework-grounded constraints
Routing files and conventions such as page.tsx and layout.tsx have framework-defined meaning. Route groups in parentheses organize routes without adding URL segments; private folders can group colocated support code. Route group paths must not collide.

## Candidate layout (illustrative, not a runnable repository)
```text
app/
  layout.tsx
  (store)/
    orders/
      page.tsx
      _components/
        OrderList.tsx
  (admin)/
    page.tsx
lib/
  auth.ts
```

## Simpler alternative
Keep the existing small routing tree and colocate a component only when multiple edits show clear navigation friction.

## Counterexample and costs
Do not move Next.js route files into an arbitrary feature directory outside recognized route conventions or assume route groups produce a new URL prefix.

## Evaluation, migration and rollback
Gather runtime/framework versions, source/deployment tree, entrypoints, ownership and two representative feature changes before recommending a layout. Inspect route discovery, navigation and layout inheritance; run framework build and UI tests; trace client/server boundaries and check route collisions. Move one cohesive unit at a time; preserve behavior and contracts; compare file hops, files touched and net maintained LOC excluding generated code. Revert when navigation, correctness, runtime discovery or operational ownership worsens.

## Evidence limits
The cited docs support specific platform capabilities and constraints. They do not independently demonstrate shorter completion time, fewer bugs, fewer LOC, or improved maintainability for an uninspected application. No application code was changed or executed for this entry.

## Search aliases
ui project structure; ui web application (next.js app router example); application folder structure; code navigation; project files; reusable modules

## Related concepts
- [Project structure selection](project-structure-selection.md)
- [Feature first folders](feature-first-folders.md)
- [Modularity](modularity.md)
- [Code simplification](code-simplification.md)

## Sources
1. Next.js App Router project structure: https://nextjs.org/docs/app/getting-started/project-structure (consulted 2026-11-07).
2. Next.js Route Groups: https://nextjs.org/docs/app/api-reference/file-conventions/route-groups (consulted 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Reassess upon major framework/hosting version change or evidence from an application-specific navigation/reliability study.
