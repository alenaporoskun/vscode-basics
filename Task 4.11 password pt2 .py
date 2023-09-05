def is_valid_password(password):
    """
    Функція, яка перевірятиме отриманий параметр — пароль на надійність.
    Функція is_valid_password повинна повернути True, якщо переданий параметр пароль відповідає вимогам на надійність. 
    Інакше повернути False 
    """

    # Довжина рядка пароля має бути вісім символів
    if len(password) < 8:
        return False
    
    # пароль повинен мати хоча б одну літеру у верхньому регістрі
    upper = 0
    for ch in password:
        if ((ord(ch) > 64) & (ord(ch) < 91)):
            upper += 1
    if upper == 0:
        return False
    
    # пароль повинен мати хоча б одну літеру у нижньому регістрі
    lower = 0
    for ch in password:
        if ((ord(ch) > 96) & (ord(ch) < 123)):
            lower += 1
    if lower == 0:
        return False    

    # пароль повинен мати хоча б одну цифру
    number = 0
    for ch in password:
        if ((ord(ch) > 47) & (ord(ch) < 58)):
            number += 1
    if number == 0:
        return False 

    return True
    
print(is_valid_password('1wwAU\Gq')) # True
print(is_valid_password('1wwfh\6q')) # False
print(is_valid_password('wwfh\q')) # False
print(is_valid_password('wwfh\qpt')) # False
        
            
        
            
        
            
    
        
    