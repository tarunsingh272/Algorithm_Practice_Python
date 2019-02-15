from typing import List
from unittest import TestCase


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pass


class HashMap(Solution):
    def singleNumber(self, nums: List[int]):
        map_ = dict()
        for i in nums:
            if i not in map_:
                map_[i] = 1
            else:
                map_[i] += 1
        for i in nums:
            if map_[i] == 1:
                return i


class Set(Solution):
    def singleNumber(self, nums: List[int]):
        set_ = set()
        for i in nums:
            if i not in set_:
                set_.add(i)
            else:
                set_.remove(i)
        return set_.__iter__().__next__()


class XOR(Solution):
    def singleNumber(self, nums: List[int]):
        num = 0
        for x in nums:
            num ^= x
        return num

class Test(TestCase):
    def test_1(self):
        for s in [HashMap(), Set(), XOR()]:
            self.assertEqual(4, s.singleNumber([4, 1, 2, 1, 2]))
