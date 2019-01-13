import unittest
"""注意用list.insert在头部插入数据会很慢O（N），所以最后用了末尾加零，头上改1的骚操作"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        while i >= 0:
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
            i -= 1
        digits.append(0)
        digits[0] = 1
        return digits


class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        ss = [1, 2, 3]
        ss = s.plusOne(ss)
        self.assertListEqual([1, 2, 4], ss)
        ss = [9, 9, 9]
        ss = s.plusOne(ss)
        self.assertListEqual([1, 0, 0, 0], ss)
