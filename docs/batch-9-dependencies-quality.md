# B9 — Dependency management, code simplification and quality gates

**Date:** 2026-11-07. **Campaign branch:** `curation/b7-b14-knowledge-gaps-20261107`; **shared draft PR:** #3. **Evidence boundary:** catalog research, not an assessed application.

## Context gathered before changes
The B8 branch contained 57 canonical entries: 41 reviewed, 16 stubs. The five B9 existing concepts (`dependency-conflicts`, `supply-chain`, `cognitive-complexity`, `quality-gates`, `testing-strategy`) were all stubs. Existing reviewed neighbors included `code-simplification`, `dependency-inversion`, `architecture-dependency-rules`, `module-public-contracts`, and `api-contracts`. No source application, Sonar scan, actual package graph or target CI logs was provided.

Research investigated official NuGet dependency resolution, Central Package Management and lockfile behavior; npm peer dependencies and `npm ci`; GitHub dependency review; SonarQube Server quality gates, security issue classifications and code metrics; Microsoft testing guidance; Nx module boundaries. All cited URLs are listed on individual concept pages; researched 2026-11-07. The documentation establishes tool-specific behavior, **not** measured application improvements or scan compliance.

## Deduplication and scope
- Keep `dependency-conflicts` as the operational diagnosis/decision hub. Give `transitive-dependency-resolution` resolver rules and `package-locking-and-version-policy` reproducible-build policy.
- Keep `supply-chain` distinct from simple version compatibility and relate it to vulnerability and provenance reviews.
- Reuse the existing `architecture-dependency-rules` for import-rule enforcement. `cyclic-dependency-prevention` adds graph diagnosis and cycle-breaking; do not introduce another generic module boundary concept.
- Reuse `code-simplification` while adding `dead-code-and-dependency-removal` for removal evidence and consumer verification.
- Separate **Sonar quality gate** (configured acceptance condition), **quality profile** (activated rules), and **cognitive complexity** (metric/signal). A Security Hotspot is not automatically a confirmed vulnerability.
- Separate mutation testing of assertion sensitivity from contract testing of consumer/provider compatibility and broader architecture-focused test selection.
- Treat fitness functions as targeted, executable invariants—not generic requirements that every codebase must create a custom validation framework.

## Example evidence-to-action matrix (illustrative)
| Observation | Verify before deciding | Smallest alternative | Required gate |
| --- | --- | --- | --- |
| NuGet restore reports dependency downgrade | Framework/SDK versions, direct and resolved graph, lockfile, exact NU error | Align one compatible dependency; remove unused package | Clean restore, build, affected runtime tests |
| npm peer constraint conflict | package.json, lockfile, npm version and flags | Adjust compatible peer or consumer release | `npm ci` with matching project config; integration tests |
| Suspected dead package | Runtime registration, reflection, tests, scripts, external clients | Remove one leaf dependency | Clean install, build, smoke tests and rollback |
| Cognitive complexity finding | Actual analyzer rule, language, behavior and test paths | Clarify guards or preserve cohesive code | Tests, reviewer navigation assessment, measured metric |
| Sonar gate reported green without run | Product/edition, profile, rule keys, baseline and scan ID | State 'unknown', run configured analysis | Actual gate result; no invented pass |
| Contract drift or escaping test failures | Provider/consumer assumptions and integration behavior | One regression and provider contract check | Negative/integration/provider tests |
| Recurring forbidden import | Module ownership and actual dependency graph | Build/project rules or focused lint check | Deliberate failing fixture and stable CI |

## Files curated
**Upgraded from stub (5):** `dependency-conflicts`, `supply-chain`, `cognitive-complexity`, `quality-gates`, `testing-strategy`.

**New scoped concepts (7):** `transitive-dependency-resolution`, `package-locking-and-version-policy`, `cyclic-dependency-prevention`, `dead-code-and-dependency-removal`, `sonar-rules-and-quality-profiles`, `mutation-and-contract-testing`, `architecture-fitness-functions`.

Index and category navigation updated. Branch inventory after curation: **64 indexed, 53 reviewed, 11 stubs**.

## Validation and outstanding work
Validate `catalog/index.json`, all internal links and consistent frontmatter, `source_count` metadata and 12 B9 canonical ID searches. Update the golden retrieval case for `dependency hell` after promotion. Keep a different real stub (`caching`) as a negative retrieval-evidence example. Run `python scripts/validate_catalog.py` and `python -m unittest discover -s tests -v` in GitHub Actions; record the actual run outcome in the campaign tracker.

No production target was inspected: no observed dependency conflict remediation, line reduction, test coverage improvement or Sonar quality gate status is claimed. Product-specific docs need revisiting as vendor versions change; independent source-to-claim assessment remains outstanding.
