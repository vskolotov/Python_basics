import sys

param = sys.argv[1:]
if len(param) == 0:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())
if len(param) == 1:
    start_idx = int(param[0]) - 1
    count = 0
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if count >= start_idx:
                print(line.strip())
            count += 1
if len(param) == 2:
    start_idx = int(param[0]) - 1
    end_idx = int(param[1])
    count = 0
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if start_idx <= count < end_idx:
                print(line.strip())
            count += 1
