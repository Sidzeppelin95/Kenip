from pathlib import Path
import xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1]
def main():
 for p in (R/'assets/svg').glob('*.svg'):ET.parse(p)
 print('SVG/XML validation passed.')
if __name__=='__main__':main()