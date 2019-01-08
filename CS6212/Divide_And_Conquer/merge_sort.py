"""
Merge Sort Ascending and Descending
Implemented in "Procedure" style
https://www2.seas.gwu.edu/~ayoussef/cs6212/divide-and-conquer.html#1stapplication
By: Xiaochi (George) Li
"""

from typing import List, Union
import unittest


def merge(array: List[Union[int, float]],
          i: int, j: int, reverse: bool):
    """"merge procedure combine the two sorted array """
    k: int = (i+j) // 2  # k is the mid point of the array
    u: int = i  # u will scan left part
    v: int = k+1  # v will scan right part
    w: int = u  # w is the index of merged output
    copied: List = [array[i] for i in range(len(array))]  # a copy of unmerged array so we can make inplace merge
    if not reverse:  # ascending
        while u <= k and v <= j:
            if copied[u] < copied[v]:
                array[w] = copied[u]
                u += 1
                w += 1
            else:
                array[w] = copied[v]
                v += 1
                w += 1
    else:  # descending
        while u <= k and v <= j:
            if copied[u] > copied[v]:  # reverse means take the larger one
                array[w] = copied[u]
                u += 1
                w += 1
            else:
                array[w] = copied[v]
                v += 1
                w += 1
    if u > k:  # the right part is not empty
        while w <= j:  # put copied[v:j] into array[w:j]
            array[w] = copied[v]
            v += 1
            w += 1
    elif v > j:
        while w <= j:  # put copied[u:k] to array[w:j]
            array[w] = copied[u]
            u += 1
            w += 1


def merge_sort(array: List[Union[int, float]],
               i: int = 0, j: int = None, reverse: bool = False) -> None:
    """merge sort recursive procedure, use parameter with default value as entry point
    the procedure change the content of the passed in array and has no return"""

    if j is None:  # when the last element is not specified, only True when call from outside
        j = len(array) - 1
    if i != j:  # base case is do nothing, forget base case will cause endless recursion
        merge_sort(array, i, (i+j) // 2, reverse)  # remember to take the reverse argument
        merge_sort(array, (i+j)//2+1, j, reverse)
        merge(array, i, j, reverse)


# class TestSort(unittest.TestCase):
#     def test_not_reverse(self):
#         from random import randint
#         array = [randint(1, 100) for _ in range(10000)]
#         expected = sorted(array, reverse=False)
#         merge_sort(array,reverse=False)
#         self.assertListEqual(expected, array)
#
#     def test_reverse(self):
#         from random import randint
#         array2 = [randint(1, 100) for _ in range(10000)]
#         expected2 = sorted(array2, reverse=True)
#         merge_sort(array2, reverse=True)
#         self.assertListEqual(expected2, array2)

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def speed_test(size):
    from random import randint
    import timeit
    array = [randint(1, 100) for _ in range(size)]
    start = timeit.default_timer()
    # x = [[array[i] for i in range(len(array))]]
    # mergeSort(array)
    merge_sort(array)
    time_elapsed = timeit.default_timer() - start
    return time_elapsed


for i in [5000*x for x in range(4, 5)]:
    print(i, speed_test(i))

