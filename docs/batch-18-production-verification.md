# B18 — Production observability, hosted identity and frontend verification

**Research date:** 2026-11-07. **Scope:** Final Expanse Phase 5 blockers only. **Status:** scoped reference and runnable verification plan; no target-system deployment, OIDC integration, PostgreSQL worker drill, or frontend browser test was executed.

This is a **companion runbook**, not another canonical concept. Extend the existing [observability](../concepts/operations/observability.md), [reliability objectives](../concepts/operations/reliability-objectives.md), [identity and access](../concepts/governance/identity-and-access.md), [package locking](../concepts/dependencies/package-locking-and-version-policy.md), and [testing strategy](../concepts/quality/testing-strategy.md) pages. B15 owns local transactions, B16 owns worker fencing, and B17 owns market-data validity.

## 1. Durable worker monitoring, readiness and incident recovery

### Separate three questions

| Signal | What it proves | What it does NOT prove |
| --- | --- | --- |
| **Liveness** | A process is running/responding to its probe | A bot has executed a valid strategy, or has an active lease |
| **Readiness** | A process currently passes its defined dependency and admission checks | Every due job is progressing or market data is current |
| **Business progress** | An authorized paper-bot evaluation was completed and durably recorded | Trading profitability or safe external live execution |

A successful HTTP health response alone must not mark a trading worker healthy. Observe scheduled work from authoritative database records; distinguish intentionally paused/stopped bots from due work. Health endpoints should not perform consequential jobs, reset leases or expose financial/user data.

### Proposed minimum telemetry contract (application-specific names)

| Signal | Type | Dimensions / policy | Operational purpose |
| --- | --- | --- | --- |
| `paper_worker_due_age_seconds` | gauge | environment, worker pool; controlled label set | Oldest eligible due job age |
| `paper_worker_last_success_age_seconds` | gauge | worker group only | Detect stalled useful work |
| `paper_worker_evaluation_total` | counter | outcome: success/hold/skip/rejected/failure | Outcome rates and regression symptoms |
| `paper_worker_evaluation_duration_seconds` | histogram | controlled outcome/reason class | Slow execution or external dependency |
| `paper_worker_claim_conflict_total` | counter | worker group | Contention/lease acquisition anomalies |
| `paper_worker_lease_renewal_failure_total` | counter | error class only | Possible ownership loss |
| `paper_worker_expired_lease_count` | gauge | worker group | Repeated stale or stalled work |
| `paper_worker_retry_count` | gauge | bounded class | Retry accumulation |
| `paper_worker_terminal_failure_total` | counter | sanitized failure code | Poison jobs or permanent configuration errors |
| `paper_market_data_rejection_total` | counter | B17 quality reason | Bad/stale/unavailable strategy inputs |

These instrument names, units, and dimensions are **proposals**, not OpenTelemetry predefined standard instrument names or measured requirements. Use OpenTelemetry metric naming and semantic convention guidance, sampling and resource attributes appropriate for deployed SDK versions. Do not include customer IDs, bot IDs, access tokens, exchange secrets, prices, prompts or high-cardinality per-job values as metric labels [1, 2]. Restrict traces/logs containing resource identities and redact user secrets.

Recommended structured **restricted logs**: timestamp UTC, trace/run correlation ID, anonymized tenant reference where authorized, job ID (access-controlled), lease generation, configuration revision, outcome reason code, external endpoint category, and elapsed duration. Never log bearer tokens or API keys.

### SLI/SLO and operational policy

Choose stakeholder-approved windows and thresholds **from real workload baselines**; do not invent a universal success target. Example SLIs to define: due-job completion within agreed lag, recoverable failed-job percentage, percentage of scheduled evaluations rejected due to stale data, time to detect a lost lease, and time to resume work after worker restart. Denominators must exclude intentionally paused bots when appropriate. Paper-market data unavailability should be visible as a **SKIP**, not falsely counted as a successful trade. Alert on actionable symptoms and verify that someone actually receives alerts [3, 4].

### Failure drill and owner matrix — proposed, NOT RUN

| Injected incident | Expected result | Evidence to capture |
| --- | --- | --- |
| Kill active worker before/after DB commit | B16 replay/fencing preserves at most one financial effect | Receipt count, generation, recovery age |
| Block PostgreSQL from worker | No unguarded write; readiness degraded; error surfaced | DB errors, job age, alert routed |
| Hold renewal until lease expires | Old generation rejected; successor may reclaim | Renewal failures, old/new token, no duplicate fill |
| Stale or unavailable Kraken feed | B17 SKIP reason, no fabricated HOLD or price | Rejection metric and source age |
| Worker process healthy but job loop dead | Business progress SLI catches condition | Last-success age, due-job lag |
| Stop a bot while evaluation pending | No obsolete fill after stop | State revision, receipt count |
| Flood invalid jobs | Bounded attempts, terminal failures, no hot retry loop | Retry rates, queue age, operator action |
| Alert destination missing/unreachable | Incident not counted as operationally ready | Alert firing and receipt evidence |
| Restore lost PostgreSQL state | RTO/RPO measured and reconciled | Backup integrity, restored jobs and receipts |

