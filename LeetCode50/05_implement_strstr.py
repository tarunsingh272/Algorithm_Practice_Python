"""考虑边界条件与代码的简洁性"""

import unittest


class Faster_Solution:
    """标准答案, 原答案中的Java写法允许无上限的for， 但是改成python的for后要把i和j的上限写的高于字符串长度
    因为后面几个判断是在越界时触发的"""
    def strStr(self, haystack, needle):
        for i in range(len(haystack) + 1):  # i is the start pointer of the haystack
            for j in range(len(needle) + 1):  # j is the pointer in the needle
                if j >= len(needle):  # already found
                    return i
                if i + j >= len(haystack):  # reach the limit of haystack
                    return -1
                if needle[j] != haystack[i+j]:  # letter not match
                    break


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)):
            if len(needle) > len(haystack[i:]):  # haystack not long enough
                return -1
            p = 0
            q = i
            while p < len(needle) and needle[p] == haystack[q]:
                p += 1
                q += 1
            if p == len(needle):
                return i
        return -1


class Test(unittest.TestCase):
    s = Faster_Solution()

    def test1(self):
        self.assertEqual(self.s.strStr('hello', 'll'), 2)
        self.assertEqual(self.s.strStr('aaaaa', 'bba'), -1)

    def test_special_case(self):
        self.assertEqual(self.s.strStr("", "a"), -1)
