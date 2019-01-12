import unittest
"""要注意python的负数取余的结果与C语言不同，加一个符号判断
"""


class Solution:
    @staticmethod
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        flag = 1
        if x < 0:
            x = abs(x)
            flag = -1
        while x != 0:
            if abs(ret) > 2**31//10:
                return 0

            ret = ret * 10 + x % 10
            x //= 10
        return flag * ret


class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(123, s.reverse(321))
        self.assertEqual(1, s.reverse(100))
        self.assertEqual(-123, s.reverse(-321))
