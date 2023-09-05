grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    i = 1
    answer = []
    for key, value in students.items():
        ans = ('{:>4}|{:<10}|{:^5}|{:^5}'.format(i, key, value, grades[value]))
        answer.append(ans)
        i += 1
               
    for el in answer:
        print(el)
        
    return answer

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
formatted_grades(students)