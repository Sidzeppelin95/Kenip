import sys,unittest,xml.etree.ElementTree as ET
from pathlib import Path
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'python'))
from graphics.network import generate as n
from graphics.architecture import generate as a
from graphics.capability_map import generate as c
from graphics.process_diagram import generate as p
class T(unittest.TestCase):
 def test_generated_svg(self):
  for g in (n,a,c,p):
   x=ET.fromstring(g());self.assertIsNotNone(x.find('{http://www.w3.org/2000/svg}title'));self.assertIsNotNone(x.find('{http://www.w3.org/2000/svg}desc'))
if __name__=='__main__':unittest.main()