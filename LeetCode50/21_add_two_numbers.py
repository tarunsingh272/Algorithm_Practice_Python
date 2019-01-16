"""这道题要注意进位问题，两个数字可能不同长度，因此要用if来避免空指针，别的没啥难度"""

from linked_list import ListNode, create_linked_list, print_linked_list
import unittest

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p = dummy
        add_on = 0
        while l1 is not None or l2 is not None:
            x = 0 if l1 is None else l1.val
            y = 0 if l2 is None else l2.val
            next_digit = x + y + add_on
            if next_digit < 10:
                p.next = ListNode(next_digit)
                add_on = 0
            else:
                p.next = ListNode(next_digit % 10)
                add_on = 1
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            p = p.next
        if add_on > 0:
            p.next = ListNode(1)
        return dummy.next


class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        l1 = create_linked_list([9, 9])
        l2 = create_linked_list([1])
        result = print_linked_list(s.addTwoNumbers(l1, l2))
        self.assertListEqual([0, 0, 1], result)
