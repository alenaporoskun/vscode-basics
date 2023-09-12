import os
import glob
import shutil
from pathlib import Path


source = 'C:/Users/Admin/Downloads/TRASH'

if os.path.exists('C:/Users/Admin/Downloads/TRASH/moved') == False:
    os.mkdir(os.path.join(source, './moved'))

destination = 'C:/Users/Admin/Downloads/TRASH/moved'
#
# gather all files
allfiles = os.listdir(source)
print("\nFiles to move", allfiles, '\n')
 
# iterate on all files to move them to destination folder
for f in allfiles:
    if Path(f).is_dir():
        print(f, ' - папка')
    else:
        # iterate on all files to move them to destination folder
        print(f, ' - файл')
        src_path = os.path.join(source, f)
        dst_path = os.path.join(destination, f)
        shutil.move(src_path, dst_path)