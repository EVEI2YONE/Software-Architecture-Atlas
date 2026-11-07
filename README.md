# Software Architecture Atlas

A **human-readable and agent-searchable** knowledge catalog covering software architecture, design principles, dependency health, clean code, asynchronous and distributed systems, scalability, and maintainability.

This is a **knowledge/reference repository**, not a claim that every scaffolded concept is vetted. The initial 30 concept pages began as research stubs. Concept status now varies; always check the canonical index, reviewed source evidence and applicable runtime constraints.

## Start here

- [Agent reading and contribution instructions](AGENTS.md)
- [Full concept index](catalog/index.json) (machine-readable)
- [Topic taxonomy](catalog/taxonomy.json)
- [Current concept coverage](docs/coverage.md)
- [Research archive and remaining evidence gaps](research/README.md)
- [Sequenced knowledge-gap research batches](docs/knowledge-gap-batches.md)
- [Batch B0: catalog evidence integrity and agent retrieval benchmark](docs/batch-0-catalog-integrity.md)
- [Batch B1: code organization research and measurement guide](docs/batch-1-code-organization.md)
- [Batch B2: architectural drivers and boundary decisions](docs/batch-2-architecture-boundaries.md)
- [Batch B3: security, contracts, data and correctness](docs/batch-3-security-contracts-data.md)
- [Batch B4: application type file-structure archetypes](docs/batch-4-project-archetypes.md)
- [Batch B5: prototype to enterprise evolution](docs/batch-5-maturity-evolution.md)
- [Batch B6: operations, reliability and scalability](docs/batch-6-operations-reliability.md)
- [Navigation and retrieval guide](docs/agent-search.md)
- [Source and evidence policy](docs/evidence-policy.md)
- [Knowledge-gap and curation workflow](docs/curation-workflow.md)
- [Entry template](templates/concept.md)

## Browse by topic
- [principles](concepts/principles/README.md): Design principles and practical trade-offs
- [domain-design](concepts/domain-design/README.md): Domain-driven design and business boundaries
- [code-organization](concepts/code-organization/README.md): Modularity, human navigation and code reduction
- [dependencies](concepts/dependencies/README.md): Dependency resolution, third-party packages and supply chain
- [runtime](concepts/runtime/README.md): Asynchrony, threading and concurrency safety
- [distributed-systems](concepts/distributed-systems/README.md): Distributed communication, failure and consistency
- [data](concepts/data/README.md): Data models, transactions and access patterns
- [performance](concepts/performance/README.md): Caching, capacity and scalability
- [quality](concepts/quality/README.md): Readability, tests, Sonar and static quality gates
- [operations](concepts/operations/README.md): Resilience, observability and delivery
- [governance](concepts/governance/README.md): Architecture decisions and lifecycle

## Agent quick path

1. Search `catalog/index.json` by `id`, `title`, `tags`, `summary`, or `related` before scanning pages.
2. Read relevant concept pages, then follow relative links to adjacent decisions.
3. Treat `status: stub` as **unknown**, not authoritative; inspect citations and freshness for reviewed pages.
4. Return evidence-linked architectural recommendations and open a gap request for missing/unverified concepts.
5. After additions/edits, run `python scripts/validate_catalog.py` and update the machine index as necessary.

## Contributing

Add one concept per stable canonical ID. Follow [CONTRIBUTING.md](CONTRIBUTING.md), cite authoritative primary sources, distinguish facts from trade-offs, and document version/platform applicability. A Sonar quality gate is **project-configured**, not a universal threshold.

## Scope and boundaries

Prioritize realistic simplicity and developer comprehension over maximal architectural sophistication. Do not encourage blanket microservices, CQRS, layers, interfaces, caching, or async for their own sake. Security and correctness outweigh line-count reduction. Catalog reviews do not substitute for running tests, profiling, dependency resolution, security scanning, or Sonar analysis on a target repository.

## Agent-friendly search

Run `python scripts/search_catalog.py "dependency hell" --json` for deterministic offline, machine-readable concept lookup, or `python scripts/search_catalog.py "idempotency" --expand 2 --json` to traverse related concepts. See [agentic search guide](docs/agentic-search.md) for result schema, evidence handling, limitations and examples. Run `python -m unittest discover -s tests -v` for retrieval tests.

## B7–B14 campaign and architecture overlays

- [Shared research and completion board](docs/b7-b14-campaign.md)
- [B14 agent retrieval and cross-language review](docs/batch-14-agent-retrieval.md)
- [Language overlays](concepts/code-organization/README.md): C#/.NET, TypeScript/Node, Java/Scala and Python
- [Evidence and agent search governance](concepts/governance/README.md): ADR lifecycle, index validation and retrieval evaluation

A `reviewed` page means scoped references and curation metadata are present, **not** that its source claims or recommendations were independently validated on the reader's application.
