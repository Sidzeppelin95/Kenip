from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ["index.html", "solutions/index.html", "work/index.html", "capabilities/index.html", "technology/index.html", "approach/index.html", "about/index.html", "contact/index.html", "privacy/index.html", "terms/index.html", "404.html"]

class StaticPagesTests(unittest.TestCase):
    def assert_site_root(self, site_root):
        self.assertTrue((site_root / "index.html").is_file(), f"Missing entry point in {site_root}")
        self.assertTrue((site_root / "index.html").read_text(encoding="utf-8").lstrip().lower().startswith("<!doctype html>"))
        for relative in PAGES:
            with self.subTest(root=str(site_root), page=relative):
                page = site_root / relative
                self.assertTrue(page.is_file(), f"Missing static page: {page}")
                html = page.read_text(encoding="utf-8")
                self.assertIn("<!doctype html>", html.lower())
                self.assertIn('id="main"', html)
                self.assertIn('name="description"', html)
                self.assertIn("/Kenip/assets/css/static-site.css", html)
                self.assertNotIn(".php", html, "Static page links must not point to PHP routes")
                self.assertNotIn("<form", html.lower())
                self.assertNotIn("<script", html.lower())

    def test_root_publication_source(self):
        self.assert_site_root(ROOT)

    def test_docs_publication_source(self):
        self.assert_site_root(ROOT / "docs")

    def test_shared_stylesheet_and_site_maps_exist_in_both_sources(self):
        for site_root in [ROOT, ROOT / "docs"]:
            self.assertTrue((site_root / "assets/css/static-site.css").is_file())
            self.assertTrue((site_root / "robots.txt").is_file())
            self.assertTrue((site_root / "sitemap.xml").is_file())

if __name__ == "__main__":
    unittest.main()
