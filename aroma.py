dict_of_aroma_bonds, spTree, type_bond_gl = ({}, [], 0)
three_valencies = set()


def into_aroma_dict(start, finish, weight):
    global dict_of_aroma_bonds
    if start not in dict_of_aroma_bonds:
        dict_of_aroma_bonds[start] = {finish:weight}
    else:
        dict_of_aroma_bonds[start][finish] = weight
    if finish not in dict_of_aroma_bonds:
        dict_of_aroma_bonds[finish] = {start:weight}
    else:
        dict_of_aroma_bonds[finish][start] = weight
    #return dict_of_aroma_bonds

def create_sp_trees():
    global three_valencies, type_bond_gl, dict_of_aroma_bonds #, spTree
    '''print("three_valencies:", three_valencies, "type_bond_gl:",\
           type_bond_gl, "dict_of_aroma_bonds:", \
          dict_of_aroma_bonds, "spTree:", spTree, sep='\n')'''
    #num_of_spanning_trees = 0
    for atom in dict_of_aroma_bonds:
        if atom not in three_valencies:
            type_bond_gl = 0
            #spTree.append([])
            #print("spTree:\n", spTree)
            last_atom = dfs_aroma(atom) #, num_of_spanning_trees)
            type_bond_l = 2 - type_bond_gl % 2
            '''if type_bond_l == 2:
                print("Not aromatic")
                #FIX_ME : it's neсessary to exit with error!!!
            elif type_bond_l == 1:
                dict_of_aroma_bonds[atom][last_atom] = type_bond_l
                dict_of_aroma_bonds[last_atom][atom] = type_bond_l
            '''
            '''print("last_atom:\n", last_atom)
            print("dict_of_aroma_bonds: \n", dict_of_aroma_bonds)
            print("spTree:", spTree, "num_of_spanning_trees:", \
                  num_of_spanning_trees, sep='\n')'''
            #num_of_spanning_trees += 1
def dfs_aroma(atom): #, num_of_spanning_trees):
    global three_valencies, type_bond_gl, dict_of_aroma_bonds
    three_valencies.add(atom)
    '''print("call dfs_aroma()")
    print("atom:", atom, "three_valencies:", three_valencies, sep='\n')'''
    #spTree[num_of_spanning_trees].append(atom)
    #print(spTree)
    for near_atom in dict_of_aroma_bonds[atom]:
        '''print("dict_of_aroma_bonds[atom]:", dict_of_aroma_bonds[atom],\
              "near_atom:", near_atom, sep='\n')
        print(near_atom not in three_valencies)'''
        last_atom = near_atom
        if near_atom not in three_valencies:
            type_bond_l = 2 - type_bond_gl % 2
            #print("type_bond_gl, type_bond_l: ", type_bond_gl, type_bond_l)
            dict_of_aroma_bonds[atom][near_atom] = type_bond_l
            dict_of_aroma_bonds[near_atom][atom] = type_bond_l
            #why twice add, when list?
            #print("dict_of_aroma_bonds: \n", dict_of_aroma_bonds)
            type_bond_gl += 1
            last_atom = dfs_aroma(near_atom) #, num_of_spanning_trees)
    return last_atom 
    '''if len(three_valencies) == len(dict_of_aroma_bonds):
        for near_atom in dict_of_aroma_bonds[atom]:
            if len(dict_of_aroma_bonds[atom][near_atom]) == 1:
                print("fail")
                break
        cheque_fail.append(dict_of_aroma_bonds[atom][near_atom][1])
    if cheque_fail == [1, 1, 1]:
        print'''
        
