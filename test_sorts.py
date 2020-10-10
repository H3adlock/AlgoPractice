import random
from Sorting import Sorting

testCases = []
# small testcase
testCases.append(random.sample(range(-99, 99), 10))
# medium testcase
testCases.append(random.sample(range(-999, 999), 1000))
# large testcase
testCases.append(random.sample(range(-9999, 9999), 10000))

for testCase in testCases:
    n = len(testCase)
    s = Sorting()
    print("Initial unsorted list: {}".format(testCase))
    s.bubbleSort(testCase, n)
    s.selectionSort(testCase, n)
    s.insertionSort(testCase, n)
    s.mergeSort(testCase, n)
    s.radixSort(testCase, n)
    s.heapSort(testCase, n)
    s.quicksort(testCase, n)
    print("\n\n")
