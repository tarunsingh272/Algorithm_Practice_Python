from typing import List
from collections import deque
from unittest import TestCase

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree(object):
    root: TreeNode = None

    def __init__(self):
        self.root: TreeNode = None

    def bfs(self) -> List:
        """Breadth First Search in BST, for visualization"""
        visit = []
        q = deque()
        p = self.root
        q.append(p)
        # visit.append(p.val)
        while len(q) > 0:
            x: TreeNode = q.popleft()
            visit.append(x.val)
            if x.left is not None:
                q.append(x.left)
            #     visit.append(x.left.val)
            # else:
            #     visit.append('-')
            if x.right is not None:
                q.append(x.right)
            #     visit.append(x.right.val)
            # else:
            #     visit.append('-')

        return visit

    def create_binary_tree_from_list(self, lst: List) -> TreeNode:
        pass


class Test(TestCase):
    def test_bfs(self):
        t = TreeNode(1)
        t.left = TreeNode(2)
        t.right = TreeNode(2)
        t.left.left = TreeNode(3)
        t.left.right = TreeNode(3)
        t.left.left.left = TreeNode(4)
        t.left.left.right = TreeNode(4)
        bt = BinaryTree()
        bt.root = t
        self.assertListEqual([1, 2, 2, 3, 3, 4, 4], bt.bfs())
