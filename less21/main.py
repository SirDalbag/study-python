import tkinter as tk
from tkinter import scrolledtext
import sqlite3
import smtplib as smtp


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


def select():
    return query("SELECT id, name_candidate, group_candidate FROM candidates", ())


def save():
    try:
        query(
            "INSERT INTO candidates (name_candidate, group_candidate) VALUES (?,?)",
            (name_entry.get(), group_entry.get()),
        )
        status_label.config(text="Status: Success!")
    except Exception as error:
        status_label.config(text=f"Status: {error}")


def export():
    try:
        candidates = select()
        with open("less21/candidates.txt", "w") as file:
            for candidate in candidates:
                id, name, group = candidate
                file.write(f"ID: {id}, Name: {name}, Group: {group}\n")
        status_label.config(text="Status: Success!")
    except Exception as error:
        status_label.config(text=f"Status: {error}")


def display():
    try:
        candidates = select()

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

        status_label.config(text="Status: Success!")
    except Exception as error:
        status_label.config(text=f"Status: {error}")


def message():
    try:
        email_from = "eevee.cycle@yandex.com"
        password = "mawfgptgdehfcwyi"
        email_to = "sir.dalbag@gmail.com"
        subject = "Candidates"

        count = query("SELECT count(*) FROM candidates", (), False)[0]
        text = f"Candidates Count: {count}."

        message = f"From: {email_from}\nTo: {email_to}\nSubject: {subject}\n\n{text}"

        server = smtp.SMTP_SSL("smtp.yandex.com:465")
        server.login(email_from, password)
        server.sendmail(email_from, email_to, message)
        server.quit()
        status_label.config(text="Status: Success!")
    except Exception as error:
        status_label.config(text=f"Status: {error}")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("List Candidates")
    window.geometry("300x300")

    label_frame = tk.Frame(window)
    label_frame.pack()

    name_label = tk.Label(label_frame, text="Name Candidate:")
    name_label.pack()

    name_entry = tk.Entry(label_frame)
    name_entry.pack(pady=5)

    group_label = tk.Label(label_frame, text="Group Candidate:")
    group_label.pack()

    group_entry = tk.Entry(label_frame)
    group_entry.pack(pady=10)

    first_button_frame = tk.Frame(window)
    first_button_frame.pack()

    save_button = tk.Button(first_button_frame, text="Save", command=save)
    save_button.pack(side=tk.LEFT, padx=10)

    export_button = tk.Button(first_button_frame, text="Export", command=export)
    export_button.pack(side=tk.LEFT)

    second_button_frame = tk.Frame(window)
    second_button_frame.pack(pady=10)

    candidates_button = tk.Button(
        second_button_frame, text="Candidates", command=display
    )
    candidates_button.pack(side=tk.LEFT, padx=10)

    message_button = tk.Button(
        second_button_frame, text="Send Message", command=message
    )
    message_button.pack(side=tk.LEFT)

    status_label = tk.Label(window, text="Status: 0")
    status_label.pack()

    window.mainloop()
