import os
import shutil
from pathlib import Path

def main():

    paths_from = 'C:/Users/Admin/Downloads/TRASH'
    #fun_trying(paths_from)

    print(fun_IMAGE(paths_from))


def fun_IMAGE(paths_from):
    
    paths_to = os.path.join('C:/Users/Admin/Downloads/TRASH', 'IMAGE')

    if os.path.exists(paths_to) == False:
        os.mkdir(paths_to)

    for file in os.listdir(paths_from):
        print(file)

        if file != 'IMAGE' and Path(file).suffix.upper() in ('.JPEG', '.PNG', '.JPG', '.SVG'):
                print('name of file: ', file, '- image')
                path_join = os.path.join(paths_from, file)
                print('path_join: ', path_join, '\n')
                shutil.copy2(path_join, paths_to)
                #shutil.move(path_join, paths_to)
                return True

        if os.path.isdir(f'{paths_from}/{file}') and file != 'IMAGE':

            dirContents = os.listdir(f'{paths_from}/{file}')
            if not dirContents and file != 'IMAGE':
                print(f'{file} is empty')
                os.rmdir(f'{paths_from}/{file}')
            else:
                print(f'{file} not empty')
                return fun_IMAGE(f'{paths_from}/{file}')
                

def fun_trying(paths_from):

    #paths_from = 'C:/Users/Admin/Downloads/TRASH'

    paths_to = os.path.join('C:/Users/Admin/Downloads/TRASH', 'moved')

    if os.path.exists(paths_to) == False:
        os.mkdir(paths_to)

    #paths_to = 'C:/Users/Admin/Downloads/TRASH/moved'

    for file in os.listdir(paths_from):
        if file != 'moved':
            print('name of file: ', file)
            path_join = os.path.join(paths_from, file)
            print('path_join: ', path_join, '\n')
            #shutil.copy2(path_join, paths_to)
            shutil.move(path_join, paths_to)



if __name__ == '__main__':
 
    main()