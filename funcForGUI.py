def for_circle(x, y, radius):
    return [x-radius, y-radius, x+radius, y+radius]
#def create_line(list_of_coordinates):
    #canv.create_line(*list_of_coordinates, width=2)
#canv.create_line
def get_mol(mol):
    return mol
def g(num_atom1, num_atom2, type_svyaz, mol):
    atom1 = mol.atom_block[num_atom1][:2]
    atom2 = mol.atom_block[num_atom2][:2]
    svyaz = []
    svyaz.extend(atom1)
    svyaz.extend(atom2)
    canv.create_line(*svyaz,width=2,tag=str(type_svyaz))
def k(svyaz, mol):
    g(*svyaz[:3], mol=mol)
def h(mol):
    for svyaz in mol.bond_block:
        k(svyaz, mol=mol)
    for atom in mol.atom_block:
        x_y = atom[:2]
        x_y_r=for_circle(*x_y, radius=2)
        canv.create_oval(*x_y_r, fill="white", outline="white")
        canv.create_text(x_y,atom[3])

        
        
    
