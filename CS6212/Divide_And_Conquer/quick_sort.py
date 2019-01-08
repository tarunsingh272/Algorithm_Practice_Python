"""
Quick Sort Ascending and Descending
https://www2.seas.gwu.edu/~ayoussef/cs6212/divide-and-conquer.html#2ndapplication
By: Xiaochi(George)Li
"""
from typing import List, Union
import unittest


def partition(array: List[Union[int, float]],
              p: int, q: int, reverse: bool = False) -> int:
    a = array[p]
    i: int = p
    j: int = q
    if not reverse:
        while i <= j:
            while i <= q and array[i] <= a:
                i += 1
            while array[j] > a:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        array[p], array[j] = array[j], array[p]

    else:
        while i <= j:
            while i <= q and array[i] >= a:
                i += 1
            while array[j] < a:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        array[p], array[j] = array[j], array[p]
    return j


def quick_sort(array: List[Union[int, float]],
               p: int = 0, q: int = None, reverse: bool = False) -> None:
    if q is None:  # entry point from outside
        q = len(array) - 1
    if p != q:  # Base case, when p == q, do nothing
        r: int = partition(array, p, q, reverse)
        """Fix of a weird bug: I think the reason is that when r is at the head or the tail,
        it indicates that we should not sort the left(<r) or right(>r) sub array, because they don't exist
        otherwise, will cause an error of index out of range"""
        if p < r:
            quick_sort(array, p, r - 1, reverse)
        if r < q:
            quick_sort(array, r + 1, q, reverse)


class TestSort(unittest.TestCase):
    def test_not_reverse(self):
        from random import randint
        array = [randint(1, 100) for _ in range(100)]
        # array = [3,1,2]
        expected = sorted(array, reverse=False)
        quick_sort(array, reverse=False)
        self.assertListEqual(expected, array)

    def test_reverse(self):
        from random import randint
        array2 = [randint(1, 100) for _ in range(100)]
        expected2 = sorted(array2, reverse=True)
        quick_sort(array2, reverse=True)
        self.assertListEqual(expected2, array2)
