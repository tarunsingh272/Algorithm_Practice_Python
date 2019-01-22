import heapq
import unittest

# some usage of python's built in heap
# 1. heappush
# 2. heappop
# 3. heappushpop = push then pop
# 4, heapify(x)
# 5.  heapreplace = pop then push
heapq._heappop_max()


class TestMinHeap(unittest.TestCase):
    def test_insert(self):
        heap = []
        for i in range(1, 12):
            heapq.heappush(heap, i)
        self.assertListEqual(heap, list(range(1, 12)))
        heapq.heappush(heap, 0)
        self.assertListEqual(heap, [0, 2, 1, 4, 5, 3, 7, 8, 9, 10, 11, 6])

    def test_delete(self):
        heap = []
        for i in range(1, 7):
            heapq.heappush(heap, i)
        self.assertEqual(heapq.heappop(heap), 1)
        self.assertListEqual(heap, [2, 4, 3, 6, 5])
