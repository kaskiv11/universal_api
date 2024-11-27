conditions = [True, True, True]
conditions2 = [False, False, False]

all_conditions_met = all(conditions2)

print(all_conditions_met)

numbers = [-1, -6, -3, 0]

has_positive = any(n > 0 for n in numbers)
print(has_positive)

import random

numbers = [random.randint(-10, 10) for _ in range(10)]
print(numbers)

people = [
    {"name": "Anna", "age": 27},
    {"name": "Rina", "age": 23},
    {"name": "Rina", "age": 22},
    {"name": "Mike", "age": 40}
]

print(people)

sorted_people = sorted(people, key=lambda person: (person['name'], person["age"]))


print(sorted_people)