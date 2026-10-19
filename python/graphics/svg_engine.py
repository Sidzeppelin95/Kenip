from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET
def svg_start(w,h,title,description,background='#111b22'): return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',f'<title id="title">{escape(title)}</title>',f'<desc id="desc">{escape(description)}</desc>',f'<rect width="{w}" height="{h}" fill="{escape(background,quote=True)}"/>']
def text(x,y,v,size=14,fill='#f0fbfd',anchor='start',weight='400'): return f'<text x="{x}" y="{y}" fill="{escape(fill,quote=True)}" font-family="Arial,sans-serif" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}">{escape(v)}</text>'
def line(x1,y1,x2,y2,stroke='#66d7ee',opacity=.5,width=1.5): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-opacity="{opacity}" stroke-width="{width}"/>'
def rect(x,y,w,h,fill,stroke='#5a98aa'): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}"/>'
def finish_svg(parts):
 s=''.join(parts+['</svg>']);ET.fromstring(s);return s+'\n'
def write_svg(path,content):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content,encoding='utf-8');ET.parse(p)