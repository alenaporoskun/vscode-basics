'''
У багатьох на робочому столі є папка, яка називається якось ніби "Розібрати". Як правило, розібрати цю папку руки ніколи так і не доходять.

Ми з вами напишемо скрипт, який розбере цю папку. Зрештою ви зможете настроїти цю програму під себе і вона виконуватиме індивідуальний сценарій, 
що відповідає вашим потребам. Для цього наш додаток буде перевіряти розширення файлу (останні символи у імені файлу, як правило, після крапки)
 і, залежно від розширення, приймати рішення, до якої категорії віднести цей файл.

Скрипт приймає один аргумент при запуску — це ім'я папки, в якій він буде проводити сортування. 
Допустимо файл з програмою називається sort.py, тоді, щоб відсортувати папку /user/Desktop/Мотлох, треба запустити скрипт командою python sort.py /user/Desktop/Мотлох

Для того щоб успішно впорається з цим завданням, ви повинні винести логіку обробки папки в окрему функцію.
Щоб скрипт міг пройти на будь-яку глибину вкладеності, функція обробки папок повинна рекурсивно викликати сама себе, коли їй зустрічаються вкладенні папки.
Скрипт повинен проходити по вказаній під час виклику папці та сортирувати всі файли по групам:

зображення ('JPEG', 'PNG', 'JPG', 'SVG');
відео файли ('AVI', 'MP4', 'MOV', 'MKV');
документи ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
музика ('MP3', 'OGG', 'WAV', 'AMR');
архіви ('ZIP', 'GZ', 'TAR');
'''
from pathlib import Path
import sys
import os


def main():
    args = sys.argv
    p = Path(args[1])
    #print(p)

    for i in p.iterdir():
        
        if i.is_dir():
            print(i.name, ' - папка')
        if i.is_file():
            #print(i.name, ' - файл')
            if fun_image(i):
                print(os.listdir(p))
                #source = p
                #destination = Path(args[1] + '\' + 'IMAGE') # '/opt/awesome/destination'
                #os.rename(source, destination)
                #os.listdir(p)

                
            # iterate on all files to move them to destination folder
            for file_path in allfiles:
                dst_path = os.path.join(destination, os.path.basename(file_path))
                shutil.move(file_path, dst_path)
                print(f"Moved {file_path} -> {dst_path}")



            #fun_document(i)



def fun_image(i):
    
    if i.suffix.upper() in ('.JPEG', '.PNG', '.JPG', '.SVG'):
        print(i.name, ' - зображення')
        return True
    return False

def fun_document(i):

    if i.suffix.upper() in ('.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX'):
        print(i.name, ' - документ')
        return True
    return False

if __name__ == '__main__':
 
    main()

