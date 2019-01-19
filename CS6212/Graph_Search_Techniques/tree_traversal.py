"""
Tree Traversal Technique Implementation
By: Xiaochi (George) Li
https://www2.seas.gwu.edu/~ayoussef/cs6212/graphsearch.html#treetraversal
    class _Node(object):

        key: int = None
        value: Any = None
        left = None
        right = None

        def __init__(self, k=None, v=None):
            self.key = k
            self.value = v
"""

from Data_Structure.BST import BST as Tree
from Data_Structure.BST import TestBST
from typing import List


class TreeTraversal(object):
    _trace: List = None

    def __init__(self):
        self._trace = []

    def visit(self, p: Tree._Node):
        self._trace.append(p.value)

    def in_order_traversal(self, p: Tree._Node):
        if p is None:
            return
        self.in_order_traversal(p.left)
        self.visit(p)
        self.in_order_traversal(p.right)

    def pre_order_traversal(self, p: Tree._Node):
        if p is None:
            return
        self.visit(p)
        self.pre_order_traversal(p.left)
        self.pre_order_traversal(p.right)

    def post_order_traversal(self, p: Tree._Node):
        if p is None:
            return
        self.post_order_traversal(p.left)
        self.post_order_traversal(p.right)
        self.visit(p)

    def trace(self):
        return self._trace


class TestTreeTraversal(TestBST):
    def test_in_order(self):
        tree = self.create_tree()
        tt = TreeTraversal()
        tt.in_order_traversal(tree._root)
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7], tt.trace())

    def test_pre_order(self):
        tree = self.create_tree()
        tt = TreeTraversal()
        tt.pre_order_traversal(tree._root)
        self.assertListEqual([4, 2, 1, 3, 6, 5, 7], tt.trace())

    def test_post_order(self):
        tree = self.create_tree()
        tt = TreeTraversal()
        tt.post_order_traversal(tree._root)
        self.assertListEqual([1, 3, 2, 5, 7, 6, 4], tt.trace())
