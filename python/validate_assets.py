"""Validate generated SVGs as well-formed XML with accessible labels."""
import xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=['hero-network.svg','technology-landscape.svg','capability-map.svg','delivery-process.svg']
def main():
    for name in REQUIRED:
        path=ROOT/'assets'/'svg'/name
        if not path.is_file():raise SystemExit(f'Missing SVG: {path.relative_to(ROOT)}')
        try:root=ET.parse(path).getroot()
        except ET.ParseError as exc:raise SystemExit(f'Invalid SVG {name}: {exc}') from exc
        if not root.tag.endswith('svg'):raise SystemExit(f'{name} root is not svg')
        ids={node.attrib.get('id') for node in root.iter() if node.attrib.get('id')}
        if not {'svg-title','svg-desc'}<=ids:raise SystemExit(f'{name} is missing accessible title/description')
    print(f'Validated {len(REQUIRED)} accessible SVG files.')
if __name__=='__main__':main()
