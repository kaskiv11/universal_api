def out_func(x):
    def in_func(y):
        return x + y

    return in_func


clos = out_func(5)

print(clos(10))


def power(number):
    print("Enter count")

    def power_func(count):
        return number ** count

    return power_func


number = power(10)
print(number(5))

from typing import List, Dict, Set, Tuple

name: List[str] = ["Alice", "Bob", "Charlie"]
scores: Dict[str, int] = {"Alice": 5, "Bob": 4, "Charlie": 7}
unique_numbers: Set[int] = {1, 4, 5, 8, 8}
coordination: Tuple[int, int, int] = (10, -2, 0)

print(name)
print(scores)
print(unique_numbers)
print(coordination)

print(sum(scores.values()))


def add_score(name, number):
    scores[name] = number
    return scores