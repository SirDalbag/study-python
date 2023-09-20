import tkinter as tk
from tkinter import scrolledtext
import sqlite3
import smtplib as smtp


class Database:
    @staticmethod
    def query(sql: str, args: tuple, many: bool = True) -> list[tuple] or tuple:
        try:
            with sqlite3.connect("less21/database.db") as connection:
                cursor = connection.cursor()
                cursor.execute(sql, args)
                if many:
                    return cursor.fetchall()
                return cursor.fetchone()
        except Exception as error:
            print(error)

    @staticmethod
    def select():
        return Database.query(
            "SELECT id, name_candidate, group_candidate FROM candidates", ()
        )

    @staticmethod
    def insert(name: str, group: str):
        return Database.query(
            "INSERT INTO candidates (name_candidate, group_candidate) VALUES (?,?)",
            (name, group),
        )


class App:
    def __init__(self, window):
        self.window = window
        window.title("List Candidates")
        window.geometry("300x300")

        label_frame = tk.Frame(window)
        label_frame.pack()

        name_label = tk.Label(label_frame, text="Name Candidate:")
        name_label.pack()

        self.name_entry = tk.Entry(label_frame)
        self.name_entry.pack(pady=5)

        group_label = tk.Label(label_frame, text="Group Candidate:")
        group_label.pack()

        self.group_entry = tk.Entry(label_frame)
        self.group_entry.pack(pady=10)

        first_button_frame = tk.Frame(window)
        first_button_frame.pack()

        save_button = tk.Button(first_button_frame, text="Save", command=self.save)
        save_button.pack(side=tk.LEFT, padx=10)

        export_button = tk.Button(
            first_button_frame, text="Export", command=self.export
        )
        export_button.pack(side=tk.LEFT)

        second_button_frame = tk.Frame(window)
        second_button_frame.pack(pady=10)

        candidates_button = tk.Button(
            second_button_frame, text="Candidates", command=self.display
        )
        candidates_button.pack(side=tk.LEFT, padx=10)

        message_button = tk.Button(
            second_button_frame, text="Send Message", command=self.message
        )
        message_button.pack(side=tk.LEFT)

        self.status_label = tk.Label(window, text="Status: 0")
        self.status_label.pack()

    def save(self):
        try:
            Database.insert(self.name_entry.get(), self.group_entry.get())
            self.status_label.config(text="Status: Success!")
        except Exception as error:
            self.status_label.config(text=f"Status: {error}")

    def export(self):
        try:
            candidates = Database.select()
            with open("less21/candidates.txt", "w") as file:
                for candidate in candidates:
                    id, name, group = candidate
                    file.write(f"ID: {id}, Name: {name}, Group: {group}\n")
            self.status_label.config(text="Status: Success!")
        except Exception as error:
            self.status_label.config(text=f"Status: {error}")

    def display(self):
        try:
            candidates = Database.select()

            display_window = tk.Toplevel(window)
            display_window.title("Candidates")
            display_window.geometry("300x300")

            display_text = scrolledtext.ScrolledText(
                display_window, width=40, height=10, wrap=tk.WORD
            )
            display_text.pack(padx=10, pady=10)

            for candidate in candidates:
                display_text.insert(
                    tk.END,
                    f"ID: {candidate[0]}, Name: {candidate[1]}, Group: {candidate[2]}\n\n",
                )

            self.status_label.config(text="Status: Success!")
        except Exception as error:
            self.status_label.config(text=f"Status: {error}")

    def message(self):
        try:
            email_from = "eevee.cycle@yandex.com"
            password = "mawfgptgdehfcwyi"
            email_to = "sir.dalbag@gmail.com"
            subject = "Candidates"

            count = Database.query("SELECT count(*) FROM candidates", (), False)[0]
            text = f"Candidates Count: {count}."

            message = (
                f"From: {email_from}\nTo: {email_to}\nSubject: {subject}\n\n{text}"
            )

            server = smtp.SMTP_SSL("smtp.yandex.com:465")
            server.login(email_from, password)
            server.sendmail(email_from, email_to, message)
            server.quit()
            self.status_label.config(text="Status: Success!")
        except Exception as error:
            self.status_label.config(text=f"Status: {error}")


if __name__ == "__main__":
    window = tk.Tk()
    app = App(window)
    window.mainloop()
