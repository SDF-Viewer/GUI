mol_gl, canv_gl = (0, 0)

def for_circle(x, y, radius):
    return [x-radius, y-radius, x+radius, y+radius]

def into_center(scale):
    global mol_gl
    summa, num, x_y_0 = ([0, 0], [0, 0], [0, 0])
    for atom in mol_gl.atom_block:
        for i in 0, 1:
            summa[i] += atom[i]
            num[i] += 1
    for i in 0, 1:
        x_y_0[i] = summa[i] / num[i]
    for num_atom in range(len(mol_gl.atom_block)):
        atom = mol_gl.atom_block[num_atom]
        for i in 0, 1:
            atom[i] -= x_y_0[i]
            atom[i] *= scale
            atom[i] += 250
    
def g(num_atom1, num_atom2, type_svyaz):
    atom1 = mol_gl.atom_block[int(num_atom1)-1][:2]
    atom2 = mol_gl.atom_block[int(num_atom2)-1][:2]
    svyaz = []
    svyaz.extend(atom1)
    svyaz.extend(atom2)
    canv_gl.create_line(*svyaz,width=2,tag=str(type_svyaz))

def h(mol, canv, scale=50):
    sum_x, sum_y, num_x, num_y = (0, 0, 0, 0)
    global mol_gl, canv_gl
    import copy
    mol_gl = copy.deepcopy(mol)
    canv_gl = canv
    into_center(scale)
    for svyaz in mol_gl.bond_block:
        g(*svyaz[:3])
    for atom in mol_gl.atom_block:
        x_y = atom[:2]
        x_y_r = for_circle(*x_y, radius=7)
        canv_gl.create_oval(*x_y_r, fill="lightyellow", outline="lightyellow")
        canv_gl.create_text(*x_y, text=atom[3],font="Verdana 12",fill="red")

        

    
