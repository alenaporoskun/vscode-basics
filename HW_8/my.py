import collections

# Person = collections.namedtuple('Person', ['name', 'last_name', 'age', 'birth_place', 'post_index'])
# person = Person('Mick', 'Nitch', 35, 'Boston', '01146')
# print(person.name)         # 'Mick'
# print(person.post_index)   # '01146'
# print(person.age)          # 35
# print(person[3])  


Person2 = collections.namedtuple('Person', ['name', 'last_name'])
person = Person2('Mick', 'Nitch')
print(person.name)         # 'Mick'
print(person.last_name)   # '01146'


