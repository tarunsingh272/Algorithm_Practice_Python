from unittest import TestCase
"""注意各种边界条件和防止越界"""


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i: int = 0
        n: int = len(s)
        is_number: bool = False
        while i < n and s[i] == ' ':  # eat all the space in front of the string
            i += 1
        if i < n and (s[i] == '+' or s[i] == '-'):  # the sign before the number
            i += 1
        while i < n and s[i].isnumeric():
            is_number = True
            i += 1
        if i < n and s[i] == '.':
            i += 1
        while i < n and s[i].isnumeric():
            is_number = True
            i += 1
        if not is_number:
            return False
        if i < n and s[i] == 'e':
            is_number = False
            i += 1
            if i < n and (s[i] == '+' or s[i] == '-'):  # these happen only after 'e'
                i += 1
            while i < n and s[i].isnumeric():
                is_number = True
                i += 1
        while i < n and s[i] == ' ':
            i += 1
        if i == n and is_number:
            return True
        else:
            return False


class Test(TestCase):
    def test_basic(self):
        s = Solution()
        self.assertTrue(s.isNumber('100'))
        self.assertTrue(s.isNumber('  +100'))
        self.assertTrue(s.isNumber('  -100   '))

    def test_decimal(self):
        s = Solution()
        self.assertTrue(s.isNumber('.1'))
        self.assertTrue(s.isNumber('  12.34'))

    def test_scientific(self):
        s = Solution()
        self.assertTrue(s.isNumber('  12e34  '))
        self.assertTrue(s.isNumber('12.34e56'))
        self.assertFalse(s.isNumber('0e'))
        self.assertFalse(s.isNumber('e9'))

    def test_special(self):
        s = Solution()
        self.assertFalse(s.isNumber('6+1'))
        self.assertFalse(s.isNumber(''))
        self.assertFalse(s.isNumber('  '))
