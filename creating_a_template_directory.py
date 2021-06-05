import os
import shutil

data = 'my_project'
find_dir = 'templates'
path_new_dir = os.path.join(data, find_dir)
for root, dirs, files in os.walk(data):
    if not os.path.exists(path_new_dir):
        os.makedirs(path_new_dir)
    for dir_ in dirs:
        if dir_ == find_dir:
            list_dir = os.listdir(os.path.join(root, find_dir))
            path_copy_dir = os.path.join(os.path.join(root, find_dir), f'{list_dir[0]}')
            path_new_dir = os.path.join(os.path.join(data, find_dir), f'{list_dir[0]}')
            shutil.copytree(path_copy_dir, path_new_dir)
