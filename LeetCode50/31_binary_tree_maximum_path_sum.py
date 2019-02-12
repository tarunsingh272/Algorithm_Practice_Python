from binary_tree import TreeNode
from unittest import TestCase

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    _max_sum = None
    _max_root = None

    def find_max(self, root: TreeNode) -> int:
        left_value = self.find_max(root.left) if root.left is not None else 0
        right_value = self.find_max(root.right) if root.right is not None else 0
        max_path = root.val + left_value + right_value  # 可能的最大值
        if self._max_sum < max_path:
            self._max_sum = max_path
            self._max_root = root.val
        ret = root.val + max(left_value, right_value)  # 本树作为子树时，只能选择左枝或者右枝
        return ret if ret >= 0 else 0

    def maxPathSum(self, root: TreeNode) -> int:
        self._max_sum = -2**31
        self.find_max(root)
        print(self._max_root)
        return self._max_sum


class Test(TestCase):
    def test(self):
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        s = Solution()
        self.assertEqual(42, s.maxPathSum(root))
