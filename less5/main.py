# Task 1. Функция - калькулятор.
def calc(val1: int | float, val2: int | float, operation: str) -> int | float:
    match (operation):
        case "+":
            return val1 + val2
        case "-":
            return val1 - val2
        case "*":
            return val1 * val2
        case "/":
            return val1 / val2
        case _:
            return 0


# Task 2. Проверка на cовпадение всех элементов массива.
def check_arr(arr: list[int | float]) -> bool:
    if len(arr) <= 1:
        return True

    if arr[0] != arr[1]:
        return False
    return check_arr(arr[1:])


def check_arr_val(arr: list[int | float], val: int | float) -> bool:
    if len(arr) < 1:
        return True

    if arr[0] == val:
        return check_arr_val(arr[1:], val)
    else:
        return False


# Task 3. Число, которое делится на обо числа без остатка.
def division_num(a: int, b: int) -> int:
    d = min(a, b)
    while True:
        if d % a == 0 and d % b == 0:
            break
        d += 1
    return d


print(division_num(1, 2))


# Task 4. Поиск потерянной карточки.
def find_card(n: int, arr: list[int]) -> int:
    card = [x for x in [i for i in range(1, n + 1)] if x not in arr]
    return n if not card else card[0]


print(find_card(5, [5, 3, 5, 2, 1]))


# Task 5. Квадраты чисел не больше N.
def square_num(n: int) -> list[int]:
    arr = []
    for i in range(1, n + 1):
        if i**2 > n:
            break
        arr.append(i**2)
    return arr


for i in square_num(10):
    print(i)
