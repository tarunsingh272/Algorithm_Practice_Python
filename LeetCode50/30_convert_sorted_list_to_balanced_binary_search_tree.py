"""挺难的Bottom-up方法，需要画Recursion Tree复习逻辑
Time o(n) Space O(logn)"""

from linked_list import ListNode, create_linked_list
from binary_tree import TreeNode, BinaryTree
from unittest import TestCase

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.list: ListNode = None

    def helper(self, start: int, end: int) -> TreeNode:
        if start > end:
            return None
        mid = (start + end) // 2
        left_child: TreeNode = self.helper(start, mid-1)
        parent = TreeNode(self.list.val)  # 按顺序读取链表中的元素并插入树
        parent.left = left_child
        self.list = self.list.next
        parent.right = self.helper(mid+1, end)
        return parent

    def sortedListToBST(self, head) -> TreeNode:
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        n: int = 0
        p: ListNode = head
        while p is not None:
            p = p.next
            n += 1
        self.list = head
        return self.helper(0, n-1)


class Test(TestCase):
    def test(self):
        linked_list = create_linked_list([-10, -3, 0, 5, 9])
        t = Solution().sortedListToBST(linked_list)
        bt = BinaryTree()
        bt.root = t
        self.assertListEqual([0, -10, 5, -3, 9], bt.bfs())
