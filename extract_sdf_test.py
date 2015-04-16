from molecules_list import *

file = open('sdf_list.sdf', 'tr')

#molec_list = extract_molecules_list_from_sdf(file, 'Source')

#s = file.read()
#print(s.count('$$$$'))
lm = extract_molecules_list_from_sdf(file, 'Source')
file.close()

for cl in lm.mol_list:
    print(cl.associated_data_dict, '\n------')
'''
input_string = '> <A>\n1\n\n> <B>\n3\n\n'
input_string = input_string.splitlines()
output_dict = {}

field_name = ''
for line in input_string:
        if len(line) != 0:
            if line[0] == '>':
                start = line.find('<')
                end = line.rfind('>')
                field_name = line[start + 1 : end]
                output_dict[field_name] = []
            elif field_name != '':
                output_dict[field_name].append(line)
for field in output_dict:
    output_dict[field] = float_one_dim_list(output_dict[field])
'''
