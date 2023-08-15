import hashlib
import tkinter as tk


def send_data():
    login = entry_login.get()
    pwd = entry_pwd.get()

    hashed_pwd = hashlib.sha256(pwd.encode()).hexdigest()

    with open("less10/data.txt", "a") as file:
        file.write(f"{login} | {hashed_pwd}\n")

    entry_login.delete(0, tk.END)
    entry_pwd.delete(0, tk.END)


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("600x400")
    window.title("Login and password")

    label_login = tk.Label(window, text="Login:")
    label_login.pack()

    entry_login = tk.Entry(window)
    entry_login.pack(pady=10)

    label_pwd = tk.Label(window, text="Pаssword:")
    label_pwd.pack()

    entry_pwd = tk.Entry(window, show="*")
    entry_pwd.pack(pady=10)

    button_send = tk.Button(window, text="Send", command=send_data)
    button_send.pack(pady=10)

    window.mainloop()
