# Грязная функция.
def dirty_func(s, p, m):
    print("Да" if s + p <= m else "Нет")


dirty_func(500, 600, 2000)


# Чистая функция.
def pure_func(s, p, m):
    return "Да" if s + p <= m else "Нет"


print(pure_func(500, 600, 2000))


# Функция со cтрогой типизацией и документацией.
def best_func(s: int | float, p: int | float, m: int | float) -> str:
    """
    Возможна ли покупка?

    :param s: стоимость подписки
    :param p: стоимость пиццы
    :param m: бюджет
    :return: возрат ответа - да или нет
    """

    return "Да" if s + p <= m else "Нет"


print(best_func(s=500, p=600, m=2000))
