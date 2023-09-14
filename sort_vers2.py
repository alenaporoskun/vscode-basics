import sys
import os
import shutil
import zipfile
import rarfile
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Потрібно вказати шлях до папки.")
        return

    source_folder = sys.argv[1]
    
    if not os.path.exists(source_folder):
        print("Зазначений шлях не існує.")
        return

    destination_folder = os.path.join(source_folder, "FILES")
    os.makedirs(destination_folder, exist_ok=True)

    # Викликаємо функцію для сортування файлів у папці та її вкладених папках
    sort_files(source_folder, destination_folder)

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_path = os.path.join(root, file)
            os.rename(source_path, normalize(source_path))

    print("Файли були відсортовані в папку 'FILES'.")


def sort_files(source_folder, destination_folder):

    for root, dirs, files in os.walk(source_folder):
        
        for directory in dirs:
            if directory not in ('archives', 'video', 'audio', 'documents', 'images'):
                process_directory(os.path.join(root, directory))
        
        for file in files:
            source_path = os.path.join(root, file)
            
            # Перевіряємо, чи файл вже знаходиться у відповідній папці
            #if not os.path.exists(destination_folder):
                # Отримуємо розширення файлу
                #file_extension = os.path.splitext(file)[1].upper()
            # Отримуємо розширення файлу
            file_extension = Path(file).suffix.upper()

            if file_extension in ('.JPEG', '.PNG', '.JPG', '.SVG'):
                 move_file(source_path, destination_folder, 'images')
            elif file_extension in ('.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX'):
                move_file(source_path, destination_folder, 'documents')
            elif file_extension in ('.MP3', '.OGG', '.WAV', '.AMR'):
                move_file(source_path, destination_folder, 'audio')
            elif file_extension in ('.AVI', '.MP4', '.MOV', '.MKV'):
                move_file(source_path, destination_folder, 'video')
            elif file_extension in ('.ZIP', '.GZ', '.TAR'):
                unpack_archive(source_path, destination_folder, 'archives')



def process_directory(directory_path):
    directory_name = os.path.basename(directory_path)
    normalized_name = normalize(directory_name)
    new_directory_path = os.path.join(os.path.dirname(directory_path), normalized_name)

    if new_directory_path != directory_path:
        # перейменовуємо папку згідно функції normalize
        os.rename(directory_path, new_directory_path)

    if not os.listdir(new_directory_path):
        # видаляємо шлях до каталогу
        os.rmdir(new_directory_path)

def move_file(source_path, destination_folder, category_folder):
    #os.rename(source_path, normalize(source_path))
    category_path = os.path.join(destination_folder, category_folder)
    os.makedirs(category_path, exist_ok=True)

    # Отримуємо ім'я файлу без шляху
    filename = os.path.basename(source_path)
    destination_path = os.path.join(category_path, filename)

    # Перевіряємо, чи файл вже знаходиться у відповідній папці
    if not os.path.exists(destination_path):
        #shutil.move(source_path, destination_path)
        shutil.copy2(source_path, destination_path)

def unpack_archive(archive_path, destination_folder, category_folder):
    #os.rename(archive_path, normalize(archive_path))
    category_path = os.path.join(destination_folder, category_folder)
    os.makedirs(category_path, exist_ok=True)
    archive_extension = os.path.splitext(archive_path)[1].upper()

    # Отримуємо ім'я файлу без шляху
    filename = os.path.basename(archive_path)
    filename = str(filename).replace(Path(filename).suffix, '')
    destination_path = os.path.join(category_path, filename)
    print('destination_path ', destination_path)

    # Перевіряємо, чи файл вже знаходиться у відповідній папці
    if not os.path.exists(destination_path):
        shutil.unpack_archive(archive_path, category_path)
        '''
        if archive_extension == '.ZIP':
            with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                zip_ref.extractall(destination_path)
        elif archive_extension == '.RAR':
            with rarfile.RarFile(archive_path, 'r') as rar_ref:
                rar_ref.extractall(destination_path)
        '''
        
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

    return word

if __name__ == "__main__":
    main()
