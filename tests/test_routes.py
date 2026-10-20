import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class RouteStructureTests(unittest.TestCase):
    def test_all_page_templates_exist_in_the_precreated_directories(self):
        pages = (
            "Website/index.php", "Website/solutions.php", "Website/capabilities.php",
            "Website/technology.php", "Website/approach.php", "Website/about.php",
            "Website/contact.php", "Website/privacy.php", "Website/terms.php",
            "Website/404.php", "Work/index.php", "Work/categories.php",
        )
        for relative in pages:
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file())
                self.assertGreater((ROOT / relative).stat().st_size, 100)

    def test_existing_site_configuration_is_not_a_placeholder(self):
        self.assertGreater((ROOT / "Includes/bootstrap.php").stat().st_size, 100)
        self.assertTrue((ROOT / ".htaccess").is_file())

if __name__ == "__main__":
    unittest.main()
