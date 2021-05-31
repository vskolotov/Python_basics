import json

dict_user_hobby = {}
full_name = []
with open('users.csv', 'r') as users:
    with open('hobby.csv', 'r') as hobby:
        name = [line[:-1].split(';') for line in users]
        hob = [line[:-1].split(';') for line in hobby]
        if len(name) >= len(hob):
            for _ in range(len(name)):
                full_name.append(f'{name[_][0]} {name[_][1]} {name[_][2]}')
            for _ in range(len(full_name)):
                if _ < len(hob):
                    dict_user_hobby.setdefault(full_name[_], hob[_])
                else:
                    dict_user_hobby.setdefault(full_name[_], None)
            with open('user_hobby.txt', 'w', encoding='utf-8') as f:
                f.write(json.dumps(dict_user_hobby, ensure_ascii=False))
        else:
            exit(1)
