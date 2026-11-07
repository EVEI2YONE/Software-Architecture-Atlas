# Knowledge-gap lifecycle and self-heal

## Workflow
1. Inspect target repository and architectural decision context.
2. Search index by terms/tags/related IDs.
3. Classify: absent concept, stub, stale, weak evidence, contradiction, insufficient language-specific context, or missing cross-link.
4. Record gaps using `templates/gap-request.md` with severity, value, evidence and acceptance criteria.
5. Research primary sources, add explicit applicability and trade-offs, review with validators.
6. Promote entries only after evidence review, then update `status`, `reviewed_at`, and `source_count` consistently.
7. Revalidate searchability, links, graph, and documentation.

## Reusable correction log
When a recurring misclassification, misleading stub, dead link, missing topic or unverifiable architectural claim occurs, capture: incident; actual vs expected behavior; source rule that failed; generalized prevention; files changed; test that prevents regression.

## Maintainability policies
Favor meaningful module boundaries over forced layers, explicit flow over abstraction sprawl, and fewer dependencies over incompatible overlapping packages. Track code reduction together with readability, defects, and measured complexity; never optimize line count alone.

## Sequenced research batches
Use [knowledge-gap batches](knowledge-gap-batches.md) to group the numbered [foundational gaps](foundational-gap-assessment.md) by dependencies and deliverables. Do not interpret inclusion in a batch as a reviewed or verified concept. Promote individual concepts only after source, applicability, trade-off and validation checks are complete.
