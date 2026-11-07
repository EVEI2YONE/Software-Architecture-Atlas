# Knowledge-gap research batches

**Created:** 2026-11-07  
**Status:** Proposed curation roadmap. These are research tasks, **not reviewed guidance**.  
**Source of truth:** [Foundational gap assessment](foundational-gap-assessment.md) and [canonical index](../catalog/index.json).

## Purpose

Sequence foundational architecture research into bounded, agent-friendly review units. Focus on fewer maintained lines, understandable navigation, justified reuse, modularity and extensibility, while protecting correctness and avoiding ceremonial layers or premature package splits. Do not infer that a listed solution is best for a target repository without inspecting that repository.

A **batch** is a research and verification milestone, not a release or blanket permission to promote stubs to reviewed. Work can be parallelized by independent concepts after shared evidence criteria are established. Batch numbering expresses dependency preference, not an absolute gate on all research.

## Batch summary

| Batch | Priority | Research question | Existing gaps | Dependencies | Expected deliverables |
| --- | --- | --- | --- | --- | --- |
| B0. Evidence and agent retrieval | P0 | Can agents reliably find, interpret and challenge guidance? | GAP-01; catalog metadata issues | None | Evidence checklist, retrieval benchmark, validator improvements |
| B1. Code footprint and navigation | P0 | How can code and files become simpler to find, change and reuse? | GAP-13; GAP-01 | B0 criteria | Project-structure decision framework and measured refactoring experiments |
| B2. Architectural boundaries | P0 | When are modules, layers, libraries or separate deployables justified? | GAP-02, GAP-05; GAP-01 | B0, B1 observations | Decision matrix, trade-offs, architecture driver scenarios |
| B3. Correctness, contracts and security | P0/P1 | What boundaries maintain correctness and compatibility? | GAP-03, GAP-04, GAP-06, GAP-10 | B0; B2 for boundary assumptions | Threat models, contracts, migration examples and tests |
| B4. Project-type archetypes | P1 | How should different deployable/application kinds organize code? | GAP-13 (type axis), GAP-12 | B1, B2; B3 for contracts | UI/API/Functions/WebJobs/library/multi-project comparison packs |
| B5. Maturity and multi-project growth | P1 | What triggers structural change as teams and products grow? | GAP-13 (scale axis), GAP-05, GAP-11 | B1, B2, B4 | Prototype/MVP/growth/enterprise evolution paths |
| B6. Operations and scaling | P1/P2 | How are release, runtime reliability, performance and cost evaluated? | GAP-07, GAP-08, GAP-09, GAP-11, GAP-12 | B0, B3; relevant B4/B5 examples | Measurable operational reference examples, rollbacks and ownership |

## B0 — Evidence, catalog integrity and agent retrieval

**Research:** Audit the canonical indexed entries (43 after B5, including six application-type archetypes), checking current statuses rather than assuming all are stubs; identify missing sources, duplicate tags/related IDs, outdated applicability and retrieval misses. Preserve the distinction between discoverability and verified advice.

**Deliverables:**
- Evidence rubric with source quality, technology versions, applicability, failure modes, counterexamples and review dates.
- Gold-query benchmark for `scripts/search_catalog.py`: canonical ID, natural question, alias, cross-topic query, zero-hit and misleading-hit scenarios.
- Catalog validator coverage for duplicate metadata, graph integrity, reviewed status/source consistency and broken links.
- At least two individually reviewed foundational concepts with inspectable primary sources. Suggested starting IDs: `modularity`, `decision-records`. This is a goal, not a claim of completion.

**Exit check:** Tests pass; sampled agent responses cite real source pages and never promote stubs into verified claims. Document retrieval precision or explicit failure cases rather than fabricating an accuracy percentage.

## B1 — Code reduction, file structure and developer navigation

**Execution report:** [B1 context and assessment](batch-1-code-organization.md). Two scoped concepts curated; no application-specific benchmark has been performed.

**Research:** Expand `project-structure-selection` alongside `feature-first-folders`, `code-simplification`, `modularity`, `dependency-inversion`, `dry-vs-abstraction`. Evaluate flat, framework-native, feature-first/vertical-slice, layered and modular-monolith layouts *against observed developer tasks*.

