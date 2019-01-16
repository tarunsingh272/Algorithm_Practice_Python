import unittest


class Solution:
    """Binary Search
    Time: O(nlogn)
    Space O(1)"""
    def _binary_search(self, array, t, start):  # use start to avoid duplicate search area
        """array: List, t: int, return int"""
        l = start
        r = len(array) - 1
        while l < r:
            m = (l+r)//2
            if array[m] == t:
                return m
            if array[m] < t:
                l = m + 1
            else:
                r = m - 1
        if l == r and array[l] == t:
            return l
        return False

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            bs_result = self._binary_search(numbers, target - numbers[i], i+1)
            if bs_result:
                return [i+1, bs_result+1]


class Solution2:
    """Two pointer
    Time: O(n)
    Space: O(1)"""
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i+1, j+1]
            elif sum < target:
                i += 1
            else:
                j -= 1



class Test(unittest.TestCase):
    def test(self):
        nums = [1,2,3,4,4,9,56,90]
        target = 8
        expected = [4,5]
        s = Solution2()
        self.assertListEqual(expected, s.twoSum(nums, target))
