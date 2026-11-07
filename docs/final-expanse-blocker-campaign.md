# Final Expanse blocker research campaign — B15–B19

**Base:** `main` · **Shared working branch:** `research/final-expanse-blockers-b15-b19`  
**Purpose:** Fill only the knowledge gaps identified for Final Expanse's Phase 5 reliability and hosted-SaaS blockers. This is a reference-catalog research campaign; it does not change or certify Final Expanse application code.

## Context and deduplication

The Atlas already has reviewed concepts for `transactions`, `isolation-levels`, `transactional-invariants`, `data-access-boundaries`, `idempotency`, `observability`, `reliability-objectives`, `identity-and-access`, `package-locking-and-version-policy` and `testing-strategy`. Their scoped references are guidance rather than target-system measurements. Preserve existing canonical IDs and avoid copying their generic content.

| Batch | Blocker scope | Status | Exit evidence |
| --- | --- | --- | --- |
| B15 | PostgreSQL transaction invariants, SQLAlchemy sessions, contention and concurrency tests | In progress | Focused patterns, decision matrix, negative-case test plan, indexed retrieval |
| B16 | Worker leases, fencing, retry and crash-recovery ownership | Pending | Failure matrix and no-stale-worker verification protocol |
| B17 | Trusted exchange market data and trading-decision eligibility | Pending | Data validation states and reject/skip fixture matrix |
| B18 | Worker telemetry, hosted OIDC/tenant isolation, reproducible frontend build | Pending | Domain-specific verification recipes and security boundaries |
| B19 | Consistency, source audits and agent retrieval evaluation | Pending | Catalog validation, golden queries, blocker-to-concept handoff |

## Operating rules

1. Reuse **this one PR** for each batch; add independently reviewable commits.
2. Inspect canonical index and existing concepts before adding a page. Prefer extension where the concept already exists.
3. Cite primary vendor documentation with explicit applicable versions. Distinguish vendor behavior, design inference, and application-tested evidence.
4. Validate frontmatter, indexed metadata, local links and golden retrieval; never equate an index test with real PostgreSQL/worker/browser execution.
5. Keep this campaign limited to the six identified blockers.

## Batch B15 context snapshot

- **Existing foundation:** `concepts/data/transactions.md`, `concepts/data/isolation-levels.md`, `concepts/domain-design/transactional-invariants.md` and `concepts/data/data-access-boundaries.md`.
- **Unresolved:** PostgreSQL row-lock choices, `SKIP LOCKED` semantics, a bounded SQLAlchemy 2.x unit-of-work pattern, retry ownership, monetary/tenant invariants and a runnable real-PostgreSQL concurrency test plan.
- **Not evidence:** Final Expanse's earlier SQLite tests do not validate PostgreSQL row locks or multi-process contention.
- **Boundary:** B15 documents transactions and safe concurrency. B16 owns cross-process lease/heartbeat/fencing semantics.
