import os

data = r'some_data'

full_files = {}
for root, dirs, files in os.walk(data):
    for file in files:
        path = os.path.join(root, file)
        f_size = os.stat(path).st_size
        i = 1
        for _ in range(10):
            if i <= f_size < i * 10:
                if i in full_files:
                    full_files[i] += 1
                else:
                    full_files.setdefault(i, 1)
            i *= 10
print(full_files)
