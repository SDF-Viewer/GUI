from molecule import *

class MoleculesList:
    """Список молекул
    """
    
    mol_list = []
    """Список экземпляров класса Molecule
    """
    name = ''

    def __init__(self, name):
        """Конструктор класса
        """
        self.name = name
    
    def append_molecule(self, molecule_copy):
        """Добавляет новый экземпляр класса Molecule в конец списка self.mol_list
        """
        self.mol_list.append(molecule_copy)
    

def extract_molecules_list_from_sdf(file, name):
    """Преобразует sdf в класс MoleculeList

    Возвращет экземпляр класса 'Cписок молекул' по sdf. В случае пустого/не sdf возвращает None.
    """
    file_as_string = file.read()
    molecules_count = file_as_string.count('\n$$$$\n')
    if molecules_count != 0:
        OutputClass = MoleculesList(name)
        string_list = file_as_string.split('\n$$$$\n', molecules_count)
        #рассплитили на строчки с информацией об отдельной молекуле
        for molecule_string in string_list:
            molecule_copy = extract_molecule_by_string(molecule_string)
            #получаем экземпляр класса Molecule
            OutputClass.append_molecule(molecule_copy) 
        return OutputClass
    else:
        return None
