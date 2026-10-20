from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ["index.html", "solutions/index.html", "work/index.html", "capabilities/index.html", "technology/index.html", "approach/index.html", "about/index.html", "contact/index.html", "privacy/index.html", "terms/index.html", "404.html"]

class StaticPagesTests(unittest.TestCase):
    def test_github_pages_entrypoint_exists(self):
        self.assertTrue((ROOT / "index.html").is_file())
        self.assertTrue((ROOT / "index.html").read_text(encoding="utf-8").lstrip().lower().startswith("<!doctype html>"))

    def test_all_static_routes_are_real_html(self):
        for relative in PAGES:
            with self.subTest(page=relative):
                page = ROOT / relative
                self.assertTrue(page.is_file(), f"Missing static page: {relative}")
                html = page.read_text(encoding="utf-8")
                self.assertIn("<!doctype html>", html.lower())
                self.assertIn('id="main"', html)
                self.assertIn('name="description"', html)
                self.assertIn("/Kenip/assets/css/static-site.css", html)
                self.assertNotIn(".php", html, "Static page links must not point to PHP routes")
                self.assertNotIn("<form", html.lower())
                self.assertNotIn("<script", html.lower())

    def test_shared_stylesheet_and_site_maps_exist(self):
        self.assertTrue((ROOT / "assets/css/static-site.css").is_file())
        self.assertTrue((ROOT / "robots.txt").is_file())
        self.assertTrue((ROOT / "sitemap.xml").is_file())

if __name__ == "__main__":
    unittest.main()
