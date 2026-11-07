# B6 — Operations, reliability, performance and ownership

**Batch:** B6 · **Gaps:** GAP-07, GAP-08, GAP-09, GAP-11, GAP-12 (partially).  
**Research date:** 2026-11-07 · **Status:** Source-backed reference methods curated, but actual deployment/load/recovery/cost verification remains outstanding.

## Context before curation

Earlier batches established: code navigability and reduction (B1), module/deployable boundaries (B2), security and data correctness (B3), project-type layouts (B4), and maturity transitions (B5). The Atlas itself is a knowledge/reference repository. It does **not** include a user-supplied production UI, API, Function or WebJob to benchmark. The original `observability`, `resilience`, `scalability` pages were research stubs, and dedicated deployment, reliability/recovery and operational cost pages were missing.

### Source evidence and applicability

1. [Google SRE, Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) and [Implementing SLOs](https://sre.google/workbook/implementing-slos/): SLIs are measured service behavior; SLOs and error budgets require stakeholder agreement, measurement windows and documented response policies.
2. [AWS Well-Architected Failure Management](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-failmgmt.html): business-defined RTO/RPO and regular backup/restore and failure testing.
3. [Azure Well-Architected Safe Deployments](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments): progressive exposure and health-gated releases with rollback/roll-forward caveats, especially stateful systems.
4. [OpenTelemetry Documentation](https://opentelemetry.io/docs/) and [Semantic Conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/): traces, metrics and logs plus consistent cross-system attributes.
5. [Google SRE Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) and [Production Services Best Practices](https://sre.google/sre-book/service-best-practices/): overload, retries, load shedding, capacity planning and recovery risks.
6. [Azure Performance Efficiency](https://learn.microsoft.com/en-us/azure/architecture/checklist/scalability): capacity targets, performance testing and resource efficiency.
7. [AWS Well-Architected Cost Monitoring](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.question.COST_3.en.html): workload cost attribution, tagging and budget controls.

Sources consulted 2026-11-07. These sources support general or provider-specific **methods**, not claims about a running application or universal numeric targets.

## Curated indexed concepts

**Three previously unverified stubs promoted to scoped reviewed:**
- [Observability and diagnostics](../concepts/operations/observability.md)
- [Resilience patterns](../concepts/operations/resilience.md)
- [Scalability and capacity planning](../concepts/performance/scalability.md)

**Four new scoped reviewed concepts:**
- [Deployment strategies and safe rollback](../concepts/operations/deployment-strategies.md)
- [Reliability objectives and recovery](../concepts/operations/reliability-objectives.md)
- [Operational ownership and cost attribution](../concepts/operations/operational-costs.md)
- [Workload admission and overload](../concepts/runtime/workload-admission.md)

These give agents concrete retrieval targets for `deploy canary`, `SLO error budget`, `RTO RPO recovery`, `retry overload`, `observability traces` and `operational costs`.

## Operating decision matrix

| Workload | Start with | Add complexity when evidence shows | Verify | Rollback/recovery |
| --- | --- | --- | --- | --- |
| Small UI/API | Basic actionable logs, health signal, simple deployment | Deployment faults, user-visible latency, complex request paths | Real error/latency baseline, smoke/contract tests | Known-good build and compatible data |
| Business-critical API | User-oriented SLIs, bounded timeouts, release health checks | Tail latency, external dependency cascades, independently owned teams | Fault injections, retry-budget tests, canary health | Stop rollout or route to safe old version |
| Functions/WebJobs | Trigger/job completion telemetry, idempotency and retry policy | Burst queue age, failed jobs, conflicting scaling limits | Duplicate delivery, queue limits, restart/poison messages | Pause processing safely; preserve job checkpoints |
| Library | Package build and consumer contract tests | Multiple consumers/release cadence | Published artifact compatibility and dependency versions | Supported previous version |
| Multi-project enterprise | Clear operational owner, SLOs and cost attribution | Real independent release/scale/recovery boundaries | End-to-end tracing, disaster recovery test and release drill | Coordinated version/schema rollback |

### Minimum review packet for a real target repo

- **Context:** stack/runtime versions, release topology, dependency/data graph, cost owner, workload criticality and business drivers.
- **Baseline:** user-success/latency indicators, p95/p99, throughput, resource saturation, queue age, error/retry rates, recovery objective, actual cost and toil. Do not invent thresholds.
- **Alternatives:** retain current approach, simplify hot path, tune capacity, bounded concurrency, cache only if justified, progressive rollout only when useful.
- **Experiment:** representative load with bursts and degraded dependencies, failure injection, backup restore rehearsal, contract tests, end-to-end logs/traces, after-hours/on-call ownership.
- **Decision:** observed versus supported versus inferred versus unknown; changes, risks, test results, rollback and revisit triggers.

## Example cross-project incident (illustrative, not a measurement)

A checkout API triggers a payment Function, emits an event and runs a settlement WebJob. If downstream payment latency rises, automatic retries at the API and job both multiply requests. A candidate plan is to measure retry amplification, set an owner-defined deadline and bounded retry policy, prevent duplicate payment effects, track end-to-end completion, and test degradation and recovery. Do **not** claim that adding a queue or circuit breaker automatically improves the outcome. A simpler single-worker design may suffice where capacity is low.

## Operational cost and ownership gate

Before extracting a module into a separately deployed service, compare independently measurable release/scale gains against added network behavior, telemetry, secrets, package versioning, deployment pipeline, on-call responsibility and incident coordination. Evaluate consolidation if multiple services repeatedly deploy together or share a large coupled data model. Track workload cost per business result, not simply number of containers or cloud spend.

## B6 exit accounting

**Research deliverables achieved:** seven scoped reviewed reference concepts; source/constraint declarations; operational review packet; alternatives, failure modes, test and rollback approaches.

**Not verified:** no target system, actual SLO, RTO/RPO, cost figures, load-test results, Sonar quality gate, CI deployment check or real incident drill. `backpressure`, `caching`, `quality-gates`, `testing-strategy` and many runtime-specific examples remain stubs; language-specific and tenancy details need later work.

**Batch state: partially curated**, not operationally validated.

## Agent retrieval

```sh
python scripts/search_catalog.py "service SLO error budget recovery" --json
python scripts/search_catalog.py "canary deployment rollback" --json
python scripts/search_catalog.py "high latency scale capacity" --json
python scripts/search_catalog.py "webjobs overload retry queue" --json
python scripts/search_catalog.py "operational costs ownership" --json
```

A reviewed concept means its sources and trade-offs are documented; it does not authorize claims of verified performance, uptime, security, or recovery of a particular application.
