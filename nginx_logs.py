def find_ip(string):
    stat_idx = 0
    end_idx = string.find(' - - ')
    return string[stat_idx:end_idx]


def request_type(string):
    stat_idx = string.find('"') + 1
    end_idx = string.find(' /')
    return string[stat_idx:end_idx]


def requested_resource(string):
    stat_idx = string.find(' /') + 1
    end_idx = string.find(' HTTP')
    return string[stat_idx:end_idx]


def find_spamer(list_ip):
    dict_ip = {}
    count = 1
    for ip in list_ip:
        if ip in dict_ip:
            value = dict_ip[ip]
            value += 1
            dict_ip[ip] = value
        else:
            dict_ip.setdefault(ip, count)
    max_req = 0
    for key, val in dict_ip.items():
        if val > max_req:
            max_req = val
            spamer = key
    return spamer, max_req


remote_addr = []
parser_list = []
with open('nginx_logs.txt', 'r') as f:
    for line in f:
        parser_list.append((find_ip(line[:-1]), request_type(line[:-1]), requested_resource(line[:-1])))
        remote_addr.append(find_ip(line[:-1]))

print(find_spamer(remote_addr))

with open('parser_list.txt', 'w') as f:
    for el in parser_list:
        f.write(str(f'{el}\n'))
