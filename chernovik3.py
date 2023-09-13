import os
import shutil
from pathlib import Path

def main():

    paths_from = 'C:/Users/Admin/Downloads/TRASH'
    #fun_trying(paths_from)

    print('\n', fun_images(paths_from), '\n')
    print('\n', fun_documents(paths_from), '\n')


def fun_images(paths_from):
    
    list_images = []

    paths_to = os.path.join('C:/Users/Admin/Downloads/TRASH', 'images')
    if os.path.exists(paths_to) == False:
        os.mkdir(paths_to)

    print('os.listdir(paths_from):\n', os.listdir(paths_from))
    for file in os.listdir(paths_from):
        #print(file)
        #print(Path(file).suffix.upper())
        if file != 'images' and Path(file).suffix.upper() in ('.JPEG', '.PNG', '.JPG', '.SVG'):
                os.rename(f'{paths_from}\{file}', normalize(f'{paths_from}\{file}'))
                print('name of file: ', file, '- image')
                path_join = os.path.join(paths_from, file)
                print('path_join: ', path_join, '\n')
                shutil.copy2(path_join, paths_to)
                #shutil.move(path_join, paths_to)
                list_images.append(file)
    return list_images

    '''
        if os.path.isdir(f'{paths_from}/{file}') and file != 'IMAGE':

            dirContents = os.listdir(f'{paths_from}/{file}')
            if not dirContents and file != 'IMAGE':
                print(f'{file} is empty')
                os.rmdir(f'{paths_from}/{file}')
            else:
                print(f'{file} not empty')
                return fun_IMAGE(f'{paths_from}/{file}')
    '''        


def fun_documents(paths_from):
    
    list_documents= []

    paths_to = os.path.join('C:/Users/Admin/Downloads/TRASH', 'documents')
    if os.path.exists(paths_to) == False:
        os.mkdir(paths_to)

    #print('os.listdir(paths_from):\n', os.listdir(paths_from))
    for file in os.listdir(paths_from):
        #print(file)
        #print(Path(file).suffix.upper())
        if file != 'documents' and Path(file).suffix.upper() in ('.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX'):
                os.rename(f'{paths_from}/{file}', normalize(f'{paths_from}/{file}'))
                #print('name of file: ', file, '- doc')
                path_join = os.path.join(paths_from, file)
                #print('path_join: ', path_join, '\n')
                shutil.copy2(path_join, paths_to)
                #shutil.move(path_join, paths_to)
                list_documents.append(file)
    return list_documents

def normalize(string):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ "
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", "_")
    
    TRANS = {}

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION): 
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
        
    
    word = ""
    for ch in string:
        word += ch.translate(TRANS)

    print(word)
    return word



def fun_trying(paths_from):

    #paths_from = 'C:/Users/Admin/Downloads/TRASH'

    paths_to = os.path.join('C:/Users/Admin/Downloads/TRASH', 'moved')

    if os.path.exists(paths_to) == False:
        os.mkdir(paths_to)

    #paths_to = 'C:/Users/Admin/Downloads/TRASH/moved'

    for file in os.listdir(paths_from):
        if file != 'moved':
            #print('name of file: ', file)
            path_join = os.path.join(paths_from, file)
            #print('path_join: ', path_join, '\n')
            #shutil.copy2(path_join, paths_to)
            shutil.move(path_join, paths_to)



if __name__ == '__main__':
 
    main()