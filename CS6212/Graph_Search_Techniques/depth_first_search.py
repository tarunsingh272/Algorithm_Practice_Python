from Data_Structure.graph import AdjListGraph as Graph
from collections import deque
from typing import List
import unittest


class RecursiveDepthFirstSearch(object):
    """
    Depth First Search implemented with recursion
    Algorithms 4th P531
    """
    _marked: List[bool] = None
    _count: int = 0
    _trace: List[int] = []

    def dfs(self, G: Graph, s: int):
        self._marked = [False] * G.V()
        self._dfs(G, s)

    def _dfs(self, G: Graph, v: int):
        self._trace.append(v)
        self._marked[v] = True
        self._count += 1
        for w in G.adj(v):
            if not self._marked[w]:
                self._dfs(G, w)

    def marked(self, w: int) -> bool:
        return self._marked[w]

    def count(self) -> int:
        return self._count

    def trace(self, G: Graph, s: int) -> List[int]:
        """get the visit order of dfs for debug"""
        self.dfs(G, s)
        return self._trace


class DepthFirstSearch(object):
    """
    Depth First Search without recursion
    https://www2.seas.gwu.edu/~ayoussef/cs6212/graphsearch.html#DFS
    """

    _trace: List[int] = []

    def dfs(self, G: Graph, s: int):
        visited: List = [False]* G.V()
        stack: deque = deque()  # use deque as a stack
        stack.append(s)
        visited[s] = True
        self._trace.append(s)
        while len(stack) > 0:
            current = stack[-1]  # update with the deepest place
            exist_unvisited_neighbour = False
            for neighbour in G.adj(current):
                if not visited[neighbour]:
                    # if current has one unvisited neighbour then visit it immediately,
                    # otherwise it becomes BFS
                    exist_unvisited_neighbour = True
                    visited[neighbour] = True
                    stack.append(neighbour)  # gets deeper
                    self._trace.append(neighbour)
                    break  # only visit one unvisited neighbour and goto it
            if not exist_unvisited_neighbour:
                stack.pop()

    def trace(self, G:Graph, s: int) -> List[int]:
        self.dfs(G, s)
        return self._trace




class TestDFS(unittest.TestCase):
    def create_graph(self) -> Graph:
        """tinyGG on Alg4 P532"""
        inputs = [
            [6, 8],
            [0, 5],
            [2, 4],
            [2, 3],
            [1, 2],
            [0, 1],
            [3, 4],
            [3, 5],
            [0, 2]
        ]
        G = Graph(inputs)
        return G

    def test_recurisive_dfs(self):
        G = self.create_graph()
        rdfs = RecursiveDepthFirstSearch()
        self.assertListEqual([0, 2, 1, 3, 5, 4], rdfs.trace(G, 0))

    def test_non_recursive_dfs(self):
        G = self.create_graph()
        dfs = DepthFirstSearch()
        self.assertListEqual([0, 2, 1, 3, 5, 4], dfs.trace(G, 0))


