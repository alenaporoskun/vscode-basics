'''
Повернемося до нашого завдання із телефонними номерами. Компанія розширюється та вийшла на ринок Азії. 
Тепер у списку можуть знаходитись телефони різних країн. Кожна країна має свій телефонний код .

Компанія працює з наступними країнами

Країна	Код ISO	Префікс
Japan	    JP	+81
Singapore	SG	+65
Taiwan	    TW	+886
Ukraine	    UA	+380

Щоб ми могли коректно виконати рекламну SMS кампанію, необхідно створити для кожної країни свій список телефонних номерів.

Напишіть функцію get_phone_numbers_for_сountries, яка буде:

Приймати список телефонних номерів.
Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
Сортувати телефонні номери за вказаними у таблиці країнами.
Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
{
    "UA": [<тут список телефонів>],
    "JP": [<тут список телефонів>],
    "TW": [<тут список телефонів>],
    "SG": [<тут список телефонів>]
}
Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'.
'''


def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    new_phones = []
    for phone in list_phones:
        new_phones.append(sanitize_phone_number(phone))
    '''
    dict_pref = {
        'JP': '81',
        'SG': '65',
        'TW': '886',
        'UA': '380',
    }
    '''
    countries = ['JP', 'SG', 'TW',  'UA']
    prefix =    ['81', '65', '886', '380']
    list_phone = [[], [], [], []]

    for phone in new_phones:
        not_find = 0
        for i in range(len(countries)):
            if phone[:3].find(prefix[i], 0, 3) == 0:
                list_phone[i].append(phone)
                break
            else:
                not_find += 1

        if not_find == 4:
            list_phone[3].append(phone)

        dict_ans = {
        'JP': list_phone[0],
        'SG': list_phone[1],
        'TW': list_phone[2],
        'UA': list_phone[3],
        }

    return dict_ans


list1 = ['0658759411', '818765347', '818765344', '8867658976', '657658976']
list2 = ['065-875-94-11', '(81)8765347', '8867658976', '657658976', '(65)765-89-77'] 
print(get_phone_numbers_for_countries(list2))