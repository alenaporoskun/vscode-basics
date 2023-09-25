import sys
import os
import shutil
import zipfile
import rarfile
from pathlib import Path

def main():

    string = ""
    while True:
        string = input('Enter command: ')
        if string in ('.', 'good bye', 'close', 'exit'):
            print('Good bye!')
            break
        string = string.split()
        #if string[0].lower() == 'hello':
        #   print('How can I help you?')
        '''
        if len(string) == 1:
            f = get_handler(string[0].lower())
            f()

        elif len(string) == 2:
            f = get_handler(string[0].lower())
            res = f(string[1])
            print(res)

        else:
            f = get_handler(string[0].lower())
            res = f(string[1], string[2])
            print(res)
        print(dict)
        '''
        f = get_handler(string)
        

        

dict = {}

def fun_hello():
    print('How can I help you?')

def fun_add(name, number):
    dict.update({name: number})
    #dict[name] = number

def fun_change(name, number):
    dict[name] = number

def fun_phone(name):
    return dict[name]

def fun_show_all(str='all'):
    if str == 'all':
        return dict
    

commands = {
    'hello': fun_hello,
    'add': fun_add,
    'change': fun_change,
    'phone': fun_phone,
    'show': fun_show_all
    }

def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
        except KeyError as e:
            print(f"Помилка: Команда не знайдена - {e}")
        except Exception as e:
            print(f"Помилка: {e}")
        return result
    return inner


@input_error
def get_handler(*args): #(command)
    # return  commands[command]
    item = args[0]
    item = item[0]
    item = str(item).lower()
    return commands[item]


if __name__ == "__main__":
    main()