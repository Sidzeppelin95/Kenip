from .svg_engine import document,node
def generate():
 labels=["UNDERSTAND","ARCHITECT","BUILD","VALIDATE","IMPROVE"];body=[];xs=[90,220,350,480,610]
 for i,(x,label) in enumerate(zip(xs,labels)):
  body.append(node(x,160,label,accent=(i==2),width=112))
  if i<4:body.append(f'<path d="M{x+58} 160 H{xs[i+1]-60}" stroke="#67d5f4" stroke-width="1.5"/><path d="M{xs[i+1]-65} 155 l5 5 -5 5" fill="none" stroke="#67d5f4"/>')
 body.append('<path d="M610 193 V245 H90 V193" fill="none" stroke="#35505b" stroke-dasharray="5 5"/><text x="350" y="270" fill="#9db1bb" font-size="12" text-anchor="middle">Feedback informs the next iteration</text>')
 return document(700,315,"Delivery process","Five-stage iterative process: understand, architect, build, validate, and improve.",''.join(body))
