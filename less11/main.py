import tkinter as tk
from tkinter import ttk
import time, random
import requests
import concurrent, asyncio, aiohttp


def time_measurement(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} - {round(time.perf_counter() - start_time, 2)}")

        return result

    return wrapper


url = "https://picsum.photos/320/240/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) "
    "Chrome/102.0.0.0 Safari/537.36"
}


def load_image():
    with open(f"less11/image{random.randint(1, 10000000)}.jpg", "wb") as file:
        file.write(requests.get(url=url, headers=headers).content)


async def async_load_image():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as response:
            data = await response.read()
            with open(f"less11/image{random.randint(1, 10000000)}.jpg", "wb") as file:
                file.write(data)


@time_measurement
def sync_load_images():
    for _ in range(10):
        load_image()


@time_measurement
def async_load_images():
    async def async_task_inline():
        await asyncio.gather(*[async_load_image() for _ in range(10)])

    asyncio.run(async_task_inline())


@time_measurement
def threading_load_images():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(10):
            executor.submit(load_image)


@time_measurement
def multiprocessing_load_images():
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        for _ in range(10):
            executor.submit(load_image)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Loаd Image")
    window.geometry("600x400")

    sync_btn = ttk.Button(text="Sync", command=sync_load_images)
    sync_btn.pack()

    async_btn = ttk.Button(text="Async", command=async_load_images)
    async_btn.pack()

    threading_btn = ttk.Button(text="Threading", command=threading_load_images)
    threading_btn.pack()

    multiprocessing_btn = ttk.Button(
        text="Multiprocessing", command=multiprocessing_load_images
    )
    multiprocessing_btn.pack()

    window.mainloop()
