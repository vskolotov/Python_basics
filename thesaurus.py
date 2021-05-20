"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:
 thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?
4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
«Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
Например:
 thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": "Петр Алексеев"
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Сможете ли вы вернуть отсортированный по ключам словарь?
"""


def thesaurus(*args):
    """
    the function creates a dictionary from a list of words. The key is the first letter of the word.
    :param args: type: str

    """
    dict_of_names = {}
    names = list(args)
    names.sort()
    for el in names:
        key = el[0]
        if key in dict_of_names.keys():
            dict_of_names[key].append(el)
        else:
            dict_of_names[key] = [el]
    for k, v in dict_of_names.items():
        print(f'{k}: {v}')


def thesaurus_adv(*args):
    """
    the function receives a list of names and surnames as input.
    A dictionary is created with a key for the first letter of the last name,
    in which a dictionary with a key for the first letter of the first name is created.
    :param args:
    """
    dict_of_surname = {}
    temp_list = []
    full_names = list(args)
    # попытка сортировки по фамилиям
    for el in full_names:
        temp_list.append(f'{el.split()[-1]} {el.split()[0]}')
    temp_list.sort()
    full_names.clear()
    for el in temp_list:
        full_names.append(f'{el.split()[-1]} {el.split()[0]}')

    for full_name in full_names:
        key = full_name.split()[-1][0]
        dict_of_surname.setdefault(key, {full_name[0]: []})

    for key, val in dict_of_surname.items():
        for full_name in full_names:
            if full_name[0] in val.keys() and full_name.split()[-1][0] == key:
                val[full_name[0]].append(full_name)
            elif full_name.split()[-1][0] == key:
                val[full_name[0]] = [full_name]
    for k, v in dict_of_surname.items():
        print(f'{k}: {v}')


thesaurus("Иван", "Мария", "Петр", "Илья", "Дима", "Ирина", "Андрей", "Аркадий")
print('-------')
thesaurus_adv("Иван Сергеев", "Ярослав Анисимов", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")


