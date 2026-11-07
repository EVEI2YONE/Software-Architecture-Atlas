# Documentation remediation audit

Baseline: `bce1f540652dc3e315de46d99e778335611bfdd3` (main, 2026-11-07). This ledger distinguishes mechanical findings from claims requiring expert technical verification.

## Baseline inventory
- 93 canonical concepts; 93 reviewed; 0 stubs.
- Categories: principles (7), domain-design (8), code-organization (22), dependencies (6), runtime (9), distributed-systems (10), data (5), performance (7), quality (6), operations (5), governance (8).
- Scope: documentation, archival structure, evidence specificity, and retrieval/validation tooling. No application-specific performance or security claims are made.

## Findings and dispositions
| Finding | Severity | Planned disposition |
| --- | --- | --- |
| `docs/coverage.md` opens with pre-campaign counts and category inventory | High | Replace active summary with canonical totals; preserve batch timeline in research archive |
| `concepts/code-organization/README.md` says 18 pages, index has 22 | Medium | Correct count and add consistency guard |
| `docs/b7-b14-campaign.md` retains an initial "not started" matrix beside completion board | Medium | Archive as historical state with prominent snapshot labels |
| `docs/knowledge-gap-batches.md` is a proposed roadmap for completed work | Medium | Archive and distinguish any still-open empirical verification |
| `docs/agent-search.md` and `docs/agentic-search.md` overlap | Medium | Merge into an active retrieval guide, preserve old path as compatibility pointer if needed |
| Reviewed source lists may be adjacent rather than claim-specific | High | Add evidence-audit ledger; correct misleading pages without inventing source verification |
| `scripts/validate_catalog.py` checks concept-local links rather than all Markdown | Medium | Add repo-wide link and navigation checks with tests |

## Technical audit status
The catalog's `reviewed` label records scoped source-based curation, not independent verification of each assertion. Perform technical review against primary documentation and source versions; log unresolved cases. A URL count must not imply that every claim was verified.

## Rules
1. Preserve IDs and canonical concept paths.
2. Preserve historical research through versioned archival moves.
3. Document any unresolved assertion rather than silently claiming it was verified.
4. Run existing validation and regression tests before merge; record actual results, not assumed successes.