Every drill requires **real deployment and environment-specific evidence** before any production readiness claim. Record failure owner, runbook action, halt/restart criteria and customer impact; require an explicit trading stop/disable mechanism when monitoring or ownership is uncertain. Do not use restart loops as a substitute for recovery policy.

## 2. Hosted OIDC authentication, tenant isolation and sessions

### Browser/client architecture choices

RFC 10017 (August 2026) documents browser OAuth deployment patterns and their trade-offs [5]. For a first-party hosted React UI + Python backend, **evaluate a backend-for-frontend (BFF)** that handles authorization code flow and stores OAuth tokens on the server side, using an appropriately hardened browser session. A pure SPA is another possible architecture, but it is a public client, cannot protect a client secret, and needs PKCE and stronger token-exposure controls. The choice depends on product hosting, domain layout, API call patterns, risk and deployment complexity; do not mandate a BFF by default.

| Area | Proposed minimum boundary | Test |
| --- | --- | --- |
| Login | Authorization Code + PKCE where relevant; strict provider redirect/callback and anti-CSRF/state handling | Wrong/old state or code verifier rejected; callback cannot be swapped |
| OIDC identity | Validate provider issuer, intended audience/client, signature/key, expiry and nonce where required [6] | Wrong issuer/audience, expired token, forged algorithm, key rollover |
| API authorization | Check the API's **access token** using provider-specific issuer, signature, audience, expiration, scopes and server-owned resource policy | ID token used as an API access credential is rejected unless explicitly documented/supported |
| Actor key | Resolve account from trusted `issuer + sub` (or documented stable provider ID), not email, display name or client-controlled tenant selector | Email changes and same-email/different-issuer do not cross-link accounts |
| Tenant ownership | Every customer-owned query/write derived from resolved actor scope; verify object-level policies independent of frontend | Cross-customer read/update, known-ID probe, background-worker ownership |
| Session | HttpOnly, Secure, appropriate SameSite cookies for BFF, CSRF defenses, rotation and expiry; decide storage and revocation according to threat model | XSS/CSRF, logout, fixation, stolen/expired cookie, stale session |
| Token storage | Keep authorization and refresh tokens server-side for BFF; if SPA pattern, account for browser token exposure and provider policy [5] | No tokens in URLs, frontend logs, analytics or localStorage by default |
| Signing keys | Use vetted issuer discovery/JWKS, explicit algorithm allowlist, bounded cache and rotation behavior; fail closed when unverifiable | Unknown `kid`, forced `alg=none`, stale keys and outage |
| Secrets/roles | Provider client credentials and exchange secrets stored with least privilege and rotation; separate customer vs worker access | Unauthorized job/secret read, secret rotation and revocation |
| Service identity | Workers use purpose-specific service identity while preserving customer ownership in job records; not forged end-user bearer tokens | Worker cannot impersonate tenant, API cannot bypass ownership |

**Important distinction:** OIDC **ID tokens** establish user authentication for a client; OAuth **access tokens** authorize API access according to their issuing provider's rules. Never assume an ID token is valid as an API bearer token merely because it contains a subject [6, 7].

A FastAPI dependency should verify the configured provider's token with a tested library and return a typed actor. Application services must then query/update data within that actor's server-derived account scope. The frontend can guide UX but must not be the authoritative permission evaluator. Persist account membership/ownership and audit changes with versioned policies; organization-ready schema does not imply already implemented organization-level authorization.

### Negative test matrix — proposed, NOT RUN

- Forged or `none` signing algorithm; unknown key ID; invalid issuer/audience; expired or premature token; invalid nonce/state; PKCE downgrade.
- User swaps account or bot ID in route/body/query; cross-tenant list/read/write and worker status; object ID enumeration.
- Same email address but two separate issuer/subject identities; changed email or deleted identity.
- Session expiration, logout, refresh-token failure, CSRF request, browser history/token leakage, revoked credential, unavailability of issuer/JWKS.
- CORS/cookie domain and SameSite behavior in **actual deployed domains**, including allowed cross-origin and forbidden origins.
- Provider signing key rotation and cache expiry; distinguish temporary key-retrieval errors from legitimate authentication.
- Worker service claims unexpected tenant authority; customer API key inadvertently used for migration/administrative operations.

The hosted provider, real redirect URIs, JWT validation configuration, database-tenancy policies, key lifecycle and browser session have **not** been exercised by this Atlas reference.

## 3. React/Vite reproducible build, contract and accessibility verification

### Build gate from a clean CI runner

Record the actual package manager version, Node runtime, Vite and React/TypeScript versions; retain the committed lockfile and project configuration. `npm ci` performs a clean lockfile-consistent install and fails on manifest/lockfile disagreement [8]. Vite's production build does **not** independently typecheck a TypeScript project; run `tsc --noEmit` or `tsc -b` per actual tsconfig before `vite build` [9].

