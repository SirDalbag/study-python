# Task 1. Региcтрация.
import re

while True:
    email = input()
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        break
    print("Wrong e-mail")

while True:
    pwd = input()
    if re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$", pwd):
        break
    print("Wrong password")

print("Success")

# Task 2. Четные задачи.
import requests

data = requests.get(f"https://jsonplaceholder.typicode.com/todos/").json()

even_list = [x for x in data if x["id"] % 2 == 0]

# Task 3. Сумма квадратов всех считанных чисел.
arr = []

while True:
    if len(arr) != 0 and sum(arr) == 0:
        break
    num = int(input())
    arr.append(num)

res = sum([x**2 for x in arr])

# Task 4. Оценки.
scores = input().split()

print(
    "{} {} {} {}".format(
        scores.count("5"), scores.count("4"), scores.count("3"), scores.count("2")
    )
)

print(sum([int(x) for x in scores]) / len([int(x) for x in scores]))

# Task 5. Замена оценок.
scores = input().replace("2", "3")

print(scores)
