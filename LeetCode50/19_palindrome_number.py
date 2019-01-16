import unittest
"""这道题的设计思路很简单，用while循环探测最高位的位数即可"""

class Solution:
    def isPalindrome(self, x:int) ->bool:
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div: int = 1
        while x / div > 10:
            div *= 10
        while x != 0:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x % div) // 10
            div /= 100
        return True


class Test(unittest.TestCase):
    def test_basic(self):
        s = Solution()
        self.assertTrue(s.isPalindrome(101))
        self.assertFalse(s.isPalindrome(123))
        self.assertTrue(s.isPalindrome(1))
        self.assertFalse(s.isPalindrome(-1))
