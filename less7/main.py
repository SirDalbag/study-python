# Task 1. Cравнение дат.
import json
from datetime import timedelta

day1 = input()
day2 = input()

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

date1 = timedelta(days=(days.index(day1) + 7) % 7)
date2 = timedelta(days=(days.index(day2) + 7) % 7)

hours_difference = abs(date2 - date1).total_seconds() // 3600

print(f"After {hours_difference} hours")

data = {
    "day1": day1,
    "day2": day2,
}

with open("less7/data.json", "w") as file:
    json.dump(data, file)


# Task 2. Шифр Цезаря.
def encrypt(text: str, shift: int) -> str:
    return [chr((ord(x) - 97 + shift) % 26 + 97) for x in text]


# Task 3. Как часто встречается фрукт?
fruit = input()

fruits = ("apple", "orange", "orange", "banana", "kiwi", "mango")

print(fruits.count(fruit))

# Task 4. Как часто встречается название фрукта?
fruit = input()

fruits = ("apple", "orangebanana", "orange", "banana", "kiwi", "mango-banana")

print(sum([1 for x in fruits if fruit in x]))

# Task 5. Замена названий в кортеже.
brand = input()
new_brand = input()

cars = ("Ford", "BMW", "Toyota", "Mitsubishi", "Lada", "Toyota", "Toyota")

new_cars = tuple([new_brand if x == brand else x for x in cars])


# Task 6. Супермножество.
def superset(set1: set, set2: set) -> str:
    if set1 == set2:
        return "Множества равны"
    elif set1.issuperset(set2):
        return f"Объект {set1} является чистым супермножеством"
    elif set2.issuperset(set1):
        return f"Объект {set2} является чистым супермножеством"
    else:
        return "Супермножество не обнаружено"


print(superset(set([1, 2, 3]), set([4, 5, 6])))


# Task 7. Методы словаря.
def add_word(dict: dict, en: str, fr: str) -> dict:
    dict[en] = fr
    return dict


def del_word(dict: dict, en: str) -> dict:
    if en in dict:
        del dict[en]
    return dict


def find_word(dict: dict, en: str) -> str:
    if en in dict:
        return f"{en} - {dict[en]}"
    return "Not Found"


def edit_word(dict: dict, en: str, fr: str) -> dict:
    dict[en] = fr
    return dict


# Task 8. Множество натуральных чисел.
def set_gen(list: list[int]) -> set:
    result = set()
    count_dict = {}

    for i in list:
        if i in count_dict:
            count_dict[i] += 1
            str_i = str(i) * count_dict[i]
            result.add(str_i)
        else:
            count_dict[i] = 1
            result.add(i)

    return result
