from pathlib import Path
import sys
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'python'))
from graphics.network import generate as n
from graphics.architecture import generate as a
from graphics.capability_map import generate as c
from graphics.process_diagram import generate as p
from graphics.svg_engine import write_svg
def main():
 for name,fn in [('hero-network.svg',n),('technology-landscape.svg',a),('capability-map.svg',c),('delivery-process.svg',p)]:write_svg(R/'assets/svg'/name,fn());print('generated',name)
if __name__=='__main__':main()