import time
import random


# Замер времени сортировок.
class TimeSorting:
    @staticmethod
    def display(func, array):
        start = time.perf_counter()
        func(array)
        print(f"{func.__name__} : {round(time.perf_counter() - start, 10)}")


def bubble_sort(array):
    lenght = len(array)
    for i in range(lenght - 1):
        for j in range(lenght - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def selection_sort(array):
    lenght = len(array)
    for i in range(lenght):
        min = i
        for j in range(i + 1, lenght):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def merge_sort(array):
    lenght = len(array)
    if lenght > 1:
        mid = lenght // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def quick_sort(array):
    lenght = len(array)
    if lenght > 1:
        pivot = array[lenght - 1]
        i = j = 0
        while i < lenght - 1:
            if array[i] < pivot:
                array[j], array[i] = array[i], array[j]
                j += 1
            i += 1
        array[j], array[lenght - 1] = array[lenght - 1], array[j]
        quick_sort(array[:j])
        quick_sort(array[j + 1 :])


if __name__ == "__main__":
    array = [random.randint(0, 100) for _ in range(100)]
    TimeSorting.display(bubble_sort, array)
    TimeSorting.display(selection_sort, array)
    TimeSorting.display(insertion_sort, array)
    TimeSorting.display(merge_sort, array)
    TimeSorting.display(quick_sort, array)
