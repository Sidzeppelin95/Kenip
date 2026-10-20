from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ("hero-network.svg", "technology-landscape.svg", "capability-map.svg", "delivery-process.svg")
SVG_NS = "{http://www.w3.org/2000/svg}"

def main():
    folder = ROOT / "assets" / "svg"
    for name in EXPECTED:
        path = folder / name
        if not path.is_file() or path.stat().st_size < 100:
            raise SystemExit(f"Missing or empty SVG asset: assets/svg/{name}")
        root = ET.parse(path).getroot()
        if root.tag != SVG_NS + "svg":
            raise SystemExit(f"Not an SVG document: assets/svg/{name}")
        if root.find(SVG_NS + "title") is None or root.find(SVG_NS + "desc") is None:
            raise SystemExit(f"SVG must include title and description: assets/svg/{name}")
    print("SVG/XML validation passed for all four original diagrams.")

if __name__ == "__main__":
    main()
