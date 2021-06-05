import os


def create_dir(path, string):
    dir_path = os.path.join(path, string.strip())
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


pattern = ' '
with open('config.yml', 'r') as f:
    root = f.readline()[:-1]
    if not os.path.exists(root):
        os.mkdir(root)
    for line in f:
        line = line[:-1]
        file_extension = line.count('.') == 1

        if line.count(pattern) == 2 and not file_extension:
            level_1 = create_dir(root, line)
        if line.count(pattern) == 2 and file_extension:
            f = open(os.path.join(root, line.strip()), 'w', encoding='utf-8')
            f.close()

        if line.count(pattern) == 4 and not file_extension:
            level_2 = create_dir(level_1, line)
        if line.count(pattern) == 4 and file_extension:
            f = open(os.path.join(level_1, line.strip()), 'w', encoding='utf-8')
            f.close()

        if line.count(pattern) == 6 and not file_extension:
            level_3 = create_dir(level_2, line)
        if line.count(pattern) == 6 and file_extension:
            f = open(os.path.join(level_2, line.strip()), 'w', encoding='utf-8')
            f.close()

        if line.count(pattern) == 8 and not file_extension:
            level_4 = create_dir(level_3, line)
        if line.count(pattern) == 8 and file_extension:
            f = open(os.path.join(level_3, line.strip()), 'w', encoding='utf-8')
            f.close()