**Questions:** Which code is unnecessary? Which abstractions or cross-project helpers create more complexity than reuse? Does finding one feature require scanning unrelated folders? Would moving files reduce change footprint or merely add indirection? When does shared code deserve its own package?

**Deliverables:** A reproducible file-layout assessment checklist; sample before/after trees; guide to cohesive names, feature ownership and test colocation; low-risk change plan with rollback; decision criteria to **retain the current structure** when it is adequate.

**Metrics:** Number of files and code paths traversed to implement representative changes; net maintained LOC (not a quality target alone); files touched per feature; circular dependencies; duplication with semantics; build/test behavior; task completion time from representative users if available.

**Exit check:** Provide multiple alternative layouts with constraints/counterexamples and show how a reviewer tests navigation and maintainability changes. Do not assert that fewer files/lines inherently means better architecture.

## B2 — Architecture drivers and modular boundaries

**Execution report:** [B2 research and boundary decision matrix](batch-2-architecture-boundaries.md). Three scoped concept pages reviewed; application-specific outcome and dedicated GAP-02/GAP-05 concepts remain open.

**Research:** GAP-02 and GAP-05; examine `separation-of-concerns`, `solid`, `bounded-contexts`, `aggregates`, `decision-records`.

**Deliverables:** Measurable quality-attribute scenarios; comparison of no-change, pragmatic module boundaries, layered/ports-and-adapters, modular monolith and separate services; dependency direction and ownership rules; architectural decision record template with evidence and revisit triggers.

**Exit check:** Every recommendation states actual driver, viable simpler alternative, impact on dependencies and deployability, testing/rollback cost, and unknowns.

## B3 — Security, contracts, data integrity and migrations

**Execution report:** [B3 source review and verification matrix](batch-3-security-contracts-data.md). Four new concepts and two existing stubs curated as scoped reviewed guidance. No target application was audited.

**Research:** GAP-03, GAP-04, GAP-06, GAP-10; connect `transactions`, `idempotency`, `consistency`, `testing-strategy`, `supply-chain`.

**Deliverables:** Example trust-boundary/threat model; API/request/event contract compatibility checklist; least-privilege and secrets-lifecycle questions; expand/migrate/contract schema example; negative/contract/integration tests; safe failure and migration paths.

**Exit check:** Separate illustrative examples from verified production evidence, cite official standards/platform sources, and document version-specific security and data guarantees. Do not claim an architecture is secure solely from structure.

## B4 — Project-type file-structure archetypes

**Execution report:** [B4 platform-specific research and six indexed archetypes](batch-4-project-archetypes.md). Six framework-scoped reviewed concepts added; no real application refactor benchmark.

**Research:** Cross-check each type against **prototype/MVP** and **growing/enterprise** contexts; these are candidate layouts, not mandated templates.

| Project type | Research candidates | Critical concerns |
| --- | --- | --- |
| UI (web, mobile, desktop) | Route/feature colocation, components/state/tests and platform conventions | navigation, state ownership, design-system boundaries |
| API | Endpoint/feature slices vs controller-service-repository directories | contracts, validation, authorization, domain cohesion |
| Functions / serverless | Trigger/handler-local modules vs central function layers | cold starts, bindings, runtime constraints, idempotency |
| WebJobs / workers | Job/queue/schedule-centric organization vs shared task runners | retries, scheduling, checkpoints, observability |
| Libraries/packages | Keep internal module vs publish shared package | stable public API, versioning, ownership and consumer evidence |
| Multi-project systems | Single solution with internal modules vs separate deployables | dependency direction, release coupling, contracts and shared code |

**Deliverables:** Small, version-labeled directory trees for each project type, before/after examples, test placement, deployment boundaries, anti-patterns, framework-convention notes and explicit trade-off tables.

**Exit check:** Every archetype must include a simpler alternative and a negative case where it should not be applied. No automatic proliferation of projects or `Shared` libraries.

## B5 — Evolution by maturity and business scale

**Execution report:** [B5 research and evolution matrix](batch-5-maturity-evolution.md). Two scoped reviewed concepts added; the stage-dependent layouts are inferred and target application evidence is pending.

