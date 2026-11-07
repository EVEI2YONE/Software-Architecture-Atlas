# Contributing

Use `templates/concept.md` for new concepts and add an entry to `catalog/index.json`. Keep IDs stable, kebab-case and unique; file path is `concepts/<category>/<id>.md`. Update the group README and `docs/coverage.md` if adding a category.

## Readability first
Prefer a concrete explanation of trade-offs over dogmatic rules, case studies over speculation, short headings and cross-links over monolithic documents. Distinguish runtime/language-specific guidance from general principles.

## Status lifecycle
`stub` (intent only) → `draft` (research in progress) → `reviewed` (sourced and examined) → `deprecated` (superseded). For `reviewed`, include authoritative source links and `reviewed_at` date in both page and index. Document the applicable framework, runtime and relevant versions.

## Checklist
- No misleading claims of testing or Sonar passes.
- References are traceable, sources reliable, conflicting views acknowledged.
- Related IDs exist; relative Markdown links resolve.
- Avoid duplicating concepts without explaining their boundaries.
- Run `python scripts/validate_catalog.py` and correct any errors.
