from .svg_engine import svg_start,finish_svg,text,rect,line
from .themes import get_theme
def generate(theme_name='midnight',density=1.0):
 t=get_theme(theme_name);p=svg_start(1200,620,'Connected technology architecture','Six conceptual technology layers.',t['background']);rows=[('Applications & product workflows','USER VALUE / BUSINESS RULES'),('AI / machine learning workloads','MODELS / INFERENCE'),('Software runtimes & APIs','COMPATIBILITY / OBSERVABILITY'),('Cloud & deployment infrastructure','NETWORK / STORAGE / SECURITY'),('Operating systems & resource management','MEMORY / SCHEDULING / DRIVERS'),('Compute hardware & accelerators','CPU / GPU / MEMORY / I/O')]
 for i,(a,b) in enumerate(rows):
  y=125+i*77;p.extend([rect(54,y,1092,58,t['panel'],t['line']),text(78,y+36,a,17,t['ink']),text(1110,y+35,b,12,t['muted'],'end')])
  if i<5:p.append(line(1000,y+58,1000,y+77,t['accent']))
 return finish_svg(p)