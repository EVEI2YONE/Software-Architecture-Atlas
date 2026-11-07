# Remediation verification and handoff

## Branch provenance
- Branched from `main` commit `bce1f540652dc3e315de46d99e778335611bfdd3` on 2026-11-07.
- Seven phase commits are separately reviewable on the shared branch. No application code was changed.

## Completed
1. Canonical inventory and findings recorded.
2. Current coverage reconciled to 93 concepts and misleading category summary corrected.
3. Research snapshot copies preserved in a dedicated archive; original report paths retained for compatibility.
4. Three weakly scoped articles updated with explicit evidence limits; 93-ID audit ledger created.
5. Search guides consolidated and compatibility pointers retained.
6. Coverage/category/active-link regression validator and CI stage added.
7. Limitations and release checks documented here.

## Execution and uncertainty
- A container clone attempt failed due to DNS resolution for github.com. Therefore **local Python validation and tests were not executed**, and no passing-test claim is made.
- CI in this PR should run `python scripts/validate_catalog.py`, `python scripts/validate_documentation.py`, and `python -m unittest discover -s tests -v`. Inspect workflow results before merge.
- The entire 93-concept claim audit is **not complete**. The ledger marks all independent claim checks pending; only three source-scope cautions were introduced. Do not equate these changes with full technical certification.
- Archived reports have original relative links. Original `docs/` copies are intentionally retained; archives are preservation copies, not fully relocated canonical documents. Deleting originals requires a separate complete inbound-link rewrite.
- Source URL reachability and technical claim-to-source correspondence remain open manual review work.

## Merge criteria
- CI green after addressing any regressions.
- Review archived navigation, per-concept evidence limitations and current counts.
- Follow up on unresolved items in `research/open-gaps.md` and `research/claim-audit-ledger.md`.
