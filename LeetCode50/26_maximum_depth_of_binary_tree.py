from binary_tree import TreeNode
from unittest import TestCase

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root):
        """
        Time O(n), space O(logn)
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class Test(TestCase):
    def test(self):
        t = TreeNode(3)
        t.left = TreeNode(9)
        t.right = TreeNode(20)
        t.right.left = TreeNode(15)
        t.right.right = TreeNode(7)
        self.assertEqual(3, Solution().maxDepth(t))
