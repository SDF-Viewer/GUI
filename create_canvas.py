from handlers import*
from molecule import*
from molecules_list import*
from module_ref import*
from tkinter import*


def create_canvas():
    root = Tk()
    canv = Canvas(root,width=500,height=500,bg="lightyellow",
                  cursor="pencil")
    canv.pack()
    file = open('sdf_list.sdf', 'tr')
    lm = extract_molecules_list_from_sdf(file, 'Source')
    file.close()
    mol=lm.mol_list[29]
    draw_mol(mol, canv)   
    root.mainloop()
create_canvas()
