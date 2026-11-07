---
id: knowledge-index-validation
title: "Knowledge index validation and evidence integrity"
category: governance
status: reviewed
reviewed_at: 2026-11-07
---

# Knowledge index validation and evidence integrity

> **Scoped research guidance, not target-repository verification.** Source-backed platform behavior, inferred trade-offs and missing project-specific evidence are distinct. A reviewed catalog page always requires source inspection.

## Problem and context
An agent sees a reviewed record with a broken local link or stale citation and assumes its claim was verified.

## Applicability and decision
Treat catalog/index.json and Markdown frontmatter as a versioned contract. Validate unique IDs, canonical paths, taxonomy, statuses, dates, related IDs and numbered source counts; separately audit claim-to-source relevance, link availability, version scope and contradictory guidance.

### Simpler/no-change option
For a small catalog, a stdlib metadata validator plus human review is sufficient. Avoid automatically promoting reviewed status based on a URL count or introducing a hosted vector database by default.

### Failure modes and counterexamples
Passing metadata checks does not prove a citation supports a claim. A live link may have changed content, and a page's review date cannot stand in for actual re-validation of its sources.

## Illustrative example (not an inspected application)
The validator confirms source_count=2 and existing local links; the curator then manually checks both primary sources for the page's version-specific claims and records evidence as supported, inferred or unknown.

## Validation, migration and rollback
Run scripts/validate_catalog.py and unit tests; insert controlled duplicate ID, nonexistent related ID and source-count mismatch into fixtures to prove failures. Review sampled claim/source pairs manually; record unresolved assertions rather than silently changing statuses. Preserve original application behavior and compare against no-change. Verify framework/runtime/build-tool version and platform conventions; use a small reversible change before broad reorganization. Never assert measured code reduction, security, developer navigation or quality-gate success without a target application's results.

## Search aliases
knowledge index validation; knowledge index validation and evidence integrity; catalog; schema; validation; citations; evidence; source applicability

## Related concepts
- [retrieval-evaluation](../governance/retrieval-evaluation.md)
- [decision-records](../governance/decision-records.md)
- [testing-strategy](../quality/testing-strategy.md)

## Evidence scope and uncertainty

The GitHub CODEOWNERS and Python unittest references demonstrate ownership and testing tooling, respectively; neither independently establishes that this catalog's technical claims are correct or citations are relevant. A manual claim-to-source audit remains necessary.

## Evidence and sources
1. GitHub Docs, About code owners: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners (accessed 2026-11-07). Scope: the named platform, documentation workflow or evaluation approach, not a benchmark of this catalog.
2. Python Standard Library, unittest: https://docs.python.org/3/library/unittest.html (accessed 2026-11-07). Scope: the named platform, documentation workflow or evaluation approach, not a benchmark of this catalog.

## Maintenance
Reviewed 2026-11-07. Revisit on policy/tool/version changes, contradictory sources or observed application behavior. Independent detailed claim-to-source and project-specific audits remain open.
