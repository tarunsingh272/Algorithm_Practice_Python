from linked_list import ListNode, create_linked_list, print_linked_list
import unittest
from heapq import heappop, heappush

"""使用了动态向类添加方法，使算法可以调用heapq"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
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

    def mergeKLists(self, lists):
        """这个设计用到了第20题的函数，本质上是一对对地合成直到只剩一个
        因此空间复杂度只需要原始大小"""
        if len(lists) == 0:
            return None
        end = len(lists) - 1
        while end > 0:
            begin = 0
            while begin < end:
                lists[begin] = self.mergeTwoLists(lists[begin], lists[end])
                begin += 1
                end -= 1
        return lists[0]

class Solution:

    def mergeKLists(self, lists):
        """
        Time is n*k*logk, because heap operation takes logk for n*k elements
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def lt(self, other):
            return self.val < other.val
        ListNode.__lt__ = lt
        min_heap = []
        if len(lists) == 0:
            return None
        for head_node in lists:
            if head_node is not None:
                heappush(min_heap, head_node)
        dummy_head = ListNode(None)
        p: ListNode = dummy_head
        while len(min_heap) > 0:
            p.next = heappop(min_heap)
            p = p.next
            if p.next is not None:
                heappush(min_heap, p.next)
        return dummy_head.next


class Test(unittest.TestCase):
    def test(self):
        l1 = create_linked_list([1, 4, 5])
        l2 = create_linked_list([1, 3, 5])
        l3 = create_linked_list([2, 6])
        s = Solution2().mergeKLists([l1, l2, l3])
        self.assertListEqual([1, 1, 2, 3, 4, 5, 5, 6], print_linked_list(s))
