from typing import List
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree(object):
    _root: TreeNode = None

    def __init__(self):
        _root:TreeNode = None

    def bfs(self) -> List:
        """Breadth First Search in BST, for visualization"""
        visit = []
        q = deque()
        p = self._root
        q.append(p)
        while len(q) > 0:
            x = q.popleft()
            visit.append(x.value)
            if x.left is not None:
                q.append(x.left)
            if x.right is not None:
                q.append(x.right)
        return visit

    def create_binary_tree_from_list(self, lst: List) -> TreeNode:
        pass

