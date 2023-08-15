# Task 1. Инкапсуляция.
class Parent:
    def __init__(self, text: str):
        self._text = text

    def set(self, text: str = None):
        if text is not None:
            self._text = text
        else:
            self._text = ""


class Child(Parent):
    def __init__(self, text: str, number: int):
        super().__init__(text)
        self._number = number


# Task 2. Полиморфизм.
class Parent:
    def __init__(self, text: str):
        self._text = text

    def set(self, text: str = None):
        if text is not None:
            self._text = text
        else:
            self._text = ""


class Child(Parent):
    def __init__(self, text: str, number: int):
        super().__init__(text)
        self._number = number

    def set(self, text: str = None):
        if text is not None:
            self._text = text
        else:
            self._text = "Empty"


# Task 3. Римское число.
class Roman:
    roman_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def __init__(self, roman):
        self.num = Roman.roman_to_int(roman)

    def __add__(self, other):
        if isinstance(other, Roman):
            return self.num + other.num
        else:
            raise TypeError("Невозможно сложить!")

    def __sub__(self, other):
        if isinstance(other, Roman):
            return self.num - other.num
        else:
            raise TypeError("Невозможно вычесть!")

    def __mul__(self, other):
        if isinstance(other, Roman):
            return self.num * other.num
        else:
            raise TypeError("Невозможно умножить!")

    def __truediv__(self, other):
        if isinstance(other, Roman):
            return int(self.num / other.num)
        else:
            raise TypeError("Невозможно разделить!")

    @staticmethod
    def roman_to_int(roman: str) -> int:
        result = 0
        prev = 0

        for i in reversed(roman):
            curr = Roman.roman_int[i]
            if curr < prev:
                result -= curr
            else:
                result += curr
                prev = curr

        return result
