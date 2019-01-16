from linked_list import ListNode, create_linked_list, print_linked_list
import unittest
"""标准答案使用了dummy node来避免特殊处理链表的头（也就是我的方法），值得学习"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class BetterSolution:
    def swapPairs(self, head):
        dummy: ListNode = ListNode(0)
        dummy.next = head
        p = head
        prev = dummy
        while p is not None and p.next is not None:
            q = p.next
            r = p.next.next
            prev.next = q
            q.next = p
            p.next = r
            prev = p
            p = r
        return dummy.next


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # eg. 1->2->3->4->None
        p:ListNode = head  # p->1
        first_node:ListNode = True
        prev_p: ListNode = None
        while p is not None and p.next is not None:
            if first_node:
                head = p.next  # head -> 2
                first_node = False
            else:
                prev_p.next = p.next  # make 1 -> 4 instead of 3
            temp = p.next.next  # temp -> 3
            p.next.next = p  # 2(1.next) -> 1
            p.next = temp  # 1 -> 3 this line takes care of odd situation, eg. ends in 3

            prev_p = p  # prev -> 1
            p = p.next  # p -> 2
            # first loop: 2 -> 1 -> 3 -> 4
            # second loop: 2 -> 1 -> 4 -> 3
        return head


class Test(unittest.TestCase):
    def test(self):
        s = BetterSolution()
        lst = create_linked_list([1, 2, 3, 4])
        self.assertListEqual([2, 1, 4, 3], print_linked_list(s.swapPairs(lst)))
