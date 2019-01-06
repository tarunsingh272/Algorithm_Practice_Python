"""
Binary Search Tree
https://www2.seas.gwu.edu/~ayoussef/cs6212/datastructures.html#bst
By: Xiaochi (George) Li
"""

import unittest
from Data_Structure.queue_ import Queue
from typing import Any, List


class BST(object):
    """Basic Binary Search Tree, not always balanced"""
    class _Node(object):
        """Node of the tree"""
        key: int = None
        value: Any = None
        left = None
        right = None

        def __init__(self, k=None, v=None):
            self.key = k
            self.value = v

    _root: _Node = None

    def __init__(self):
        """Create an empty BST"""
        self._root = self._Node()

    def search(self, a: int) ->Any:
        """Search element in the BST with key"""
        p:BST._Node = self._root
        if p.key is None:  # empty tree
            return None
        while p is not None and p.key != a:
            if a <= p.key:
                p = p.left
            else:
                p = p.right
        if p is not None:  # found the key
            return p.value
        else:
            return None

    def insert(self, a: int, v: Any) -> None:
        """Insert new element into a BST"""
        done: bool = False
        p: BST._Node = self._root
        if p.key is None:  # empty tree
            p.key = a
            p.value = v
            return
        while not done:
            if a <= p.key:  # go left
                if p.left is not None:
                    p = p.left  # continue go left
                else:
                    p.left = self._Node(a, v)
                    done = True
            else:
                if p.right is not None:
                    p = p.right  # continue go right
                else:
                    p.right = self._Node(a, v)
                    done = True

    def delete(self, a: int) -> None:
        """Delete element from BST"""
        p: BST._Node = self._root  # p is the node we found the key
        q: BST._Node = None  # q is the parent node of p
        direction: bool = False  # if p is left child then False, else True
        while p is not None and p.key != a:
            if a <= p.key:  # go left
                q = p
                p = p.left
                direction = False
            else:
                q = p
                p = p.right
                direction = True
        if p is None:  # Not found
            return
        elif p.left is None and p.right is None:  # p has no child, delete p
            if not direction:
                q.left = None
            else:
                q.right = None
        elif p.left is None:  # p only has right child, create a shortcut
            if not direction:
                q.left = p.right
            else:
                q.right = p.right
        elif p.right is None:  # p only has left child, create a shortcut
            if not direction:
                q.left = p.left
            else:
                q.right = p.left
        else:  # p has two children, find the maximum node in p's left subtree
            s: BST._Node = p.left
            q = p  # q become the parent of s
            direction = False  # left is False
            while s.right is not None:  # go to the most right leaf(maximum)
                q = s
                s = s.right
                direction = True

            p.key = s.key  # replace p by s
            p.value = s.value

            if s.left is None:  # s has no child
                if not direction:
                    q.left = None
                else:
                    q.right = None
                return
            else:  # s has left child
                if not direction:
                    q.left = s.left
                else:
                    q.right = s.left
                return



    def bfs(self) -> List:
        """Breadth First Search in BST, for visualization"""
        visit = []
        q = Queue()
        p = self._root
        q.enqueue(p)
        while not q.is_empty():
            x = q.dequeue()
            visit.append(x.value)
            if x.left is not None:
                q.enqueue(x.left)
            if x.right is not None:
                q.enqueue(x.right)
        return visit


class TestBST(unittest.TestCase):
    def create_tree(self) ->BST:
        t = BST()
        t._root = t._Node(4, 4)
        t._root.left = t._Node(2, 2)
        t._root.right = t._Node(6, 6)
        t._root.left.left = t._Node(1, 1)
        t._root.left.right = t._Node(3, 3)
        t._root.right.left = t._Node(5, 5)
        t._root.right.right = t._Node(7, 7)
        return t

    def test_insert(self) -> BST:
        t = BST()
        for i in [4, 2, 6, 1, 3, 5, 7]:
            t.insert(i, i)
        return t

    def test_search(self):
        x = 7
        t = self.test_insert()
        self.assertEqual(t.search(7), 7)

    def test_BFS(self):
        t1 = self.create_tree()
        t2 = self.test_insert()
        self.assertListEqual(t1.bfs(), t2.bfs())

    def test_empty_tree(self):
        t = BST()
        self.assertIsNone(t.search(1))

    def test_not_find(self):
        t = self.test_insert()
        self.assertIsNone(t.search(8))

    def test_delete_leaf(self):
        t = self.test_insert()
        t.delete(5)
        expected = [4, 2, 6, 1, 3, 7]
        self.assertListEqual(expected, t.bfs())

    def test_delete_node(self):
        t = self.test_insert()
        t.delete(9)
        expected = [4, 2, 6, 1, 3, 5, 7]
        self.assertListEqual(expected, t.bfs())
        t.delete(6)
        expected = [4, 2, 5, 1, 3, 7]
        self.assertListEqual(expected, t.bfs())
