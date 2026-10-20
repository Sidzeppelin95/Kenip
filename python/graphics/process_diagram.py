from .svg_engine import svg_start,finish_svg,text,line,rect
from .themes import get_theme
def generate(theme_name='midnight',density=1.0):
 t=get_theme(theme_name);p=svg_start(1200,300,'Five-step delivery process','Understand, architect, build, validate, and improve.',t['background']);items=[('Understand','Requirements & context',106,157),('Architect','Options & trade-offs',342,157),('Build','Agreed scope',578,157),('Validate','Evidence & checks',814,157),('Improve','Feedback & iteration',1072,200)]
 for i,(a,b,x,w) in enumerate(items):
  l=x-w/2;p.extend([rect(l,82,w,112,t['panel'],t['line']),text(l+16,106,f'{i+1:02d}',11,t['accent']),text(x,142,a,18,t['ink'],'middle','600'),text(x,165,b,10,t['muted'],'middle')])
  if i<4:p.append(line(x+w/2+4,137,items[i+1][2]-items[i+1][3]/2-4,137,t['accent']))
 return finish_svg(p)