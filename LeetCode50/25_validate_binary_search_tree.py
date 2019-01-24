from binary_tree import TreeNode
from unittest import TestCase


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pass


class BruteForce(Solution):
    """
    O(n^2) when the tree is a linked list of n elements
    O(n) space
    """
    def is_sub_tree_less_than(self, p: TreeNode, val: int) -> bool:
        if p is None:
            return True
        return p.val < val and \
            self.is_sub_tree_less_than(p.left, val) and self.is_sub_tree_less_than(p.right, val)

    def is_sub_tree_greater_than(self, p: TreeNode, val: int) -> bool:
        if p is None:
            return True
        return p.val > val and \
            self.is_sub_tree_greater_than(p.left, val) and self.is_sub_tree_greater_than(p.right, val)

    def isValidBST(self, root:TreeNode) -> bool:
        if root is None:
            return True
        return self.is_sub_tree_less_than(root.left, root.val) and self.is_sub_tree_greater_than(root.right, root.val)\
            and self.isValidBST(root.left) and self.isValidBST(root.right)


class TopDownRecursion(Solution):
    """
    O(n) Time and O(n) Space
    """
    def traverse(self, root, small, large):
        if root is None:
            return True
        if small < root.val < large:
            return self.traverse(root.left, small, root.val) and self.traverse(root.right, root.val, large)
        else:
            return False

    def isValidBST(self, root):
        return self.traverse(root, -2**31, 2**31)


class InOrderTraversal(Solution):
    """应该是单调递增的
    Time: O(n), space: O(n)"""
    def __init__(self):
        self.prev = None

    def helper(self, root):
        if self.prev is None or self.prev < root.val:
            self.prev = root.val
            return True
        else:
            return False

    def isValidBST(self, root):
        if root is None:
            return True
        return self.isValidBST(root.left) and self.helper(root) and self.isValidBST(root.right)


class Test(TestCase):
    solutions = [BruteForce(), TopDownRecursion(), InOrderTraversal()]

    def test_bst(self):
        t = TreeNode(2)
        t.left = TreeNode(1)
        t.right = TreeNode(3)
        for x in self.solutions:
            self.assertTrue(x.isValidBST(t))

    def test_not_bst(self):
        t = TreeNode(5)
        t.left = TreeNode(1)
        t.right = TreeNode(4)
        t.right.left = TreeNode(3)
        t.right.right = TreeNode(6)
        for x in self.solutions:
            self.assertFalse(x.isValidBST(t))
