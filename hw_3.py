"""
Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида:
'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка,
как привести их к корректному виду. Можно ли при этом не создавать новый список?
"""
employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
print(employees)
for elem in employees:
    name = elem[elem.rfind(' ') + 1:].title()
    employee_position = elem[:elem.rfind(' ')].capitalize()
    employees[employees.index(elem)] = f'{employee_position} {name}'
print(employees)
