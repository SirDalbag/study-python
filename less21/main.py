import tkinter as tk
import sqlite3


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
        candidates = query(
            "SELECT id, name_candidate, group_candidate FROM candidates", ()
        )
        with open("less21/candidates.txt", "w") as file:
            for candidate in candidates:
                id, name, group = candidate
                file.write(
                    f"ID: {id}, Name Candidate: {name}, Group Candidate: {group}\n"
                )
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

    button_frame = tk.Frame(window)
    button_frame.pack()

    save_button = tk.Button(button_frame, text="Save", command=save)
    save_button.pack(side=tk.LEFT, padx=10)

    export_button = tk.Button(button_frame, text="Export", command=export)
    export_button.pack(side=tk.LEFT)

    status_label = tk.Label(window, text="Status: 0")
    status_label.pack()

    window.mainloop()
