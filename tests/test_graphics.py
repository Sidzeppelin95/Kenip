import sys,unittest,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'python'))
from graphics.network import generate as network
from graphics.architecture import generate as architecture
from graphics.capability_map import generate as capability_map
from graphics.process_diagram import generate as process_diagram
class GraphicsTests(unittest.TestCase):
 def test_generators_return_accessible_svg(self):
  for fn in [network,architecture,capability_map,process_diagram]:
   with self.subTest(generator=fn.__module__):
    root=ET.fromstring(fn());self.assertTrue(root.tag.endswith('svg'));self.assertTrue(any(n.attrib.get('id')=='svg-title' for n in root.iter()))
 def test_build_outputs_exist(self):
  for name in ['hero-network.svg','technology-landscape.svg','capability-map.svg','delivery-process.svg']:self.assertTrue((ROOT/'assets/svg'/name).is_file(),name)
if __name__=='__main__':unittest.main()
