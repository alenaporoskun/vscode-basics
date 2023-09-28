# Список чисел
numbers = [123, 45, 67890]

# Функція для підрахунку кількості цифр у числі
def count_digits(number):
    return len(str(number))

# Ініціалізуємо лічильник
total_digits = 0

# Перебираємо всі числа у списку та додаємо кількість їх цифр до лічильника
for num in numbers:
    total_digits += count_digits(num)

# Виводимо результат
print(f"Загальна кількість цифр у списку: {total_digits}")