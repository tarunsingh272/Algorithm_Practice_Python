import unittest


class Solution:
    def twoSum1(self, nums, target):
        """
        Brute force Solution: Time: O(n^2), Space:O(1)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            e = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == e:
                    return [i, j]

    def twoSum2(self, nums, target):
        """
        Hash table Solution : Time:O(n), Space:O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}  # map:value -> index
        for i in range(len(nums)):
            if (target - nums[i]) in hash_map:   # in key
                return [hash_map[target - nums[i]], i]
            else:
                hash_map[nums[i]] = i


class Test(unittest.TestCase):
    def test(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        s = Solution()
        self.assertListEqual(expected, s.twoSum2(nums, target))
