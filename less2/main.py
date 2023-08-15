# Task 1. Это треугольник?
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

res = True if a + b > c and a + c > b and b + c > a else False

# Task 2. Это четное число?
a = int(input("A: "))

res = True if a % 2 == 0 else False

# Task 3. Сумма A и B больше C?
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

res = True if a + b > c else False

# Task 4. A больше В?
a = int(input("A: "))
b = int(input("B: "))

res = True if a > b else False
