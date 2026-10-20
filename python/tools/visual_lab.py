"""Optional Tkinter utility for previewing/exporting generated SVG diagrams."""
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'python'))
from graphics.network import generate as network
from graphics.architecture import generate as architecture
from graphics.capability_map import generate as capability_map
from graphics.process_diagram import generate as process_diagram
GENERATORS={"Hero network":network,"Technology landscape":architecture,"Capability map":capability_map,"Delivery process":process_diagram}
def main():
    root=tk.Tk();root.title("SVG Visual Lab");root.geometry("540x250");root.minsize(420,220)
    selected=tk.StringVar(value="Hero network")
    ttk.Label(root,text="Diagram",font=("TkDefaultFont",12,"bold")).pack(anchor="w",padx=18,pady=(18,6))
    ttk.Combobox(root,textvariable=selected,values=list(GENERATORS),state="readonly").pack(fill="x",padx=18)
    ttk.Label(root,text="Generate an SVG using the shared Python graphics engine.").pack(anchor="w",padx=18,pady=12)
    def export():
        path=filedialog.asksaveasfilename(defaultextension=".svg",filetypes=[("SVG image","*.svg")],initialfile=selected.get().lower().replace(" ","-")+".svg")
        if not path:return
        try:Path(path).write_text(GENERATORS[selected.get()]()+"\n",encoding="utf-8")
        except OSError as exc:messagebox.showerror("Export failed",str(exc));return
        messagebox.showinfo("SVG exported",f"Saved {path}")
    ttk.Button(root,text="Generate and export SVG",command=export).pack(anchor="w",padx=18,pady=8)
    root.mainloop()
if __name__=="__main__":main()