**Research:** GAP-13 along its scale axis, GAP-05 and GAP-11.

| Stage | Research emphasis | Avoid |
| --- | --- | --- |
| Prototype | Tight feedback, few moving parts, easy deletion and experiments | speculative plugin systems and premature package splits |
| MVP | Repeatable tests/deployment, initial feature ownership and stable boundaries | copying enterprise reference architecture |
| Growing business | Several UI/API/jobs/libraries, independent change hotspots, team and deployment seams | sharing every similar helper across projects |
| Enterprise | Multiple teams, lifecycle/versioning, policies, compliance and operational ownership | assuming enterprise requires microservices or maximum layers |

**Deliverables:** Transition triggers backed by evidence (team ownership, coupling, release coordination, build times, incidents), migration sequences with rollback, and evolving project trees. Show both growth and consolidation/removal paths.

**Exit check:** No recommendation based only on organization size labels; explicitly preserve no-change and simpler approaches.

## B6 — Deployment, reliability, performance and operations

**Research:** GAP-07, GAP-08, GAP-09, GAP-11, GAP-12; expand `observability`, `resilience`, `scalability`, `backpressure`, `caching`, `quality-gates`.

**Deliverables:** Version-scoped runtime examples; measured workload baseline, p95/p99 and resource budgets; SLI/SLO/recovery questions; release and schema-safe rollback considerations; cost and runbook ownership; static analysis guidance tied to the **actual** project quality profile.

**Exit check:** Demonstrate measurement/proposed experiments; do not claim Sonar passes, performance improvements or recovery behavior without tests and recorded results.

## Suggested research work units

For the current research campaign, use the **same branch and PR #2** for all batches, with separate, reviewable commits per concept or coherent example pack. Subsequent changes should update that PR rather than open a new PR. Use small, reviewable changes per **one concept or one coherent example pack**. Each batch update should identify `batch_id`, `gap_ids`, canonical concept IDs, source URLs and dates, status transitions, evidence classification, applicability, a simpler alternative, tests, migration and rollback. Add a link to the batch plan. Research notes can be merged as draft/stub without treating the guidance as reviewed.

### Agent retrieval and task planning

The agent should:
1. Search `catalog/index.json` (or `scripts/search_catalog.py`) for the relevant concept IDs before consulting this plan.
2. Select the smallest relevant batch and inspect its gap IDs in `docs/foundational-gap-assessment.md`.
3. Decide whether it is a **coverage gap**, **unreviewed stub**, **weak evidence**, **retrieval failure** or **application-specific unknown**.
4. For file-structure questions, always record **project type**, **growth stage**, **framework/runtime**, **deployment boundaries** and **representative developer tasks** before prescribing changes.
5. Return a proposed research/experiment plan with confidence labels and exact paths. Use only verified inputs for claims; a hypothetical tree is illustrative, not a verified target-repository recommendation.
6. Run `python scripts/validate_catalog.py` and `python -m unittest discover -s tests -v` when changing catalog or search code.

## Batch status

Every batch starts **proposed / not completed**. Completion requires reviewable artifacts and checked acceptance criteria; no automatic transition occurs because this document exists. Update this file explicitly as curation advances.

| Batch | State | Owner | Review evidence |
| --- | --- | --- | --- |
| B0 | Proposed | Unassigned | Not yet linked |
| B1 | Partially curated — 2 scoped concepts reviewed; application metrics pending | Unassigned | [B1 context and assessment](batch-1-code-organization.md) |
| B2 | Partially curated — 3 scoped concepts reviewed; target evidence pending | Unassigned | [B2 context and decision matrix](batch-2-architecture-boundaries.md) |
| B3 | Partially curated — 6 scoped concepts reviewed; application testing pending | Unassigned | [B3 context and validation matrix](batch-3-security-contracts-data.md) |
| B4 | Partially curated — 6 scoped archetypes indexed; app metrics and broader runtimes pending | Unassigned | [B4 source review and decisions](batch-4-project-archetypes.md) |
| B5 | Partially curated — 2 scoped concepts reviewed; real project metrics pending | Unassigned | [B5 maturity and evolution report](batch-5-maturity-evolution.md) |
| B6 | Proposed | Unassigned | Not yet linked |
