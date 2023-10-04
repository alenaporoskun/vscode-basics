# Завдання  
  
У цьому домашньому завданні ми:  
* Додамо поле для дня народження Birthday. Це поле не обов'язкове, але може бути тільки одне.
* Додамо функціонал роботи з Birthday у клас Record, а саме функцію days_to_birthday, яка повертає кількість днів до наступного дня народження.
* Додамо функціонал перевірки на правильність наведених значень для полів Phone, Birthday.
* Додамо пагінацію (посторінковий висновок) для AddressBook для ситуацій, коли книга дуже велика і треба показати вміст частинами, а не все одразу. Реалізуємо це через створення ітератора за записами.  
  
## Критерії прийому:
* AddressBook реалізує метод iterator, який повертає генератор за записами AddressBook і за одну ітерацію повертає уявлення для N записів.
* Клас Record приймає ще один додатковий (опціональний) аргумент класу Birthday
* Клас Record реалізує метод days_to_birthday, який повертає кількість днів до наступного дня народження контакту, якщо день народження заданий.
* setter та getter логіку для атрибутів value спадкоємців Field.
* Перевірку на коректність веденого номера телефону setter для value класу Phone.
* Перевірку на коректність веденого дня народження setter для value класу Birthday.  
  
## Example of Output:
Contact name: John, phones: 1234567890; 5555555555  
Contact name: Jane, phones: 9876543210  

john.edit_phone("1234567890", "1112223333"):  
Contact name: John, phones: 1112223333; 5555555555  
  
found_phone = john.find_phone("5555555555"):  
John: 5555555555   
   
john_record.set_birthday("2001-08-19")     
Contact name: John, phones: 1112223333; 5555555555, birthday: 2001-08-19   
There are 319 days left before the birthday.  
  
Add another contacts...  
   
book:  
Page 1  
Contact name: John, phones: 1112223333; 5555555555, birthday: 2001-08-19  
Contact name: Jane, phones: 9876543210  
Contact name: Kol  
Contact name: Anna  
Contact name: Lily  
Page 2  
Contact name: David  
Contact name: Clark  