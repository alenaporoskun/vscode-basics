""" 
Потрібно написати функцію реалізації наступного ігрового алгоритму. 
На вхід функції game подається два аргументи: список, що складається зі списків, та початкове значення power - енергія гравця. 
Внутрішні списки — це списки з числовим значенням енергії, які може поглинути гравець, якщо вони менші або дорівнюють його енергії. 
Після поглинання елементу списку він рухається за списком далі та, або поглинає список повністю до кінця, 
або, якщо знаходить енергію вище за власну, залишає його і переходить до наступного списку. 
Наприкінці обходу всіх списків функція повинна повернути загальну отриману енергію гравця.

Приклад списку:
[[1, 1, 5, 10], [10, 2], [1, 1, 1]]
Для цього списку і початкової енергії рівної 1 гравець поглине з першого списку перші два значення і залишить його, 
зустрівши значення 5, через те, що на цей момент матиме енергію в 3. 
Другий список пропустить відразу, а третій повністю поглине та отримає остаточну енергію в 6. 
"""


def game(terra, power):
    for t in terra:
        for i in t:
            if power >= i:
                power += i
            else:
                break
    return power
    
print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))  