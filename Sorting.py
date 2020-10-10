import functools
import time


def timer(func):
    # @functools.wraps(func)
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
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # print(f"Sorted list: {arr}")

    @timer
    def insertionSort(self, arr, n):
        for i in range(1, n):

            key = arr[i]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        # print(f"Sorted list: {arr}")

    @timer
    def selectionSort(self, arr, n):
        for i in range(n):

            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, n):
                if arr[min_idx] > arr[j]:
                    min_idx = j

                    # Swap the found minimum element with
            # the first element
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # print(f"Sorted list: {arr}")

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
