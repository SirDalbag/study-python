import tkinter as tk
from tkinter import ttk
import requests, json
import concurrent.futures


def get_post(k: int):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{k}")
    with open(f"less19/posts{k}.json", "w") as file:
        json.dump(response.json(), file)


def threading(k: int):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(1, k + 1):
            executor.submit(get_post, i)


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("300x300")
    window.title("Download Posts")

    label = ttk.Label(window, text="Posts:")
    label.pack()

    entry = ttk.Entry(window)
    entry.pack()

    button = ttk.Button(
        window, text="Download", command=lambda: threading(int(entry.get()))
    )
    button.pack()

    window.mainloop()
