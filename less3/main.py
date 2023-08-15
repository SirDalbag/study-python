# Task 1. Проверка данных.
login = input("")
pwd = input("")

if login == "user" and pwd == "qwerty":
    print("Authentication completed")
else:
    print("Invalid login or password")

# Task 2. Обмен валют.
amount = int(input("Insert amount in KZT: "))
currency = int(input("Choose currency:\n[1] USD\n[2] EUR\n[3] RUB\n"))

res = 0

match (currency):
    case 1:
        res = amount / 420
        print(f"{res:.2f} USD")
    case 2:
        res = amount / 510
        print(f"{res:.2f} EUR")
    case 3:
        res = amount / 5.8
        print(f"{res:.2f} RUB")
    case _:
        print("Unknown currency")

# Task 3. Массив чисел и массив c их квадратами.
arr1 = []

for i in range(0, 1000 + 1):
    arr1.append(i)

arr2 = []

for i in arr1:
    arr2.append(i**2)
