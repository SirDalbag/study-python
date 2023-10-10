import functools


def mul(a, b):
    return a * b


# Позволяет создавать новую функцию с фиксированными аргументами.
double = functools.partial(mul, 2)
print(double(2))

# Применяет указанную функцию к элементам последовательности, сводя её к единственному значению.
nums = [1, 2, 3]
print(functools.reduce(mul, nums))


# Позволяет ускорить выполнение функции, кэшируя результаты вызовов функции.
@functools.lru_cache(maxsize=5)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))


# Позволяет получить имя функции, её аргументы и документацию (метаданные).
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@decorator
def sqrt(a):
    """Return sqrt(a)"""
    return a**0.5


print(sqrt.__name__)
print(sqrt.__doc__)
print(sqrt(4))
