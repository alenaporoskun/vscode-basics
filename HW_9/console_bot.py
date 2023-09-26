def main():

    while True:
        string = input('Enter command: ')
        if string in ('.', 'good bye', 'close', 'exit'):
            print('Good bye!')
            break
        string = string.split() # розбити рядок на частини за  роздільником ' '
        '''
        Функція get_handler призначена для обробки команд, які вводить користувач. 
        Цей рядок після виконання присвоює змінній f результат роботи функції get_handler, 
        тобто функцію, яка відповідає за обробку команди, яку ввів користувач.
        '''
        f = get_handler(string) # 
        if callable(f):
            # далі перевіряємо кількість частин у string і виконуємо функцію відповідно до неї 
            if len(string) == 1:
                result = f()
            elif len(string) == 2:
                result = f(string[1])
            elif len(string) == 3:
                result = f(string[1], string[2])
            else:
                result = 'Invalid number of arguments for the command.'
            print(result)
        else:
            print(f)

contacts = {}  # Словник для зберігання контактів

def fun_hello():
    return 'How can I help you?'

def fun_add(name=None, number=None):
    if name is None:
        return "Error: Name and phone number are not provided."
    if number is None:
        return "Error: Phone number is not provided."
    contacts.update({name: number})
    return f'Contact {name} added with number {number}'

def fun_change(name, number):
    if name in contacts:
        contacts[name] = number
        return f'Phone number for {name} changed to {number}'
    else:
        return f'Contact {name} not found'

def fun_phone(name):
    if name in contacts:
        return f"Phone number for contact {name}: {contacts[name]}."
    else:
        return f"Error: Contact {name} not found."

def fun_show_all(str='all'):
    if str == 'all':
        return contacts
    else:
        return "Error: Invalid command."


commands = {
        'hello': fun_hello,
        'add': fun_add,
        'change': fun_change,
        'phone': fun_phone,
        'show': fun_show_all
    }

# декоратор для обробки помилок
def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
        except TypeError as e:
            result = f'Error: Command missing argument - {e}'
        except KeyError as e:
            result = f'Error: Command not found - {e}'
        except ValueError as e:
            result = f'Error: Invalid input - {e}'
        except IndexError as e:
            result = f'Error: Invalid number of arguments - {e}'
        except Exception as e:
            result = f'Error: {e}'
        return result

    return inner


@input_error
def get_handler(*args):
    '''
    Функція get_handler призначена для обробки команд, які вводить користувач. 
    Цей рядок після виконання присвоює змінній f результат роботи функції get_handler, 
    тобто функцію, яка відповідає за обробку команди, яку ввів користувач.
    '''
    # так як бот не чутливий до регістру, то робимо регістр команди низьким (першого елемента в string)
    item = args[0][0].lower()
    # повертаємо значення за ключем item зі словника commands
    return commands.get(item, f'Command {item} not found')


if __name__ == "__main__":
    main()
