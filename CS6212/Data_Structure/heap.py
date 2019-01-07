"""
Min Heap and Max Heap
https://www2.seas.gwu.edu/~ayoussef/cs6212/datastructures.html#heaps
By: Xiaochi (George) Li
"""
from typing import Any, Tuple, List
import unittest


class MinHeap(object):

    class _Node(object):
        key: int = None
        value: Any = None

        def __init__(self, k=None, v=None):
            self.key = k
            self.value = v

    _heap: List[_Node] = None

    def __init__(self):
        self._heap = [self._Node()]  # heap is represented by an array

    def delete_min(self) -> Tuple[int, Any]:
        min_value = (self._heap[1].key, self._heap[1].value)
        self._heap[1], self._heap[-1] = self._heap[-1], self._heap[1]  # swipe with last element
        del self._heap[-1]  # remove the last element
        index = 1
        while index*2 < len(self._heap):  # at least one child
            if index*2 + 1 < len(self._heap):  # two child
                if self._heap[index*2].key < self._heap[index*2+1].key:  # left child is smaller
                    self._heap[index], self._heap[index*2] = self._heap[index*2], self._heap[index]
                    index = index * 2
                else:
                    self._heap[index], self._heap[index * 2+1] = self._heap[index * 2+1], self._heap[index]
                    index = index * 2 + 1
            else:  # compare with the only child
                if self._heap[index].key > self._heap[index*2].key:
                    self._heap[index], self._heap[index*2] = self._heap[index*2], self._heap[index]
                    index = index * 2
        return min_value

    def insert(self, k: int, v: Any) -> None:
        self._heap.append(self._Node(k, v))  # insert the new node to the end
        index = len(self._heap) - 1
        while index != 1 and self._heap[index].key < self._heap[index//2].key:  # when smaller than the parent, swap
            self._heap[index//2], self._heap[index] = self._heap[index], self._heap[index//2]
            index = index // 2
        return

    def print_key(self) -> List[int]:
        """Print the keys for debug"""
        result = []
        for i in self._heap:
            result.append(i.key)
        return result[1:]


class MaxHeap(object):

    class _Node(object):
        key: int = None
        value: Any = None

        def __init__(self, k=None, v=None):
            self.key = k
            self.value = v

    _heap: List[_Node] = None

    def __init__(self):
        self._heap = [self._Node()]  # heap is represented by an array

    def delete_max(self) -> Tuple[int, Any]:
        max_value = (self._heap[1].key, self._heap[1].value)
        self._heap[1], self._heap[-1] = self._heap[-1], self._heap[1]  # swipe with last element
        del self._heap[-1]  # remove the last element
        index = 1
        while index*2 < len(self._heap):  # at least one child
            if index*2 + 1 < len(self._heap):  # two child
                if self._heap[index*2].key > self._heap[index*2+1].key:  # left child is larger
                    self._heap[index], self._heap[index*2] = self._heap[index*2], self._heap[index]
                    index = index * 2
                else:
                    self._heap[index], self._heap[index * 2+1] = self._heap[index * 2+1], self._heap[index]
                    index = index * 2 + 1
            else:  # compare with the only child
                if self._heap[index].key < self._heap[index*2].key:
                    self._heap[index], self._heap[index*2] = self._heap[index*2], self._heap[index]
                    index = index * 2
        return max_value

    def insert(self, k: int, v: Any) -> None:
        self._heap.append(self._Node(k, v))  # insert the new node to the end
        index = len(self._heap) - 1
        while index != 1 and self._heap[index].key > self._heap[index//2].key:  # when larger than the parent, swap
            self._heap[index//2], self._heap[index] = self._heap[index], self._heap[index//2]
            index = index // 2
        return

    def print_key(self) -> List[int]:
        """Print the keys for debug"""
        result = []
        for i in self._heap:
            result.append(i.key)
        return result[1:]


class TestMinHeap(unittest.TestCase):
    def test_insert(self):
        h = MinHeap()
        for i in range(1,12):
            h.insert(i, i)
        self.assertListEqual(h.print_key(), list(range(1, 12)))
        h.insert(0, 0)
        self.assertListEqual(h.print_key(), [0, 2, 1, 4, 5, 3, 7, 8, 9, 10, 11, 6])

    def test_delete(self):
        h = MinHeap()
        for i in range(1, 7):
            h.insert(i, i)
        self.assertTupleEqual(h.delete_min(), (1, 1))
        self.assertListEqual(h.print_key(), [2, 4, 3, 6, 5])


class TestMaxHeap(unittest.TestCase):
    def test_insert(self):
        h = MaxHeap()
        for i in range(1,7):
            h.insert(i, i)
        self.assertListEqual(h.print_key(), [6, 4, 5, 1, 3, 2])

    def test_delete(self):
        h = MaxHeap()
        for i in range(1,7):
            h.insert(i, i)
        self.assertTupleEqual(h.delete_max(), (6, 6))
        self.assertListEqual(h.print_key(), [5, 4, 2, 1, 3])


if __name__ == '__main__':
    unittest.main()
