"""Tests for the zero-dependency catalog search."""
import unittest
from scripts.search_catalog import search

class SearchCatalogTests(unittest.TestCase):
    def test_canonical_id_first(self):
        self.assertEqual(search("idempotency")["results"][0]["id"], "idempotency")

    def test_alias(self):
        self.assertEqual(search("dependency hell")["results"][0]["id"], "dependency-conflicts")

    def test_deterministic(self):
        self.assertEqual(search("concurrency", limit=4), search("concurrency", limit=4))

    def test_filter(self):
        result = search("async thread", category="runtime", status="stub")
        self.assertTrue(result["results"])
        self.assertTrue(all(hit["category"] == "runtime" and hit["status"] == "stub" for hit in result["results"]))

    def test_project_structure_gap_discoverable(self):
        result = search("file structure for UI API Functions WebJobs enterprise")
        self.assertEqual(result["results"][0]["id"], "project-structure-selection")
        self.assertEqual(result["results"][0]["status"], "reviewed")
        self.assertEqual(result["results"][0]["evidence"], "requires-source-inspection")

    def test_b3_retrieval(self):
        self.assertEqual(search("threat model")["results"][0]["id"], "threat-modeling")
        self.assertEqual(search("api versioning")["results"][0]["id"], "api-contracts")
        self.assertEqual(search("database migration")["results"][0]["id"], "schema-evolution")
        self.assertEqual(search("identity-and-access")["results"][0]["status"], "reviewed")

    def test_b4_scoped_project_retrieval(self):
        for query, expected in [
            ("nextjs", "ui-project-structure"),
            ("minimal api", "api-project-structure"),
            ("azure functions project", "functions-project-structure"),
            ("webjobs scheduled worker", "webjobs-project-structure"),
            ("python library", "libraries-project-structure"),
            ("multi project solution", "multi-project-structure"),
        ]:
            hit = search(query)["results"][0]
            self.assertEqual(hit["id"], expected, query)
            self.assertEqual(hit["status"], "reviewed")
        self.assertEqual(search("project-structure-selection")["results"][0]["status"], "reviewed")

    def test_b5_growth_and_migration_retrieval(self):
        self.assertEqual(search("prototype MVP enterprise")["results"][0]["id"], "architecture-evolution")
        self.assertEqual(search("strangler migration")["results"][0]["id"], "incremental-boundary-migration")
        self.assertEqual(search("project-structure-selection")["results"][0]["evidence"], "requires-source-inspection")

    def test_b6_operational_retrieval(self):
        for query, expected in [
            ("slo error budget", "reliability-objectives"),
            ("canary deployment", "deployment-strategies"),
            ("load shedding", "workload-admission"),
            ("operational costs", "operational-costs"),
        ]:
            result = search(query)
            self.assertEqual(result["results"][0]["id"], expected, query)
            self.assertEqual(result["results"][0]["status"], "reviewed")
        self.assertEqual(search("caching")["results"][0]["status"], "stub")

    def test_unmatched(self):
        self.assertEqual(search("zzzzzzzzzzzz")["results"], [])

    def test_no_stub_as_evidence(self):
        hit = search("caching")["results"][0]
        self.assertEqual(hit["status"], "stub")
        self.assertEqual(hit["evidence"], "unknown")

    def test_b8_canonical_retrieval(self):
        for concept_id in [
            "project-structure-selection", "vertical-slice-architecture",
            "package-by-feature-vs-layer", "module-public-contracts",
            "architecture-dependency-rules", "monorepo-vs-multirepo",
        ]:
            hit = search(concept_id)["results"][0]
            self.assertEqual(hit["id"], concept_id)
            self.assertEqual(hit["status"], "reviewed")
            self.assertEqual(hit["evidence"], "requires-source-inspection")

    def test_b9_canonical_retrieval(self):
        for concept_id in [
            "dependency-conflicts", "supply-chain", "cognitive-complexity",
            "quality-gates", "testing-strategy", "transitive-dependency-resolution",
            "package-locking-and-version-policy", "cyclic-dependency-prevention",
            "dead-code-and-dependency-removal", "sonar-rules-and-quality-profiles",
            "mutation-and-contract-testing", "architecture-fitness-functions",
        ]:
            hit = search(concept_id)["results"][0]
            self.assertEqual(hit["id"], concept_id)
            self.assertEqual(hit["status"], "reviewed")
            self.assertEqual(hit["evidence"], "requires-source-inspection")

    def test_b10_canonical_retrieval(self):
        for concept_id in [
            "bounded-contexts", "aggregates", "domain-events", "cqrs",
            "ubiquitous-language", "context-mapping",
            "domain-services-vs-application-services", "transactional-invariants",
            "anti-corruption-layers", "data-access-boundaries", "isolation-levels",
        ]:
            hit = search(concept_id)["results"][0]
            self.assertEqual(hit["id"], concept_id)
            self.assertEqual(hit["status"], "reviewed")
            self.assertEqual(hit["evidence"], "requires-source-inspection")

    def test_related_expansion_deduped(self):
        hits = search("idempotency", limit=1, expand=2)["results"]
        self.assertEqual(len({hit["id"] for hit in hits}), len(hits))
        self.assertTrue(any(hit["matched_by"].startswith("related:") for hit in hits[1:]))

if __name__ == "__main__":
    unittest.main()
