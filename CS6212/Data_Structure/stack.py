"""
Last In Fist Out Stack
Algorithms 4th. P149
By: Xiaochi (George) Li
"""
from typing import Any
import unittest


class Stack(object):
    """Push down Stack Linked-list implementation"""

    class _Node(object):
        """Private class of Linked List Node"""
        item = None
        next = None

    _n: int = None
    _first: _Node = None

    def __init__(self)->None:
        """Create an empty stack"""
        self._n = 0
        self._first = None

    def push(self, item: Any):
        """Add an item"""
        old_first = self._first
        self._first = self._Node()
        self._first.item = item
        self._first.next = old_first
        self._n += 1

    def pop(self) ->Any:
        """Remove the most recently added item"""
        item = self._first.item
        self._first = self._first.next
        self._n -= 1
        return item

    def is_empty(self)->bool:
        """Is the stack empty?"""
        return self._first is None

    def size(self)->int:
        """number of items in the stack"""
        return self._n


class _TestStack(unittest.TestCase):
    def test(self):
        test_input = ['to', 'be', 'or', 'not', 'to', '-', 'be', '-', '-', 'that', '-', '-', '-', 'is']
        s = Stack()
        self.assertTrue(s.is_empty())
        test_output = []
        for i in test_input:
            if not i == '-':
                s.push(i)
            else:
                test_output.append(s.pop())
        expected_output = ['to', 'be', 'not', 'that', 'or', 'be']
        print(test_output)
        self.assertListEqual(expected_output, test_output)
        self.assertEqual(s.size(), 2)


if __name__ == '__main__':
    unittest.main()
