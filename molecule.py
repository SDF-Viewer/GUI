from handlers import *

class Molecule:
    """Класс молекула

    Содержит информацию об одной молекуле, дублирует кусок SDF
    """
    
    header_list = []
    #название, etc информация, комментарий
    counts_line = []
    #состоит из строковых! значений counts_line sdf
    atom_block_list = []
    #float двумерная матрица, в 4 столбце string - обозначение атома 
    bond_block_list = []
    #float двумерная матрица
    associated_data_dict = {}
    #словарь списков, каждый список - строчка поля в sdf (бывают многострочные поля)
    
    def get_atom_count(self):
        """Возвращает количество атомов в молекуле
        """
        return int(self.counts_line[0])
    def get_bond_count(self):
        """Возвращает количество связей в молекуле
        """
        return int(self.counts_line[1])

def extract_molecule_by_string(input_string):
    """Преобразует кусок sdf в класс Molecule

    Возвращает экземпляр класса
    """
    #сплит на список строк, заполнение экземпляра класса
    string_lines_list = input_string.splitlines()

    header_list = string_lines_list[:3]
    counts_line = string_lines_list[3].split() 

    OutputMolecule = Molecule()
    OutputMolecule.header_list = header_list
    OutputMolecule.counts_line = counts_line

    atom_count = OutputMolecule.get_atom_count()
    atom_block_string_list = string_lines_list[4 : 4 + atom_count]
    for i in range(atom_count):
        line = atom_block_string_list[i]
        line = line.split()
        atom_block_string_list[i] = line
    atom_block = float_two_dim_list(atom_block_string_list)

    OutputMolecule.atom_block = atom_block

    bond_count = OutputMolecule.get_bond_count()
    bond_block_string_list = string_lines_list[4 + atom_count : 4 + atom_count + bond_count]
    for i in range(bond_count):
        line = bond_block_string_list[i]
        line = line.split()
        bond_block_string_list[i] = line
    bond_block = float_two_dim_list(bond_block_string_list)

    OutputMolecule.bond_block = bond_block
    
    associated_data_string_list = string_lines_list[5 + atom_count + bond_count : ]    
    associated_data_dict = get_data_dict_from_string_list(associated_data_string_list)

    OutputMolecule.associated_data_dict = associated_data_dict
    
    return OutputMolecule
