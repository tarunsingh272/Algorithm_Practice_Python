from binary_tree import TreeNode
from unittest import TestCase


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        pass


class DFS(Solution):
    """O(n) time, O(logn) space"""
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None:  # when only one sub tree exists
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


from collections import deque
class BFS(Solution):
    """O(n) time, O(n) Space
    works better when the tree is highly unbalanced"""
    def minDepth(self, root):
        queue = deque()
        if root is None:
            return 0
        queue.append(root)
        right_most = root
        depth = 1
        while len(queue) > 0:
            current: TreeNode = queue.popleft()
            if current.left is None and current.right is None:
                return depth  # 如果是左右都没有子节点的话就结束了
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
            if current == right_most:  # 判断是否已经到最右侧了，且最右侧节点必然是有子节点的
                depth += 1
                right_most = current.right if current.right is not None else current.left


class Test(TestCase):
    def test(self):
        t = TreeNode(3)
        t.left = TreeNode(9)
        t.right = TreeNode(20)
        t.right.left = TreeNode(15)
        t.right.right = TreeNode(7)
        self.assertEqual(2, BFS().minDepth(t))
        self.assertEqual(2, DFS().minDepth(t))
