import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


class Sorting:
    @timer
    def bubbleSort(self, arr, n):
        for i in range(1, n):
            for j in range(0, n - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"Sorted list: {arr}")

    @timer
    def insertionSort(self, arr, n):
        pass

    @timer
    def selectionSort(self, arr, n):
        pass

    @timer
    def mergeSort(self, arr, n):
        pass

    @timer
    def radixSort(self, arr, n):
        pass

    @timer
    def heapSort(self, arr, n):
        pass

    @timer
    def quicksort(self, arr, n):
        pass
