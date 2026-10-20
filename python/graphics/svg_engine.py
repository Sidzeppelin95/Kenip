"""Small, dependency-free SVG document helpers."""
from xml.sax.saxutils import escape
def document(width,height,title,description,body,background="#111a20"):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="svg-title svg-desc"><title id="svg-title">{escape(title)}</title><desc id="svg-desc">{escape(description)}</desc><defs><linearGradient id="accent-gradient" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#67d5f4"/><stop offset="1" stop-color="#4c9ebd"/></linearGradient><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M 32 0 L 0 0 0 32" fill="none" stroke="#35505b" stroke-opacity=".24" stroke-width="1"/></pattern></defs><rect width="100%" height="100%" fill="{background}"/><rect width="100%" height="100%" fill="url(#grid)"/>{body}</svg>'''
def node(x,y,label,subtitle="",accent=False,width=150):
 from xml.sax.saxutils import escape
 stroke="#67d5f4" if accent else "#35505b";fill="#182932" if accent else "#142127"
 size=9 if len(label)>19 else 11
 title_y=y-3 if subtitle else y+4
 sub=f'<text x="{x}" y="{y+15}" fill="#9db1bb" font-size="9" text-anchor="middle">{escape(subtitle)}</text>' if subtitle else ''
 return f'<g><rect x="{x-width/2}" y="{y-24}" width="{width}" height="48" rx="2" fill="{fill}" stroke="{stroke}"/><text x="{x}" y="{title_y}" fill="#e8f1f4" font-size="{size}" font-weight="600" text-anchor="middle">{escape(label)}</text>{sub}</g>'
