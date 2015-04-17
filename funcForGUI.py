def for_circle(x, y, radius):
    return [x-radius, y-radius, x+radius, y+radius]
#def create_line(list_of_coordinates):
    #canv.create_line(*list_of_coordinates, width=2)
#canv.create_line
def get_mol(mol):
    return mol
def g(num_atom1, num_atom2, type_svyaz, mol, canv, x_y_0, scale):
    atom1 = mol.atom_block[int(num_atom1)-1][:2]
    atom2 = mol.atom_block[int(num_atom2)-1][:2]
    svyaz = []
    svyaz.extend(atom1)
    svyaz.extend(atom2)
    #print(svyaz)
    for value in range(len(svyaz)):
        svyaz[value] *= scale
        svyaz[value] -= x_y_0[value%2]
        svyaz[value] += 250
    #print(svyaz)
    canv.create_line(*svyaz,width=2,tag=str(type_svyaz))
def k(svyaz, mol, canv, x_y_0, scale):
    g(*svyaz[:3], mol=mol, canv=canv, x_y_0=x_y_0, scale=scale)
def h(mol, canv, scale=50):
    sum_x, sum_y, num_x, num_y = (0, 0, 0, 0)
    for atom in mol.atom_block:
        sum_x += atom[0]
        num_x += 1
        sum_y += atom[1]
        num_y += 1
    x_0 = sum_x / num_x
    y_0 = sum_y / num_y
    x_y_0 = [x_0*scale, y_0*scale]
    print(x_y_0)
    
    for svyaz in mol.bond_block:
        k(svyaz, mol=mol, canv=canv, x_y_0=x_y_0, scale=scale)
    for atom in mol.atom_block:
        x_y = atom[:2]
        for value in range(len(x_y)):
            x_y[value] *= scale
            x_y[value] -= x_y_0[value]
            x_y[value] += 250
            '''sum_x += x_y[value]
            num_x += 1
            sum_y = atom[1]
            num_y += 1'''
        x_y_r=for_circle(*x_y, radius=7)
        canv.create_oval(*x_y_r, fill="lightyellow", outline="lightyellow")
        canv.create_text(*x_y,text=atom[3],font="Verdana 12",fill="red")

        

    
