#from dfs import* 
mol_gl, canv_gl,  = (0, 0)
from aroma import*
#three_valencies = set()


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
            
'''def callFriends(vertex):
    three_valencies.add(vertex)
    for friend in dict_of_aroma_bonds[vertex]:
        if friend not in three_valencies:
            weight=dict_of_aroma_bonds[vertex][friend]
            start=vertex
            finish=friend
            if start not in spTree:
                spTree[start] = {finish:weight}
            else:
                spTree[start][finish] = weight
            if finish not in spTree:
                spTree[finish] = {start:weight}
            else:
                spTree[finish][start] = weight
            callFriends(friend)
'''
def dfs_aroma(atom):
    
    pass

def draw_aroma_bonds():
    #print("draw_aroma_bonds works")
    pass

def double_line(bond, ro=1):
    import math
    dist = 2
    double_bond = [[0 for i in range(4)] for j in [0, 1]]
    dist *= ro
    k_znam = bond[2] - bond[0]
    if k_znam == 0:
        almost_x_y = [dist, 0]
    else:
        k = (bond[3] - bond[1]) / k_znam
        sign_k = k / abs(k)
        k *= k
        almost_x_y = [dist/math.sqrt(1/k + 1), -dist/math.sqrt(k + 1)*sign_k]
    for bond_i in [0, 1]:
        for coord_i in [0, 1, 2, 3]:
            double_bond[bond_i][coord_i] = (2*bond_i - 1) * almost_x_y[coord_i%2] + bond[coord_i]
    for i in [0, 1]:
        canv_gl.create_line(*double_bond[i],width=2,tag=str(bond[4]))
 
def draw_bond(num_atom1, num_atom2, type_bond):
    ro = 3
    atom1 = mol_gl.atom_block[int(num_atom1)-1][:2]
    atom2 = mol_gl.atom_block[int(num_atom2)-1][:2]
    bond = []
    bond.extend(atom1)
    bond.extend(atom2)
    bond.append(type_bond)
    if type_bond == 1:
        canv_gl.create_line(*bond[:4],width=2,tag=str(type_bond))
    elif type_bond == 2:
        double_line(bond)
    elif type_bond == 3:
        double_line(bond, ro=ro)
        canv_gl.create_line(*bond[:4],width=2,tag=str(type_bond))
    else:
        canv_gl.create_line(*bond[:4],width=2,tag=str(type_bond), fill="red")
'''def printAsListOfArcs(tree):
    for start in tree:
        for finish in tree[start]:
            print(start, finish, tree[start][finish])'''
'''def jk():
    dict_of_aroma_bonds = into_aroma_dict()
    three_valencies = set()
    spTree = {}
    numOfComp = 0
    for key in dict_of_aroma_bonds:
        if key in called:
            continue
        else:
            callFriends(key)
            printAsListOfArcs(spTree)
            spTree = {}
            print()
            numOfComp += 1
        

    print("Number of components:",numOfComp)
'''
def draw_mol(mol, canv, scale=50):
    #sum_x, sum_y, num_x, num_y = (0, 0, 0, 0)
    global mol_gl, canv_gl, dict_of_aroma_bonds
    import copy
    mol_gl = copy.deepcopy(mol)
    canv_gl = canv
    into_center(scale)
    for num_bond in range(len(mol_gl.bond_block)):
        bond = mol_gl.bond_block[num_bond][:3]
        if bond[2] == 4:
            #bond[2] = [num_bond]
            bond[2] = 7
            into_aroma_dict(*bond)
        else:
            draw_bond(*bond)
    create_sp_trees()
    for atom in dict_of_aroma_bonds:
        for near_atom in dict_of_aroma_bonds[atom]:
            bond = [atom, near_atom, dict_of_aroma_bonds[atom][near_atom]]
            draw_bond(*bond)
    print("dict_of_aroma_bonds:\n", dict_of_aroma_bonds)
    '''if dict_of_aroma_bonds != []:
        for atom in dict_of_aroma_bonds:
            dfs_aroma(atom)
            draw_aroma_bonds()
    '''   
    for atom in mol_gl.atom_block:
        x_y = atom[:2]
        x_y_r = for_circle(*x_y, radius=7)
        canv_gl.create_oval(*x_y_r, fill="lightyellow", outline="lightyellow")
        canv_gl.create_text(*x_y, text=atom[3],font="Verdana 12",fill="red")

