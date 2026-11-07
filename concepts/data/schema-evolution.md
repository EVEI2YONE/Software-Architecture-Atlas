---
id: schema-evolution
title: "Data schema evolution and migration safety"
category: data
status: reviewed
reviewed_at: 2026-11-07
---

# Data schema evolution and migration safety

> **Reviewed — scoped source-backed guidance, not a target-application audit.**

## Applicability
Schema changes may break concurrently deployed application versions or destroy data. EF Core guidance recommends inspecting and testing migration output, choosing appropriate production deployment methods and separating elevated migration credentials from normal application access. PostgreSQL isolation behavior varies by level; provider/runtime differences matter.

## Candidate expand–migrate–contract sequence
1. **Expand:** add compatible schema while keeping old clients working.
2. **Migrate:** update read/write paths, backfill in bounded batches, check data invariants and observe failures.
3. **Contract:** remove legacy fields only after consumers, jobs, deployments and rollback windows are accounted for.

This is an architectural technique, not a promise of zero downtime. DDL locking, data size and irreversible operations may force a different plan.

## Alternatives and counterexamples
A tiny development database may justify a direct migration; production multi-version rollouts may require staged compatibility. Reverting a destructive migration may not restore lost data.

## Verification and rollback
Inspect generated SQL or provider-specific bundle, exercise old/new application versions against a production-like dataset, measure locking and backfill duration, verify constraints and backup restore. Record owners and actual rollback limits before production deployment.

## Search aliases
schema evolution; architecture contracts; data and security boundaries

## Related concepts
- [transactions](../data/transactions.md)
- [consistency](../distributed-systems/consistency.md)
- [testing-strategy](../quality/testing-strategy.md)

## Evidence and sources
1. EF Core Applying Migrations: https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/applying (accessed 2026-11-07).
2. PostgreSQL 18 Transaction Isolation: https://www.postgresql.org/docs/current/transaction-iso.html (accessed 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Revisit after standards/framework changes, incidents, new consumers or changed trust boundaries.
