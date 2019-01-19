"""
Breadth First Search Implementation
By: Xiaochi (George) Li
"""
from collections import deque
from Data_Structure.graph import AdjListGraph as Graph
from typing import List
import unittest


class BreadthFirstSearch(object):
    """
    Breadth First Search
    https://www2.seas.gwu.edu/~ayoussef/cs6212/graphsearch.html#BFS
    """

    _trace: List[int] = []

    def bfs(self, G: Graph, s: int):
        visited: List[bool] = [False] * G.V()
        queue = deque()  # use deque as a queue (right in left out)
        visited[s] = True
        queue.append(s)
        self._trace.append(s)
        while len(queue) > 0:
            current = queue.popleft()
            for neighbour in G.adj(current):
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)
                    self._trace.append(neighbour)

    def trace(self, G: Graph, s: int) -> List[int]:
        self.bfs(G, s)
        return self._trace


class TestBFS(unittest.TestCase):
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

    def test_bfs(self):
        G = self.create_graph()
        BFS = BreadthFirstSearch()
        self.assertListEqual([0, 2, 1, 5, 3, 4], BFS.trace(G, 0))
