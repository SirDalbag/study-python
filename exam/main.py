# TODO: Практическая часть
# Задача 1.1. Выведите в консоль 5 звёздочек, используя умножение строк.
print("*" * 5)


# Задача 1.2. Напишите программу на Python, чтобы создать треугольник из звезд.
def triangle(h: int) -> str:
    triangle = ""
    for i in range(1, h + 1):
        for _ in range(1, h - i + 1):
            triangle += " "
        for _ in range(1, 2 * i):
            triangle += "*"
        if i != h:
            triangle += "\n"
    return triangle


# Задача 2.1. Получите через http – запрос все объекты из jsonplaceholder todo. (https://jsonplaceholder.typicode.com/todos)
import requests


def request_todos(url: str) -> list[dict]:
    return requests.get(url).json()


# Задача 2.2. Запишите все полученные данные в новую папку temp, в разные .json файлы.
import json


def save_todos(todos: list[dict]):
    for todo in todos:
        with open(f"exam/temp/{todo['id']}.json", "w") as f:
            json.dump(todo, f)


# Задача 2.3. Прочитайте все файлы из папки, и запишите данные каждого в единый .xlsx файл.
import os
from openpyxl import Workbook


def save_to_xlsx():
    wb = Workbook()
    ws = wb.active
    ws.title = "todos"
    ws.append(["userId", "id", "title", "completed"])
    for file in os.listdir("exam/temp"):
        with open(f"exam/temp/{file}", "r") as f:
            data = json.load(f)
            ws.append([data["userId"], data["id"], data["title"], data["completed"]])
    wb.save("exam/todos.xlsx")


# Задача 3.1. Напишите любой пример бесконечного таймера, через цикл while.
import time


def timer():
    h, m, s = 0, 0, 0
    while True:
        s += 1
        if s >= 60:
            s = 0
            m += 1
        if m >= 60:
            m = 0
            h += 1
        if h >= 24:
            h = 0
        print(f"{h:02}:{m:02}:{s:02}")
        time.sleep(1)


# Задача 3.2. Модифицируйте код, чтобы можно было задать множитель для секунд от ввода пользователя.


def timer_mod(k: int):
    h, m, s = 0, 0, 0
    while True:
        s += 1 * k
        if s >= 60:
            s = 0
            m += 1
        if m >= 60:
            m = 0
            h += 1
        if h >= 24:
            h = 0
        print(f"{h:02}:{m:02}:{s:02}")
        time.sleep(1)


# Задача 4.1. Определите класс car с двумя атрибутами: color и speed. Затем создайте экземпляр и верните speed.
class Car:
    def __init__(self, color: str, speed: int):
        self.color = color
        self.speed = speed


car = Car("red", 100)
car_speed = car.speed

# Задача 4.2. Модифицируйте код так, чтобы при старте программы, пользователь мог сам задать скорость машины, проверку выполните через регулярное выражение.
import re

while True:
    speed = input("")
    if re.match(r"^\d+$", speed):
        car = Car("red", int(speed))
        break

# Задача 5.1. Реализуйте программу с интерфейсом на библиотеке pyqt6, необходимо чтобы при нажатии происходил запрос по адресу, введённому в textedit, статус запроса выводите в консоль.
import sys
import requests
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QWidget,
    QGridLayout,
)


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setWindowTitle("Request")
        self.setGeometry(200, 200, 400, 100)

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.layout = QGridLayout()
        self.layout.setSpacing(4)

        self.label = QLabel("Link:")
        self.layout.addWidget(self.label, 0, 0)

        self.link = QLineEdit()
        self.layout.addWidget(self.link, 0, 1)

        button = QPushButton("Send")
        button.clicked.connect(self.request)
        self.layout.addWidget(button, 0, 2)

        self.status_label = QLabel("Status:")
        self.layout.addWidget(self.status_label, 1, 0)

        self.status = QLabel("")
        self.layout.addWidget(self.status, 1, 1)

        self.widget.setLayout(self.layout)

    def request(self):
        url = self.link.text()
        try:
            status_request = str(requests.get(url))
            print(status_request)
        except Exception as error:
            self.status.setText(f"Error: {str(error)}")


def start_app():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())


# Задача 5.2. Модифицируйте код так, чтобы статус запроса с описанием выводился в текстовое поле в инстерфейсе. Соберите программу в исполняемый файл, т.е. .exe.
# Собрать в .exe файл не получилось.


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setWindowTitle("Request")
        self.setGeometry(200, 200, 400, 100)

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.layout = QGridLayout()
        self.layout.setSpacing(4)

        self.label = QLabel("Link:")
        self.layout.addWidget(self.label, 0, 0)

        self.link = QLineEdit()
        self.layout.addWidget(self.link, 0, 1)

        button = QPushButton("Send")
        button.clicked.connect(self.request)
        self.layout.addWidget(button, 0, 2)

        self.status_label = QLabel("Status:")
        self.layout.addWidget(self.status_label, 1, 0)

        self.status = QLabel("")
        self.layout.addWidget(self.status, 1, 1)

        self.widget.setLayout(self.layout)

    def request(self):
        url = self.link.text()
        try:
            status_request = str(requests.get(url))
            self.status.setText(status_request)
        except Exception as error:
            self.status.setText(f"Error: {str(error)}")


# Задача 6.1. Подбор пароля для тестирования: записать в документ в один поток числа от 1 до 100000.


def generator():
    with open("exam/temp/temp.txt", "w") as file:
        for i in range(1, 100001):
            file.write(str(i) + "\n")


# Задача 6.2. Переписать логику на 10 мультипроцессов и в конце склейку в один.
import os
import concurrent.futures


def generator_multiprocessing(start, end):
    with open(f"exam/temp/{start}.txt", "w") as file:
        for i in range(start, end + 1):
            file.write(str(i) + "\n")


def multi():
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        for i in range(10):
            start = i * 10000 + 1
            end = (i + 1) * 10000
            executor.submit(generator_multiprocessing, start, end)
    with open("exam/temp/result.txt", "wb") as file:
        for i in range(10):
            filename = f"exam/temp/{i * 10000 + 1}.txt"
            with open(filename, "rb") as temp:
                file.write(temp.read())


# if __name__ == "__main__":
#     multi()


# TODO: Палиндром, 2 указателя
def palindrom(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
