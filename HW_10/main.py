from collections import UserDict

def main():

    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходимо запис "John" в адресній книзі
    john = book.find("John")

    # Знаходження та редагування телефону для John
    john = book.find("John")
    print('\njohn.edit_phone("1234567890", "1112223333"):')
    john.edit_phone("1234567890", "1112223333")
    
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print('\nfound_phone = john.find_phone("5555555555"):')
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("1234567890")
    print('\nfound_phone = john.find_phone("1234567890"):')
    print(f"{john.name}: {found_phone}")  # Виведення: 1234567890

    # Видалення запису Jane
    book.delete("Jane")

    # Виведення всіх записів у книзі
    #for name, record in book.data.items():
    #    print(record) 
    # Виведення: Contact name: John, phones: 1112223333; 5555555555

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    def __init__(self, value):
        self.value = value
    pass

class Phone(Field):
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)

    @staticmethod
    def is_valid_phone(value):
        return len(value) == 10 and value.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)
    
    def edit_phone(self, old_phone, new_phone):
        found = False
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                found = True
                break
        
        if not found:
            raise ValueError(f"Phone {old_phone} not found in the record")
    
    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value.lower() == number:
                return phone.value
        return None


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

if __name__ == "__main__":
    main()