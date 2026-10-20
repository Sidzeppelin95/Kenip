import unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class T(unittest.TestCase):
 def test_pages(self):
  for p in ['index.php','solutions.php','capabilities.php','technology.php','approach.php','about.php','contact.php','privacy.php','terms.php','404.php','work/index.php','work/category.php']:self.assertTrue((R/p).is_file())
 def test_no_forms_or_scripts(self):
  for p in R.rglob('*.php'):
   s=p.read_text().lower();self.assertNotIn('<script',s);self.assertNotIn('<form',s)
if __name__=='__main__':unittest.main()