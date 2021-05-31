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


def find_spamer(dictionary_ip):
    max_req = 0
    for key, val in dictionary_ip.items():
        if val > max_req:
            max_req = val
            spamer = key
    return spamer, max_req


dict_ip = {}
with open('nginx_logs.txt', 'r') as f:
    for line in f:
        data = find_ip(line[:-1]), request_type(line[:-1]), requested_resource(line[:-1])
        with open('parser_list.txt', 'a') as nf:
            nf.write(str(f'{data}\n'))
        ip = find_ip(line[:-1])
        count = 1
        if ip in dict_ip:
            value = dict_ip[ip]
            value += 1
            dict_ip[ip] = value
        else:
            dict_ip.setdefault(ip, count)

print(find_spamer(dict_ip))
