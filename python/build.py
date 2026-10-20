"""Generate the site's static SVG illustrations."""
from pathlib import Path
from graphics.network import generate as network
from graphics.architecture import generate as architecture
from graphics.capability_map import generate as capability_map
from graphics.process_diagram import generate as process_diagram
ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/'assets'/'svg'
def main():
    OUTPUT.mkdir(parents=True,exist_ok=True)
    for filename,renderer in [('hero-network.svg',network),('technology-landscape.svg',architecture),('capability-map.svg',capability_map),('delivery-process.svg',process_diagram)]:
        (OUTPUT/filename).write_text(renderer()+'\n',encoding='utf-8')
        print(f'Generated {filename}')
if __name__=='__main__': main()
