def float_one_dim_list(input_list):
    """Преобразует элементы однострочного списка в тип float,
    если возможно.

    Возвращает новый список
    """
    length = len(input_list)
    output_list = []
    for i in range(length):
        value = input_list[i]
        try:
            output_list.append(float(value))
        except ValueError:
            output_list.append(value)
    return output_list

def float_two_dim_list(input_list):
    """Преобразует элементы двустрочного списка в тип float,
    если возможно.

    Возвращает новый список. Работает некорректно, если поданный\
    список не организован как список списков: '[[],[],[]]'.
    """
    line_count = len(input_list)
    output_list = []

    for i in range(line_count):
        output_list.append(float_one_dim_list(input_list[i]))
    return output_list

def get_data_dict_from_string_list(input_string_list):
    """Конвертирует список строк полей в словарь полей.

    Возвращает словарь. Многострочные поля обрабатываются некорректно
    """
    output_dict = {}
    
    field_name = ''
    for line in input_string_list:
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
    return output_dict