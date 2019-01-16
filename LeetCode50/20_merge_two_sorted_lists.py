"""用dummy node来使代码更加简洁，值得学习"""

from linked_list import ListNode, create_linked_list, print_linked_list
import unittest

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        p = dummy_head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1 is not None:
            p.next = l1
        if l2 is not None:
            p.next = l2
        return dummy_head.next


class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        l1 = create_linked_list([1, 2, 4])
        l2 = create_linked_list([1, 3, 4])
        self.assertListEqual([1, 1, 2, 3, 4, 4], print_linked_list(s.mergeTwoLists(l1, l2)))
