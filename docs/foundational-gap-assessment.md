# Foundational architecture knowledge-gap assessment

**Assessment date:** 2026-11-07  
**Scope:** Software-Architecture-Atlas itself (not an external application).  
**Evidence classification:** **Observed** for repository inventory and metadata; **inferred** for priority and proposed research sequence; **unknown** for effectiveness of any architecture guidance until independently researched.

## Baseline and methodology

Inspected `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `catalog/index.json`, `catalog/taxonomy.json`, `docs/coverage.md`, `docs/evidence-policy.md`, `docs/curation-workflow.md`, `templates/gap-request.md`, `scripts/validate_catalog.py`, and a representative concept page (`concepts/distributed-systems/consistency.md`).

**Observed:** The index has 30 concepts across 11 categories. All 30 are `stub`, each with `source_count: 0` and `reviewed_at: null`. The sample page expressly disclaims verified guidance. This means a listed topic is discoverable but **not evidence-backed coverage**. The documented backlog already mentions API versioning, security architecture, threat modeling, tenancy, deployment topology and language-specific standards; the matrix below expands and prioritizes that backlog.

**Limitations:** This is an inventory/metadata review, **not** a technical quality evaluation of production code. No external application, build, runtime measurements, security tests, Sonar scan, or primary-source literature review was performed. Absence here means no dedicated canonical indexed concept; it does not prove the subject is never mentioned in prose.

## Priority rubric

- **P0 / foundational blocker:** Needed to make architecture decisions responsibly, or to prevent incorrect/security-sensitive recommendations.
- **P1 / next foundation:** Common decision that connects multiple existing concepts, with significant correctness or operational implications.
- **P2 / specialized extension:** Important but depends on technology, domain, system scale or runtime.

Priority is **inferred**, not a measured risk score. Promote only with project-specific evidence.

## Curated gap register

Each entry follows the gap-request fields: gap type, proposed ID/category, evidence, impact, related coverage, research path, and acceptance criteria. Candidate sources are research leads, **not already-reviewed citations**.

### GAP-01 — Evidence-backed core concepts
- **Priority/type:** P0 / stub (catalog-wide).
- **Evidence:** `catalog/index.json` has 30 `stub` records with zero sources and null review dates; `docs/coverage.md` explicitly calls all 30 research stubs.
- **Impact/question:** How can the Atlas safely provide architectural advice when the indexed guidance has not been substantiated?
- **Existing coverage:** All 30 canonical IDs; start with `modularity`, `separation-of-concerns`, `transactions`, `testing-strategy`, `resilience`, `decision-records`.
- **Research leads:** Official language/framework documentation relevant to each claim; original standards and research; documented counterexamples.
- **Acceptance:** Promote **one concept at a time**, with primary-source links, applicability/version, concrete decision questions, trade-offs, failure cases, example/counterexample, verification, revisit trigger, `reviewed_at` and matching `source_count`; run validator. Do not promote in bulk.
- **Owner/revisit:** Unassigned curator; revisit on new evidence or relevant runtime/standard change.

### GAP-02 — Architectural drivers and quality-attribute trade-offs
- **Priority/type:** P0 / absent.
- **Proposed ID/category:** `architecture-drivers` / `governance`.
- **Evidence:** No matching canonical ID in `catalog/index.json`; `decision-records` is a stub and addresses recording decisions, not eliciting drivers.
- **Impact/question:** How should functional requirements, availability, performance, security, cost, team constraints and measurable quality scenarios determine design?
- **Related:** `decision-records`, `scalability`, `resilience`.
- **Research leads:** ISO/IEC 25010 (check edition and licensed access); SEI quality-attribute scenario and architecture-evaluation materials.
- **Acceptance:** Define measurable scenarios, constraints and trade-off records; worked example comparing no-change, modular monolith and distributed alternatives; reviewable sources, applicability and counterexamples.
- **Owner/revisit:** Unassigned curator; revisit when quality targets or operating context change.

### GAP-03 — Threat modeling and security boundaries
- **Priority/type:** P0 / absent.
- **Proposed ID/category:** `threat-modeling` / `governance` (initial placement; consider a dedicated security category only if multiple vetted entries justify it).
- **Evidence:** No canonical security/threat-model concept in the index; `supply-chain` covers a narrower dependency risk.
- **Impact/question:** How are trust boundaries, assets, misuse cases, authentication/authorization and mitigations identified before architecture selection?
- **Related:** `supply-chain`, `dependency-inversion`, `decision-records`.
- **Research leads:** OWASP Threat Modeling Cheat Sheet, OWASP ASVS, NIST SSDF; check source versions.
- **Acceptance:** Scope model, data-flow/trust boundaries, threat and mitigation register, least-privilege examples, verification and residual-risk ownership; distinguish principles from context-specific controls.
- **Owner/revisit:** Unassigned curator; revisit with threat landscape/system-boundary changes.

### GAP-04 — API contracts, compatibility and evolution
- **Priority/type:** P0 / absent.
- **Proposed ID/category:** `api-contracts` / `distributed-systems`.
- **Evidence:** `event-driven` and `queues` exist as stubs, but no dedicated API/contract/versioning ID in index.
- **Impact/question:** How should teams define request/response contracts, error semantics, pagination, backward compatibility and breaking-change migration?
- **Related:** `event-driven`, `idempotency`, `testing-strategy`.
- **Research leads:** OpenAPI Specification; HTTP Semantics (RFC 9110); relevant provider compatibility policies.
- **Acceptance:** Synchronous vs asynchronous boundary, consumer/provider compatibility matrix, deprecation/migration example, contract-test strategy, failure and rollback options.
- **Owner/revisit:** Unassigned curator; revisit on API or protocol version changes.

### GAP-05 — Architecture styles and boundary-selection criteria
- **Priority/type:** P1 / absent.
- **Proposed ID/category:** `architecture-styles` / `governance`.
- **Evidence:** `modularity`, `bounded-contexts`, `cqrs` exist; no indexed comparative treatment of modular monolith, layered/hexagonal, service-based and microservice styles.
- **Impact/question:** What evidence warrants system distribution, additional layers or new deployable boundaries versus simpler existing organization?
- **Related:** `modularity`, `bounded-contexts`, `cqrs`, `decision-records`.
- **Research leads:** Architecture literature with case studies and firsthand migration evidence; relevant cloud architecture guidance.
- **Acceptance:** Decision matrix with constraints, operational overhead, failure modes, no-change baseline, example and anti-example; avoid a universal winning style.
- **Owner/revisit:** Unassigned curator; revisit when team scale and deployment independence change.

### GAP-06 — Data models, ownership and schema migrations
- **Priority/type:** P1 / absent.
- **Proposed ID/category:** `schema-evolution` / `data`.
- **Evidence:** `transactions` and `cqrs` are indexed; no standalone schema evolution/data ownership ID.
- **Impact/question:** How are schema compatibility, zero/low-downtime changes, data ownership and rollback managed?
- **Related:** `transactions`, `consistency`, `bounded-contexts`.
- **Research leads:** Official database vendor migration/transaction docs; relevant schema-registry compatibility docs.
- **Acceptance:** Expand/migrate/contract example, read/write compatibility and backfill safeguards, rollback limits, verification queries and operational ownership.
- **Owner/revisit:** Unassigned curator; revisit with database/version changes.

### GAP-07 — Deployment architecture and safe delivery
- **Priority/type:** P1 / absent.
- **Proposed ID/category:** `deployment-strategies` / `operations`.
- **Evidence:** Operations has only `observability` and `resilience` indexed; neither is a deployment lifecycle entry.
- **Impact/question:** How do teams choose release strategies, rollout signals, feature flags, rollbacks and environment parity?
- **Related:** `observability`, `resilience`, `testing-strategy`.
- **Research leads:** Maintained platform documentation, deployment controller docs and SRE release-engineering references.
- **Acceptance:** Compare rolling/canary/blue-green with costs; deployment topology and release gates; rollback and data-compatibility caveats; concrete measurable signals.
- **Owner/revisit:** Unassigned curator; revisit with platform/release process changes.

### GAP-08 — Reliability objectives, incident recovery and disaster readiness
- **Priority/type:** P1 / absent.
- **Proposed ID/category:** `reliability-objectives` / `operations`.
- **Evidence:** `resilience` and `observability` are stubs; no indexed SLI/SLO/error budget, RTO/RPO or recovery topic.
- **Impact/question:** What service reliability is required and how will incidents, data loss and recovery be verified?
- **Related:** `resilience`, `observability`, `transactions`.
- **Research leads:** Google SRE materials; cloud provider resilience/recovery documentation.
- **Acceptance:** User-focused SLI/SLO example, alert and error-budget policy, recovery objectives, failure drill and disaster-recovery test outline, cost/reliability trade-off.
- **Owner/revisit:** Unassigned curator; revisit after incidents or changed reliability needs.

### GAP-09 — Performance measurement and resource budgets
- **Priority/type:** P1 / stub + missing integration.
- **Proposed ID/category:** Expand `scalability` and cross-link `backpressure`, `caching`, `observability` instead of immediately creating a duplicate ID.
- **Evidence:** Relevant IDs exist but are all stubs; the index contains no vetted measurement workflow.
- **Impact/question:** How are representative workloads, p95/p99 latency, throughput, saturation and costs measured before selecting caches or scale-out?
- **Related:** `scalability`, `backpressure`, `caching`, `observability`.
- **Research leads:** Official profiling/load-testing tools for a named stack; authoritative performance engineering guidance.
- **Acceptance:** Reproducible baseline/experiment plan, workload assumptions, performance and cost budgets, failure thresholds, regression and rollback criteria.
- **Owner/revisit:** Unassigned curator; revisit when load profile or bottlenecks change.

### GAP-10 — Identity, authorization and secrets lifecycle
- **Priority/type:** P1 / absent.
- **Proposed ID/category:** `identity-and-access` / `governance` (provisional until security taxonomy decision).
- **Evidence:** No canonical authn/authz/secrets entry; `supply-chain` is not sufficient coverage.
- **Impact/question:** How are user/service identity, permissions, credential storage/rotation and audit boundaries designed and verified?
- **Related:** `threat-modeling` (proposed), `supply-chain`, `decision-records`.
- **Research leads:** NIST SP 800-63 series, OWASP ASVS, OAuth 2.0 Security Best Current Practice (RFC 9700); verify applicability.
- **Acceptance:** Least privilege and tenant-isolation considerations, authentication vs authorization separation, secrets rotation, negative tests and incident revocation path.
- **Owner/revisit:** Unassigned curator; revisit on identity provider or regulatory changes.

### GAP-11 — Operational ownership, costs and tenancy
- **Priority/type:** P2 / absent.
- **Proposed ID/category:** `operational-costs` / `operations` (multi-tenancy may merit a separate ID later).
- **Evidence:** `docs/coverage.md` lists tenancy and operational cost models in the backlog; no corresponding indexed concepts.
- **Impact/question:** Who owns runbooks, budgets, per-tenant limits and ongoing operational burden?
- **Related:** `scalability`, `observability`, `bounded-contexts`.
- **Research leads:** Cloud provider cost and tenancy guidance; internally measured operating costs for a named workload.
- **Acceptance:** Cost drivers and resource budgets with assumptions, ownership/RACI, isolation alternatives and operational verification.
- **Owner/revisit:** Unassigned curator; revisit when tenant or cost model changes.

### GAP-12 — Runtime-specific exemplars and tooling
- **Priority/type:** P2 / absent + insufficient applicability.
- **Proposed ID/category:** Prefer scoped examples attached to existing concepts before adding new IDs.
- **Evidence:** `docs/coverage.md` names C#/.NET, Java, Scala, JS/TS and Python standards, package-manager examples and Sonar mappings as backlog; current articles are broad stubs.
- **Impact/question:** Which patterns vary materially by runtime, concurrency model, framework version or analyzer configuration?
- **Related:** `async-await`, `thread-safety`, `dependency-conflicts`, `quality-gates`.
- **Research leads:** Official vendor/runtime/package manager docs; Sonar rule documentation and the **actual** project quality profile.
- **Acceptance:** Pin versions, runnable minimal examples, tests and caveats; distinguish universal guidance from stack-specific behavior and never claim a quality gate passes without a real scan.
- **Owner/revisit:** Unassigned curator; revisit on supported version or tool-rule updates.

## First curation wave (recommended, not completed)

1. **Evidence debt first:** Research and review `decision-records`, `modularity`, `transactions`, `testing-strategy` and `resilience` individually. Leave all other stubs marked as such.
2. **New foundation:** Add properly sourced concepts for `architecture-drivers`, `threat-modeling` and `api-contracts` with canonical index records, concept pages, group navigation and links.
3. **End-to-end decision examples:** Apply the curated concepts to a hypothetical small service *clearly labeled illustrative*, recording simpler/no-change alternatives, risks, experiments and rollback. Do not treat this as real target-repository evidence.
4. **Systematize prevention:** Add a catalog check against duplicate `tags` and duplicate `related` values, and cross-check `reviewed_at`, `source_count` and source sections for reviewed entries. The inspected index contains some duplicate tags/related IDs even though the current validator checks only existence of related IDs.

## Definition of done per gap

- A canonical index entry and actual page exist for newly added concepts; no duplicate IDs/paths.
- Page and index statuses match. `reviewed` requires substantive evidence links, review date and source count in both places.
- Applicable stack, versions and assumptions are stated; sources, trade-offs, counterexamples, tests and rollback are inspectable.
- Related links, category navigation and `docs/coverage.md` are updated as relevant.
- `python scripts/validate_catalog.py` passes, and the PR CI check passes.
- A curator records unresolved contradictions and revisit triggers, without conflating research proposals and verified claims.

## Repository references

- [Canonical index](../catalog/index.json)
- [Taxonomy](../catalog/taxonomy.json)
- [Coverage inventory](coverage.md)
- [Curation workflow](curation-workflow.md)
- [Evidence policy](evidence-policy.md)
- [Gap request template](../templates/gap-request.md)
- [Validator](../scripts/validate_catalog.py)

**Assessment status:** Inventory verified from the repository metadata and inspected files; topic priority and research plans inferred. No concepts were upgraded to `reviewed` by this assessment.

### GAP-13 — Application code and file-structure guidance across types and scale
- **Priority/type:** P0 for developer navigation and code-maintainability use cases / absent (now indexed as a research stub).
- **Proposed ID/category:** `project-structure-selection` / `code-organization`.
- **Evidence:** Existing indexed concepts cover feature-first folders, modularity and simplification only as stubs; there was no dedicated project type × growth stage decision framework.
- **Impact/question:** How can a repository reduce unnecessary application code, improve feature discoverability, share only proven reusable behavior, and evolve modularly without multiplying projects or layers?
- **Dimensions:** UI, API, Functions/serverless, WebJobs/worker services, libraries, multi-project solutions; prototype, MVP, growing business, enterprise.
- **Related:** `feature-first-folders`, `modularity`, `code-simplification`, `dependency-inversion`.
- **Research leads:** Official framework/project layout and build/deployment guidance for the specific runtime, maintained language docs, measured change-task case studies, source-based architecture evaluation.
- **Acceptance:** Compare no-change, framework-native, feature-first and layered variants using real path evidence; consider deployable/project boundaries; report code deletion versus added indirection, navigation time, change footprint, dependency coupling, tests, migration and rollback; include counterexamples and scoped version applicability. Do not assert that any folder layout is universally optimal.
- **Owner/revisit:** Unassigned curator; revisit with application scale, team ownership and framework upgrades.
- **Catalog reference:** [Application file and project structure selection](../concepts/code-organization/project-structure-selection.md) (**stub**, not reviewed).
