import unittest


class Solution(object):
    """Use hashmap to store sum->pairs
    add:O(n)
    exist: O(1)
    find: O(1)
    Space: O(n^2)"""
    _hash_map = {}  # sum -> pair
    _list = []  # list of numbers

    def add(self, input):
        for i in range(len(self._list)):
            self._hash_map[self._list[i]+input] = (i, len(self._list))
        self._list.append(input)

    def exist(self, value):
        if value in self._hash_map:
            return True
        else:
            return False

    def find(self,value):
        if value in self._hash_map:
            return self._hash_map[value]


class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        s.add(1)
        s.add(3)
        s.add(5)
        self.assertTrue(s.exist(4))
        self.assertTupleEqual(s.find(4), (0, 1))
        self.assertFalse(s.exist(7))
