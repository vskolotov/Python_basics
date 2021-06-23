class IsNotNumberError(Exception):
    def __str__(self):
        return 'это не число'


my_list = []

while True:
    try:
        inp_data = input('Введите число: ')
        if inp_data.lower() == 'stop':
            break
        if inp_data.isdigit():
            my_list.append(int(inp_data))
        elif inp_data[:1] == '-' and inp_data[1:].isdigit():
            my_list.append(int(inp_data))
        else:
            raise IsNotNumberError()
    except IsNotNumberError as err:
        print(err)
print(my_list)
