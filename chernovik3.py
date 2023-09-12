import os
import shutil
from pathlib import Path

paths_from = 'C:/Users/Admin/Downloads/TRASH'

if os.path.exists('C:/Users/Admin/Downloads/TRASH/moved') == False:
    os.mkdir(os.path.join(paths_from, 'moved'))

paths_to = 'C:/Users/Admin/Downloads/TRASH/moved'

for file in os.listdir(paths_from):
    if file != 'moved':
        print('name of file: ', file)
        path_join = os.path.join(paths_from, file)
        print('path_join: ', path_join, '\n')
        #shutil.copy2(path_join, paths_to)
        shutil.move(path_join, paths_to)
