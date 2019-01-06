"""
First In First Out Queue
Algorithms 4th P151
By: Xiaochi (George) Li
"""
from typing import Any
import unittest


class Queue(object):
    class _Node(object):
        item = None
        next = None

    _first: _Node = None
    _last: _Node = None
    _n: int = None

    def __init__(self):
        self._n = 0

    def enqueue(self, item:Any) -> None:
        old_last = self._last
        self._last = self._Node()
        self._last.item = item

        if self.is_empty():
            self._first = self._last
        else:
            old_last.next = self._last
        self._n += 1

    def dequeue(self) -> Any:
        item = self._first.item
        self._first = self._first.next
        self._n -= 1
        if self.is_empty():
            self._last = None
        return item

    def is_empty(self) -> bool:
        return self._first is None

    def size(self) -> int:
        return self._n


class _TestQueue(unittest.TestCase):
    def test(self):
        test_input = ['to', 'be', 'or', 'not', 'to', '-', 'be', '-', '-', 'that', '-', '-', '-', 'is']
        q = Queue()
        self.assertTrue(q.is_empty())
        test_output = []
        for i in test_input:
            if not i == '-':
                q.enqueue(i)
            else:
                test_output.append(q.dequeue())
        expected_output = ['to', 'be', 'or', 'not', 'to', 'be']
        print(test_output)
        self.assertListEqual(expected_output, test_output)
        self.assertEqual(q.size(), 2)


if __name__ == '__main__':
    unittest.main()
