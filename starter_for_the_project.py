import os

dir_names = ('my_project_2', 'settings', 'mainapp', 'adminapp', 'authapp')
for _ in range(1, len(dir_names)):
    dir_path = os.path.join(dir_names[0], dir_names[_])
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
