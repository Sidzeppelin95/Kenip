from .geometry import radial_points
from .svg_engine import document,node
def generate():
 labels=["AI & INTELLIGENCE","SECURITY & TRUST","SYSTEMS & PERFORMANCE","CLOUD & SOFTWARE","DIGITAL INFRASTRUCTURE","AUTONOMOUS SYSTEMS","RESEARCH & EMERGING TECH"]
 points=radial_points(350,235,145,len(labels));body=[]
 for x,y in points:body.append(f'<path d="M350 235 L{x:.1f} {y:.1f}" stroke="#35505b" stroke-width="1.5"/>')
 body.append(node(350,235,"SYSTEMS ENGINEERING","Shared technical foundation",True,180))
 for i,((x,y),label) in enumerate(zip(points,labels)):body.append(node(x,y,label,accent=(i in (0,3)),width=152))
 return document(700,470,"Capability map","Seven engineering domains connected through a shared systems engineering foundation.",''.join(body))
