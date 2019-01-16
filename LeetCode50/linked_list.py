"""Linked list data structure and helper function for easy debug"""
from typing import List
import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_linked_list(lst: List) -> ListNode:
    head = ListNode(lst[0])
    p = head

    for i in lst[1:]:
        p.next = ListNode(i)
        p = p.next
    return head


def print_linked_list(p: ListNode) -> List:
    lst = []
    while p is not None:
        lst.append(p.val)
        p = p.next
    return lst


class Test(unittest.TestCase):
    def test(self):
        linked_list = create_linked_list([1, 2, 3])
        self.assertListEqual([1, 2, 3], print_linked_list(linked_list))
