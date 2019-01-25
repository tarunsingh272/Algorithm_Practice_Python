from binary_tree import TreeNode
from binary_tree import BinaryTree
from unittest import TestCase
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        Divide and Conquer
        :type nums: List[int]
        :rtype: TreeNode
        """


class Test(TestCase):
    def test(self):
        # p = TreeNode(23)
        # p.left = TreeNode(14)
        # p.right = TreeNode(67)
        # p.left.left = TreeNode(12)
        # p.left.right = TreeNode(17)
        # p.left.left.left = TreeNode(9)
        # p.left.right.right = TreeNode(19)
        # p.right.left = TreeNode(54)
        # p.right.right = TreeNode(72)
        # p.right.left.left = TreeNode(50)
        # p.right.right.right = TreeNode(76)
        p = Solution().sortedArrayToBST([9, 12, 14, 17, 19, 23, 50, 54, 67, 72, 76])
        bt = BinaryTree()
        bt.root = p
        self.assertListEqual([23, 14, 67, 12, 17, 54, 72, 9, 19, 50, 76], bt.bfs())