Illustrative CI run commands **only when matched by the project's package scripts**:

~~~sh
cd apps/web
node --version
npm --version
npm ci
npm run typecheck        # must invoke applicable tsc project check
npm test                 # must run meaningful source/component tests
npm run build            # Vite production output
# launch configured API+web test servers, then run Playwright E2E
npx playwright test
~~~

If actual scripts differ, adapt them; these commands are not evidence that Final Expanse supports each script. Do not replace missing React types with silent ambient declarations merely to make compilation pass. When an offline development environment cannot install dependencies, run the build in a clean network-enabled CI environment and inspect its **actual job logs**; source-only tests are not a substitute.

### Test layers and completion evidence

| Layer | Minimum evidence | Specific failure case |
| --- | --- | --- |
| Dependency/install | Reproducible clean `npm ci` on pinned Node | Lock drift, undeclared dependency |
| Type/contract | Generated OpenAPI types match backend and tsc passes | Stale fields, mismatched API error variants |
| Build | Vite production bundle produced and previewed | Missing env vars or incorrect base path |
| API integration | Authenticated tenant-scoped user flows | Token expiry, 401/403, tenant swap, aborted requests |
| E2E browser | Real navigation from login to bot setup, pause/stop and portfolio | Browser auth/cookie/CORS mismatch or broken error recovery |
| Accessibility | Automated axe + keyboard/focus, contrast, accessible names; manual check | Unlabeled controls, inaccessible status feedback, focus lost |
| Recovery | Slow API, 429/5xx, stale data, empty results, offline/retry | Loading indefinitely, fabricated "current" data |

Playwright + axe can detect many, **not all**, accessibility issues; manual keyboard and assistive-technology testing remains necessary [10]. Test mobile/desktop breakpoints and reduced motion as relevant. Any trading action must display correct mode (paper/live), consequence and consent; CSS/DOM tests alone cannot certify safe risk disclosure.

### Release evidence packet

- Locked dependency and Node versions, CI run ID, actual typecheck/build/test output, reproducible browser test environment and artifact integrity.
- Authenticated read-only market discovery and paper bot journeys; negative 401/403 and cross-tenant cases.
- Accessibility results plus unresolved findings, keyboard walkthrough and screen-reader checks.
- Clear proof that development-only tokens and synthetic-price endpoints are unavailable in deployed production.
- An explicit list of unavailable external providers, tests that only use fixtures, and any failed or skipped checks.

## What B18 does *not* certify

This document provides verified **reference sources** and a scoped design/test plan, not source-code evidence for Final Expanse. It does not implement a cloud identity provider, measure worker uptime, deploy a frontend, validate exchange permissions, or run real-browser accessibility tests. New source revisions, deployed versions and actual security requirements require re-verification.

## Evidence and primary sources

1. OpenTelemetry, Metrics Semantic Conventions: https://opentelemetry.io/docs/specs/semconv/general/metrics/ (accessed 2026-11-07). Metric naming/units conventions; proposed worker instruments are application-defined.
2. OpenTelemetry, Documentation and Context Propagation: https://opentelemetry.io/docs/ (accessed 2026-11-07). General instrumentation concepts.
3. Google SRE, Service Level Objectives: https://sre.google/sre-book/service-level-objectives/ (accessed 2026-11-07). Stakeholder-defined SLI/SLO methods.
4. Google SRE Workbook, Implementing SLOs: https://sre.google/workbook/implementing-slos/ (accessed 2026-11-07). Measurement and operational response methods.
5. IETF RFC 10017, OAuth 2.0 for Browser-Based Applications (August 2026): https://www.rfc-editor.org/rfc/rfc10017.html (accessed 2026-11-07). BFF/browser public-client patterns and PKCE.
6. OpenID Foundation, OpenID Connect Core 1.0: https://openid.net/specs/openid-connect-core-1_0.html (accessed 2026-11-07). ID token verification and client identity.
7. IETF RFC 9700, OAuth 2.0 Security Best Current Practice: https://www.rfc-editor.org/rfc/rfc9700.html (accessed 2026-11-07). Current OAuth code-flow and security guidance.
8. npm CLI v11, npm ci: https://docs.npmjs.com/cli/v11/commands/npm-ci/ (accessed 2026-11-07). Lockfile-consistent clean install.
9. Vite, Building for Production: https://vite.dev/guide/build (accessed 2026-11-07). Bundling and separate typecheck considerations.
10. Playwright, Accessibility testing: https://playwright.dev/docs/accessibility-testing (accessed 2026-11-07). Automated accessibility test implementation and limitations.

## Maintenance

Reviewed for source applicability 2026-11-07. Confirm OIDC/provider specifics, deployed Node/Vite, OpenTelemetry SDK versions, browser hosting topology and real backend code before adopting. B19 will examine cross-concept consistency and retrieval, not execute these application tests.
