# B3 — Security, contracts, data integrity and migrations

**Batch:** B3; **gaps:** GAP-03, GAP-04, GAP-06, GAP-10 and supporting transaction/idempotency evidence.  
**Research date:** 2026-11-07. **Outcome:** Source-backed reference guidance curated; actual application behavior remains unverified.

## Context gathered
The Atlas is a reference catalog, not a production UI/API/Functions/WebJobs application. Before B3, threat modeling, API contracts, data schema evolution and identity/access had no canonical indexed entries. Transactions and idempotency existed only as research stubs. The prior B1/B2 work supplied boundaries and refactoring trade-offs, but **no user-supplied application configuration, runtime, database, identity provider, threat model, live traffic or test output** exists from which to assert concrete safety or correctness.

## Primary sources and scope (accessed 2026-11-07)
- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html): system/data-flow modeling and trust boundaries.
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html): least privilege and deny by default.
- [NIST SSDF SP 800-218 v1.1](https://csrc.nist.gov/pubs/sp/800/218/final): final secure-development practices. **NIST SP 800-218 Rev. 1 / v1.2 was an initial public draft as of this assessment**, not a superseding final standard.
- [OpenAPI Specification v3.2.1](https://spec.openapis.org/oas/v3.2.1.html): machine-readable HTTP contract descriptions. Confirm support for this OAS version in actual tooling.
- [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html): HTTP method safety/idempotence, not business-effect exactly-once delivery.
- [PostgreSQL 18 Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html): DB-specific concurrency and retry behavior.
- [EF Core Applying Migrations](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/applying): production migration strategy, review and privilege caveats.

These sources provide **supported method-level guidance** only. They are not target-repository inspection or proof of correct implementation.

## Cross-boundary assessment matrix

| Boundary | Minimum investigation | Preferred simplest candidate | Counterexample / risk | Validation |
| --- | --- | --- | --- | --- |
| Browser -> API | User identity, authorization, input contracts, errors | Backend-enforced permission checks plus documented operation contracts | UI-only restrictions, IDOR/cross-tenant access | Negative auth and contract tests |
| API -> database | Transaction scope, isolation and migration compatibility | One local transaction for one atomic invariant | Cross-service effects cannot be atomically committed with ordinary DB transaction | Concurrent updates, rollback, old/new schema versions |
| Function/WebJob -> queue/API | Duplicate delivery, retries, deadline, credentials | Idempotent effect, bounded retry, least privilege where needed | Multiple effects on timeout, secret reuse | Duplicate/concurrent request and crash-restart tests |
| Service -> partner API | Versioned request/response expectations and failure semantics | Explicit contract and consumer compatibility tests | Breaking supplier changes, unbounded retries | Contract matrix, negative responses, fallback/rollback |
| Deployment -> database | Privileged migration identity, backups, service version overlap | Reviewed script or tested migration bundle as platform permits | Destructive DDL, lock amplification, privilege leakage | Production-like migration, restore rehearsal |

## Worked illustrative scenario (not observed)
A growing business has a web UI, orders API, payment callback Function and settlement WebJob, all using a relational database. Candidate checks:
1. Model browser, callback provider, worker and database trust boundaries; separate UI identity from privileged service identities.
2. Define GET/POST contracts and authorization policies for order access, including negative cross-tenant tests.
3. For payment callbacks, design deduplication scoped to a provider event and verify concurrent duplicate delivery; do not infer exactly-once delivery.
4. Before renaming a database column, compare old/new API and WebJob deployments, stage a compatible schema and rehearse backfill and restore.
5. Evaluate the minimal candidate structure (one app with internal modules plus jobs if deployable concerns justify them) before introducing shared service layers.

## Required checks for a real application
- Actual deployment and dependency boundaries, runtime/framework and DB versions.
- API contract and consumer inventory; security/tenant matrix and identity/secret owners.
- Data-flow diagram with risk and mitigation-to-test traceability.
- Old/new deployed versions, schema migration/rollback plan, backups and data invariants.
- Test output from negative authorization, consumer contract, concurrent transactional and duplicate-event scenarios.
- Compare no-change versus complexity added by frameworks, policy engines, distributed orchestration and duplicated abstraction.

## Batch deliverables and limits
- **Four new indexed reviewed concepts:** [threat modeling](../concepts/governance/threat-modeling.md), [API contracts](../concepts/distributed-systems/api-contracts.md), [schema evolution](../concepts/data/schema-evolution.md), [identity and access](../concepts/governance/identity-and-access.md).
- **Two existing stubs researched:** [transactions](../concepts/data/transactions.md), [idempotency](../concepts/distributed-systems/idempotency.md).
- **Still open:** full service-contract examples for named runtimes, cross-service outbox/event schema strategies, credential-store configuration, quantitative production validation and application-specific test runs. `consistency`, `testing-strategy` and `supply-chain` remain stubs.
- **State:** **partially curated**, because no target application or actual tests are available. Do not interpret the reviewed status as audit certification.

## Agent retrieval
Use `python scripts/search_catalog.py "threat model API data migration" --json` or a focused query. Prefer one canonical ID plus related links and read its specific source applicability; a `reviewed` label requires source inspection. Never assert compliance, authorization correctness, safe migrations or exactly-once execution from the index alone.
