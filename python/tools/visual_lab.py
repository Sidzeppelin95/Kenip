from pathlib import Path
import sys,tkinter as tk
from tkinter import ttk,filedialog,messagebox
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'python'))
from graphics.network import generate as network
from graphics.architecture import generate as architecture
from graphics.capability_map import generate as capability
from graphics.process_diagram import generate as process
from graphics.svg_engine import write_svg
G={'Hero network':network,'Technology architecture':architecture,'Capability map':capability,'Delivery process':process}
def main():
 root=tk.Tk();root.title('SDS SVG Visual Lab');root.geometry('500x300');f=ttk.Frame(root,padding=24);f.pack(fill='both',expand=True);ttk.Label(f,text='SVG Visual Lab',font=('TkDefaultFont',18,'bold')).pack(anchor='w');kind=tk.StringVar(value='Hero network');theme=tk.StringVar(value='midnight');ttk.Combobox(f,textvariable=kind,values=list(G),state='readonly').pack(fill='x',pady=10);ttk.Combobox(f,textvariable=theme,values=['midnight','light'],state='readonly').pack(fill='x',pady=10)
 def export():
  p=filedialog.asksaveasfilename(defaultextension='.svg',filetypes=[('SVG','*.svg')])
  if p:
   try:write_svg(p,G[kind.get()](theme_name=theme.get()))
   except Exception as e:messagebox.showerror('Export failed',str(e));return
   messagebox.showinfo('Exported',p)
 ttk.Button(f,text='Generate and export…',command=export).pack(anchor='e',pady=12);root.mainloop()
if __name__=='__main__':main()