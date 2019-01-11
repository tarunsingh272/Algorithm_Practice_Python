import unittest
"""如何用最简单的方式来避免越界，并考虑到特殊情况"""

class Solution(object):
    def myAtoi(self, string):
        """
        :type string: str
        :rtype: int
        """
        i = 0
        n = len(string)
        while i < n and string[i] == ' ':  # 搞定字符串前的空格
            i += 1
        sign = 1
        if i < n and string[i] == '+':  # i<n保证不会越界
            i += 1
        elif i < n and string[i] == '-':  # elif 保证 +-2 会被当做非数字
            sign = -1
            i += 1
        num = 0
        upper_limit = 2**31//10
        while i < n and string[i].isnumeric():  # until the last numerical character
            digit = int(string[i])
            if num > upper_limit or (num == upper_limit and digit >= 8):
                return 2**31-1 if sign == 1 else -2**31
            num = num * 10 + digit
            i += 1
        return sign * num





class Test(unittest.TestCase):
    def f(self):
        s = Solution()
        return s.myAtoi

    def test_basic(self):
        f = self.f()
        self.assertEqual(f('42'), 42)
        self.assertEqual(-42, f('   -42'))
        self.assertEqual(f('4193 abcd'), 4193)
        self.assertEqual(f('abc 123'), 0)

    def test_adcanced(self):
        f = self.f()
        self.assertEqual(-2147483648, f('-91283472332'))

    def test_special_case(self):
        f = self.f()
        self.assertEqual(0, f('+-2'))
