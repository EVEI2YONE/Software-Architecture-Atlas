"""B0 regression tests: evidence integrity and metadata checks."""
import json
import tempfile
import unittest
from pathlib import Path
from scripts.validate_catalog import validate


class CatalogValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "catalog").mkdir()
        (self.root / "concepts" / "principles").mkdir(parents=True)
        (self.root / "catalog" / "taxonomy.json").write_text(
            json.dumps({"categories": [{"id": "principles"}]}), encoding="utf-8")
        self.entry = {
            "id": "example", "title": "Example", "category": "principles",
            "path": "concepts/principles/example.md", "status": "reviewed",
            "tags": ["test"], "related": [], "source_count": 1,
            "reviewed_at": "2026-11-07"
        }
        self.page = self.root / self.entry["path"]
        self.page.write_text(
            "---\nid: example\ncategory: principles\nstatus: reviewed\nreviewed_at: 2026-11-07\n---\n"
            "# Example\n\n## Evidence and sources\n1. Source: https://example.org/doc\n",
            encoding="utf-8")
        self.write_index()

    def write_index(self):
        (self.root / "catalog" / "index.json").write_text(
            json.dumps({"concepts": [self.entry]}), encoding="utf-8")

    def test_valid_reviewed_reference(self):
        self.assertEqual(validate(self.root), [])

    def test_source_count_mismatch(self):
        self.entry["source_count"] = 2
        self.write_index()
        self.assertTrue(any("source_count" in error for error in validate(self.root)))

    def test_duplicate_related_and_tags(self):
        self.entry["tags"] = ["test", "test"]
        self.entry["related"] = ["example", "example"]
        self.write_index()
        errors = validate(self.root)
        self.assertTrue(any("duplicate tags" in e for e in errors))
        self.assertTrue(any("duplicate related" in e for e in errors))
        self.assertTrue(any("self-related" in e for e in errors))

    def test_frontmatter_review_date_mismatch(self):
        self.page.write_text(self.page.read_text().replace(
            "reviewed_at: 2026-11-07", "reviewed_at: null"), encoding="utf-8")
        self.assertTrue(any("frontmatter mismatch for reviewed_at" in e for e in validate(self.root)))

    def test_stub_cannot_have_reviewed_evidence(self):
        self.entry.update(status="stub", reviewed_at=None, source_count=1)
        self.write_index()
        self.assertTrue(any("stub must have" in e for e in validate(self.root)))

    def test_broken_local_link(self):
        with self.page.open("a", encoding="utf-8") as f:
            f.write("\n[missing](not-here.md)\n")
        self.assertTrue(any("broken link" in e for e in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
