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
        result = search("testing quality", category="quality", status="stub")
        self.assertTrue(result["results"])
        self.assertTrue(all(hit["category"] == "quality" and hit["status"] == "stub" for hit in result["results"]))

    def test_project_structure_gap_discoverable(self):
        result = search("file structure for UI API Functions WebJobs enterprise")
        self.assertEqual(result["results"][0]["id"], "project-structure-selection")
        self.assertEqual(result["results"][0]["status"], "stub")
        self.assertEqual(result["results"][0]["evidence"], "unknown")

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
        self.assertEqual(search("project-structure-selection")["results"][0]["status"], "stub")

    def test_unmatched(self):
        self.assertEqual(search("zzzzzzzzzzzz")["results"], [])

    def test_no_stub_as_evidence(self):
        self.assertEqual(search("project-structure-selection")["results"][0]["evidence"], "unknown")

    def test_related_expansion_deduped(self):
        hits = search("idempotency", limit=1, expand=2)["results"]
        self.assertEqual(len({hit["id"] for hit in hits}), len(hits))
        self.assertTrue(any(hit["matched_by"].startswith("related:") for hit in hits[1:]))

if __name__ == "__main__":
    unittest.main()
