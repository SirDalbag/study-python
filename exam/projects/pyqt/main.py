import sys
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton, QVBoxLayout, QWidget, QInputDialog

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager")

        self.task_list = QListWidget()
        self.load_tasks()

        self.add_button = QPushButton("Add Task")
        self.remove_button = QPushButton("Delete Task")

        self.add_button.clicked.connect(self.add_task)
        self.remove_button.clicked.connect(self.remove_task)

        layout = QVBoxLayout()
        layout.addWidget(self.task_list)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def add_task(self):
        task, status = EnterDialog.get(self)
        if status:
            self.task_list.addItem(task)
            self.save_tasks()

    def remove_task(self):
        selected_task = self.task_list.currentItem()
        if selected_task:
            self.task_list.takeItem(self.task_list.row(selected_task))
            self.save_tasks()

    def save_tasks(self):
        task_items = [self.task_list.item(i).text() for i in range(self.task_list.count())]
        with open("tasks.txt", "w") as file:
            file.write("\n".join(task_items))

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.read().splitlines()
                for task in tasks:
                    self.task_list.addItem(task)
        except Exception as error:
            self.task_list.addItem(error)

class Thread(QThread):
    task = pyqtSignal(str)
    def __init__(self, task_text):
        super().__init__()
        self.task_text = task_text

    def run(self):
        self.task.emit(self.task_text)

class EnterDialog:
    @staticmethod
    def get(parent):
        text, status = QInputDialog.getText(parent, "Add Task", "Enter Task:")
        return text, status

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    enter_dialog = EnterDialog()
    sys.exit(app.exec())
