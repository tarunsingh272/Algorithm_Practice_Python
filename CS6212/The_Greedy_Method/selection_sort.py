"""
Selection Sort
https://www2.seas.gwu.edu/~ayoussef/cs6212/greedy.html#firstapplication
By: Xiaochi (George) Li
"""
from typing import List, Union
import unittest


def selection_sort(array:List[Union[int, float]], reverse:bool = False) -> None:
    if not reverse:
        for i in range(len(array)):
            smallest_value: [int, float] = array[i]
            smallest_index: int = i
            for j in range(i+1, len(array)):
                if array[j] < smallest_value:
                    smallest_value = array[j]
                    smallest_index = j
            array[i], array[smallest_index] = array[smallest_index], array[i]
    else:
        for i in range(len(array)):
            largest_value: [int, float] = array[i]
            largest_index: int = i
            for j in range(i+1, len(array)):
                if array[j] > largest_value:
                    largest_value = array[j]
                    largest_index = j
            array[i], array[largest_index] = array[largest_index], array[i]


class TestSort(unittest.TestCase):
    def test_not_reverse(self):
        from random import randint
        array = [randint(1, 100) for _ in range(100000)]
        print(array)
        expected = sorted(array, reverse=False)
        selection_sort(array, reverse=False)
        self.assertListEqual(expected, array)

    def test_reverse(self):
        from random import randint
        array2 = [randint(1, 100) for _ in range(100000)]
        expected2 = sorted(array2, reverse=True)
        selection_sort(array2, reverse=True)
        self.assertListEqual(expected2, array2)
