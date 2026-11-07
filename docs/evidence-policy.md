# Evidence quality and claims

## Levels
- **Observed:** target repository config/code, test output or measured runtime evidence, with paths or logs.
- **Supported:** cited primary documentation/standards/research with explicit applicability.
- **Inferred:** reasoned risk or design hypothesis; state assumptions.
- **Unknown:** missing measurements, unclear project context or an uncited stub.

## Research source order
Prefer maintained official language/runtime/framework documentation, original research and standards, then established engineering references. Community articles are supplementary; record conflicting evidence and dates. Do not fabricate citations or claim static analysis was run when it was not.

## Required reviewed-page content
Sources with URLs/titles/accessed or published dates where feasible, constraints/versions, trade-offs, counterexamples, failure modes, verification and revisit triggers. Distinguish Sonar rule definitions from organization-specific rule sets and gate thresholds.

## Automated evidence-integrity checks (B0)

`python scripts/validate_catalog.py` now verifies duplicate tags/related IDs, self-relations, frontmatter/index review-date agreement, valid reviewed dates, stub/source consistency, and `source_count` against numbered URL references under `## Evidence and sources` or `## Sources`. This is a **metadata consistency check**, not a manual review of claim-to-source support or source freshness. See [B0 audit](batch-0-catalog-integrity.md). Reviewed entries remain `requires-source-inspection` for agents.
