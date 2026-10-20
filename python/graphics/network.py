from .svg_engine import document,node
def generate():
 nodes=[(160,95,"APPLICATIONS"),(355,70,"AI / INFERENCE"),(550,95,"CLOUD"),(160,250,"SECURITY"),(355,250,"SYSTEMS"),(550,250,"PERFORMANCE"),(355,390,"AUTONOMY")]
 edges=[]
 for a,b in [(0,1),(1,2),(0,3),(0,4),(1,4),(2,5),(3,4),(4,5),(4,6),(5,6),(2,4)]:
  x1,y1,*_=nodes[a];x2,y2,*_=nodes[b]
  edges.append(f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="#42606c" stroke-width="1.4"/><circle cx="{(x1+x2)/2}" cy="{(y1+y2)/2}" r="3" fill="#67d5f4"/>')
 body=''.join(edges)+''.join(node(x,y,label,accent=(i in (1,4))) for i,(x,y,label) in enumerate(nodes))
 return document(710,465,"Connected engineering network","Relationships between applications, AI, cloud, security, systems, performance, and autonomy.",body)
