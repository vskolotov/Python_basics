import sys

param = sys.argv[1:]
edit_idx = int(param[0]) - 1
new_val = param[1].strip()
cursor_position = 0
s = ''
with open('bakery.csv', 'r+', encoding='utf-8') as f:
    for i in range(edit_idx):
        line = f.readline()
        cursor_position = f.tell()
    line = f.readline()
    if line:
        for _ in range(len(line)):
            s += ' '
        f.seek(cursor_position)
        f.writelines(f'{s}')
        f.seek(cursor_position)
        f.writelines(f'{new_val}')
    else:
        print('not lines with this number')
