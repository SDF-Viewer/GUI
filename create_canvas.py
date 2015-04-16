from handlers import*
from molecule import*
from molecules_list import*
from funcForGUI import*
from tkinter import*


def create_canvas():
    root = Tk()
    canv = Canvas(root,width=500,height=500,bg="lightblue",
                  cursor="pencil")
    canv.pack()
    file = open('sdf_list.sdf', 'tr')
    lm = extract_molecules_list_from_sdf(file, 'Source')
    file.close()
    mol=lm.mol_list[30]
    h(mol)
        
    root.mainloop()
