from binary_tree import TreeNode
from unittest import TestCase

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pass


class BruteForceTopDownRecursion(Solution):
    """Time O(n^2) because max depth is recalculated every time
    Space O(n)"""
    def max_depth(self, root: TreeNode):
        if root is None:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1

    def isBalanced(self, root):
        if root is None:
            return True
        if abs(self.max_depth(root.left) - self.max_depth(root.right)) <= 1 and self.isBalanced(root.left)\
                and self.isBalanced(root.right):
            return True
        else:
            return False


class BottomUp(Solution):
    def max_depth(self, root: TreeNode):
        if root is None:
            return 0
        left = self.max_depth(root.left)
        right = self.max_depth(root.right)
        if abs(left - right) > 1 or left is False or right is False:
            return False
        else:
            return max(left, right) + 1

    def isBalanced(self, root):
        return self.max_depth(root) is not False


class Test(TestCase):
    def test_true(self):
        t = TreeNode(3)
        t.left = TreeNode(9)
        t.right = TreeNode(20)
        t.right.left = TreeNode(15)
        t.right.left = TreeNode(7)
        self.assertTrue(BruteForceTopDownRecursion().isBalanced(t))
        self.assertTrue(BottomUp().isBalanced(t))

    def test_false(self):
        t = TreeNode(1)
        t.left = TreeNode(2)
        t.right = TreeNode(2)
        t.left.left = TreeNode(3)
        t.left.right = TreeNode(3)
        t.left.left.left = TreeNode(4)
        t.left.left.right = TreeNode(4)
        self.assertFalse(BruteForceTopDownRecursion().isBalanced(t))
        self.assertFalse(BottomUp().isBalanced(t))
