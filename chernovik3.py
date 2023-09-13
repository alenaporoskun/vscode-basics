import sys
import os
import shutil
from pathlib import Path
# from pyunpack import Archive

def main():
    args = sys.argv
    paths_from = Path(args[1])
    print(paths_from)

    for i in paths_from.iterdir():
        
        if i.is_dir():
            print(i.name, ' - папка')

        if i.is_file():
            print(i.name, ' - файл')
    
    sort(paths_from)


def sort(paths_from):
    # paths_from = 'C:/Users/Admin/Downloads/TRASH'

    # fun_trying(paths_from)

    global list_extensions, list_unknown_extensions
    list_extensions = []
    list_unknown_extensions= []
    list_unknown_ext = []

    images = fun_images(paths_from)
    documents = fun_documents(paths_from)
    audio = fun_audio(paths_from)
    video = fun_video(paths_from)
    archives = fun_archives(paths_from)

    print(f' images {images}\n documents {documents}\n audio {audio}\n video {video}\n archives {archives}')

    for i in range(len(list_unknown_extensions)):
        item = list_unknown_extensions[i]
        if (item not in list_extensions) and (item != ''):
            list_unknown_ext.append(item)

    list_unknown_extensions.clear()

    print(' list of unknown extensions = ', list_unknown_ext)


def fun_images(paths_from):
    
    list_images = []
    
    paths_to = os.path.join('C:/Users/Admin/Downloads/TRASH', 'images')
    if os.path.exists(paths_to) == False:
        os.mkdir(paths_to)

    for file in os.listdir(paths_from):
        if Path(file).suffix.upper() in ('.JPEG', '.PNG', '.JPG', '.SVG'):
                os.rename(f'{paths_from}/{file}', normalize(f'{paths_from}/{file}'))
                path_join = os.path.join(paths_from, file)
                # shutil.copy2(path_join, paths_to)
                shutil.move(path_join, paths_to)
                list_images.append(file)
                list_extensions.append(Path(file).suffix)
        else:
            list_unknown_extensions.append(Path(file).suffix)
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

    for file in os.listdir(paths_from):
        if Path(file).suffix.upper() in ('.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX'):
                os.rename(f'{paths_from}/{file}', normalize(f'{paths_from}/{file}'))
                path_join = os.path.join(paths_from, file)
                # shutil.copy2(path_join, paths_to)
                shutil.move(path_join, paths_to)
                list_documents.append(file)
                list_extensions.append(Path(file).suffix)
        else:
            list_unknown_extensions.append(Path(file).suffix)
    return list_documents


def fun_audio(paths_from):
    
    list_audio = []

    paths_to = os.path.join('C:/Users/Admin/Downloads/TRASH', 'audio')
    if os.path.exists(paths_to) == False:
        os.mkdir(paths_to)

    for file in os.listdir(paths_from):
        if Path(file).suffix.upper() in ('.MP3', '.OGG', '.WAV', '.AMR'):
                os.rename(f'{paths_from}\{file}', normalize(f'{paths_from}\{file}'))
                path_join = os.path.join(paths_from, file)
                #shutil.copy2(path_join, paths_to)
                shutil.move(path_join, paths_to)
                list_audio.append(file)
                list_extensions.append(Path(file).suffix)
        else:
            list_unknown_extensions.append(Path(file).suffix)
    return list_audio


def fun_video(paths_from):
    
    list_video = []

    paths_to = os.path.join('C:/Users/Admin/Downloads/TRASH', 'video')
    if os.path.exists(paths_to) == False:
        os.mkdir(paths_to)

    for file in os.listdir(paths_from):
        if Path(file).suffix.upper() in ('.AVI', '.MP4', '.MOV', '.MKV'):
                os.rename(f'{paths_from}\{file}', normalize(f'{paths_from}\{file}'))
                path_join = os.path.join(paths_from, file)
                #shutil.copy2(path_join, paths_to)
                shutil.move(path_join, paths_to)
                list_video.append(file)
                list_extensions.append(Path(file).suffix)
        else:
            list_unknown_extensions.append(Path(file).suffix)
    return list_video


def fun_archives(paths_from):
    
    list_archives = []

    paths_to = os.path.join('C:/Users/Admin/Downloads/TRASH', 'archives')
    if os.path.exists(paths_to) == False:
        os.mkdir(paths_to)

    for file in os.listdir(paths_from):
        if Path(file).suffix.upper() in ('.ZIP', '.GZ', '.TAR'):
                os.rename(f'{paths_from}/{file}', normalize(f'{paths_from}/{file}'))

                new_name = file.replace(Path(file).suffix, '')
                try:
                    shutil.unpack_archive(file, f'{paths_to}/{new_name}')
                    list_archives.append(file)
                except shutil.ReadError:               
                    print(f"Файл {file} має розширення архіву, проте не є ним.\n")
                finally:
                    list_extensions.append(Path(file).suffix)
        else:
            list_unknown_extensions.append(Path(file).suffix)
    return list_archives


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