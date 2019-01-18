"""
Graph implementations
By: Xiaochi (George) Li
"""
from typing import List, Dict
from collections import deque
import unittest


class AdjListGraph(object):
    """
    Adjacency List Representation
    Based on deque instead of Bag (Linked List)
    Algorithms 4th P526
    """

    _V: int = None  # number of vertices
    _E: int = None  # number of edges
    _adj: List[deque] = None  # the adjacency list

    def __init__(self, inputs):
        """initialize the graph from input"""
        V = inputs[0][0]
        E = inputs[0][1]
        if len(inputs) != E+1:
            raise ValueError('Error in the input, the size does not match number of Edges')
        self._V = V
        self._adj = [None]*V
        for i in range(V):
            self._adj[i]: deque = deque()
        for i in range(1, len(inputs)):
            v = inputs[i][0]
            w = inputs[i][1]
            self._adj[v].appendleft(w)
            self._adj[w].appendleft(v)

    def adj(self, v: int) -> deque:
        """get the adjacency list of a vertex"""
        return self._adj[v]

    def to_list(self) -> Dict:
        """return the adjacency list for debug (Alg4 P523)"""
        adj_list: Dict = {}
        for v in range(self._V):
            adj_list[v]:List[int] = []
            for w in self.adj(v):
                adj_list[v].append(w)
        return adj_list


class Tests(unittest.TestCase):

    def test_create_graph(self):
        """the sample from Alg4 P525"""
        inputs = [
            [13, 13],
            [0, 5],
            [4, 3],
            [0, 1],
            [9, 12],
            [6, 4],
            [5, 4],
            [0, 2],
            [11, 12],
            [9, 10],
            [0, 6],
            [7, 8],
            [9, 11],
            [5, 3]
        ]
        G = AdjListGraph(inputs)
        self.assertDictEqual(
            {0: [6, 2, 1, 5],
             1: [0],
             2: [0],
             3: [5, 4],
             4: [5, 6, 3],
             5: [3, 4, 0],
             6: [0, 4],
             7: [8],
             8: [7],
             9: [11, 10, 12],
             10: [9],
             11: [9, 12],
             12: [11, 9]},
            G.to_list()
        )
