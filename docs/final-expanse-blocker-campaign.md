# Final Expanse blocker research campaign — B15–B19

**Base:** `main` · **Shared working branch:** `research/final-expanse-blockers-b15-b19`  
**Purpose:** Fill only the knowledge gaps identified for Final Expanse's Phase 5 reliability and hosted-SaaS blockers. This is a reference-catalog research campaign; it does not change or certify Final Expanse application code.

## Context and deduplication

The Atlas already has reviewed concepts for `transactions`, `isolation-levels`, `transactional-invariants`, `data-access-boundaries`, `idempotency`, `observability`, `reliability-objectives`, `identity-and-access`, `package-locking-and-version-policy` and `testing-strategy`. Their scoped references are guidance rather than target-system measurements. Preserve existing canonical IDs and avoid copying their generic content.

| Batch | Blocker scope | Status | Exit evidence |
| --- | --- | --- | --- |
| B15 | PostgreSQL transaction invariants, SQLAlchemy sessions, contention and concurrency tests | Research complete; CI passed | Focused patterns, decision matrix, negative-case test plan, indexed retrieval |
| B16 | Worker leases, fencing, retry and crash-recovery ownership | Research complete; CI passed | Failure matrix and no-stale-worker verification protocol |
| B17 | Trusted exchange market data and trading-decision eligibility | Research complete; CI passed | Data validation states and reject/skip fixture matrix |
| B18 | Worker telemetry, hosted OIDC/tenant isolation, reproducible frontend build | Research complete; CI passed | Domain-specific verification recipes and security boundaries |
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

## B15 outcome

- [B15 research report](batch-15-postgresql-concurrency.md) and [new indexed concept](../concepts/data/postgresql-transactional-concurrency.md) delivered.
- GitHub Actions catalog, documentation and retrieval tests passed on the B15 report revision; re-run after any later changes.
- Real-PostgreSQL Final Expanse concurrency and load/failure tests remain application-level blockers, not resolved by the Atlas.

## B16 outcome

- [B16 research handoff](batch-16-worker-leases-fencing.md) and [canonical lease/fencing concept](../concepts/distributed-systems/durable-worker-leases-and-fencing.md) added, with failure tests and retrieval cases.
- Source-scoped guidance only; real PostgreSQL cross-process fencing, worker heartbeat and failure injection have **not** been executed on Final Expanse.
- B17 has been delivered on the same PR; B18 follows.

## B17 outcome

- [B17 source review and verification handoff](batch-17-trading-market-data-integrity.md) and [indexed trading market-data integrity concept](../concepts/data/trading-market-data-integrity.md) delivered with negative fixture and retrieval coverage.
- Kraken documentation supports unfinished last REST OHLC candle, bounded history and instrument metadata; threshold decisions and normalized schema remain architectural proposals.
- Live read-only network, customer-specific eligibility, execution safety and paper-fill realism have **not** been verified in Final Expanse.
- Next batch: B18 production observability, OIDC/tenancy and frontend verification.

## B18 outcome

- [B18 production verification runbook](batch-18-production-verification.md) adds worker-specific progress/lease telemetry, failure drills, hosted OIDC/PKCE and account-ownership negative tests, plus clean React/Vite install, typecheck, build and accessibility gates.
- **No new canonical concepts required:** existing observability, reliability, identity, dependency locking and testing strategy entries were extended and linked to the runbook.
- GitHub Actions catalog, documentation and agent-search tests passed with the B18 regression file present. No Final Expanse identity provider, hosted worker deployment, npm build, browser or accessibility validation was executed by this Atlas batch. B19 is the final research integration/verification batch.
