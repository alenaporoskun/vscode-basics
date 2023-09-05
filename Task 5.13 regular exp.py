import re

'''
Тепер ми потренуємося писати корисні регулярні вирази. Напишіть регулярний вираз для функції find_all_emails, 
яка буде в тексті (параметр text) знаходити всі email та повертати список отриманих з тексту збігів.

З метою спрощення приймемо, що:
ми використовуємо для email, — англійський алфавіт
префікс (все, що знаходиться до символу @) починається з латинської літери та може містити будь-яке число або букву, 
включаючи нижнє підкреслення та символ точки. Має складатися мінімум із двох символів
суфікс email (все, що знаходиться після символу @) складається лише з букв англійського алфавіту, та має дві частини, розділені точкою, 
також доменне ім'я верхнього рівня не може бути менш ніж два символи (все, що після точки)
Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих варіантів email.

При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс для перевірок регулярних виразів regex101.
'''

def find_all_emails(text):
    
    result = re.findall(r"[a-zA-Z]{1}[\w\.]{1,}@{1}[a-zA-Z]+\.{1}[a-zA-Z]{2,}", text)
    for i in result:
        print(i)
    return result


#find_all_emails('Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net')

'''
['Ima.Fool@iana.org', 
'Fool@iana.org', 
'first_last@iana.org',
'first.middle.last@iana.or', 
'abc111@test.com']
'''

find_all_emails( 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net' )
'''
Очікувалося, що функція find_all_emails при отриманні параметра 
+ 'Ima.Fool@iana.org 
- Ima.Fool@iana.o 
- 1Fool@iana.org 
+ first_last@iana.org 
+ first.middle.last@iana.or 
- a@test.com 
+ abc111@test.com.net' 

поверне наступний список 
['Ima.Fool@iana.org', 
'Fool@iana.org', 
'first_last@iana.org', 
'first.middle.last@iana.or', 
'abc111@test.com']
'''