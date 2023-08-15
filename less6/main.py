# Task 1. Получение задачи по ID и запись в текстовый файл.
import requests

num = input()

data = requests.get(f"https://jsonplaceholder.typicode.com/todos/{num}")

with open("less6/data.txt", mode="w", encoding="utf-8") as file:
    file.write(str(data.json()))


# Task 2. Вывод сообщения в случае ошибки.
def plus_two(number):
    return number + 2


try:
    print(plus_two("1"))
except TypeError:
    print("Ожидаемый тип данных - чиcло!")
except Exception as error:
    print(error)
finally:
    pass


# Task 3. Вывод сообщения в случае выхода индекса за границу списка.
def index_error(arr: list[int | float], index: int) -> int | float:
    return arr[index]


try:
    print(index_error([1, 2, 3], 4))
except IndexError:
    print("Индекс вышел за границы списка")
except Exception as error:
    print(error)
finally:
    pass
