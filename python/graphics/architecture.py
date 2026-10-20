from .svg_engine import document,node
def generate():
 labels=[("APPLICATIONS","Products · APIs"),("AI & INTELLIGENCE","Models · inference"),("RUNTIMES","Services · libraries"),("CLOUD & INFRASTRUCTURE","Compute · networking"),("OPERATING SYSTEMS","Processes · resources"),("HARDWARE","CPU · GPU · devices")]
 body=[]
 for i,(title,sub) in enumerate(labels):
  y=58+i*66;body.append(node(350,y,title,sub,accent=(i in (0,1)),width=370))
  if i<5:body.append(f'<path d="M350 {y+25} V{y+40}" stroke="#67d5f4" stroke-width="1.5"/><path d="M345 {y+35} l5 5 5 -5" fill="none" stroke="#67d5f4"/>')
 return document(700,450,"Technology landscape","Layered view of applications, AI, runtimes, infrastructure, operating systems, and hardware.",''.join(body))
