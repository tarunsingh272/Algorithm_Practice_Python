import unittest


class OfficalSolution:
    """标准答案用更加简明的代码覆盖了特殊情况，值得学习"""
    def reverseWords(self, s):
        ss = []
        j = len(s)  # j is the last index of a blank
        i = len(s) - 1
        while i >= 0:
            if s[i] == ' ':
                """用于检测词末的空格，支持多个空格"""
                j = i
            elif i == 0 or s[i-1] == ' ':
                """用于检测词开始的位置，或者是句子的开头"""
                ss.append(s[i: j])
            i -= 1
        return ' '.join(ss)


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = []
        s = s.strip()  # take care of the space in the begin and end
        last = len(s)  # last index of a blank
        if len(s) <= 1:
            return s
        # for i in range(len(s)-1, -2, -1):
        i = len(s) - 1
        while i > -2:  # use i > -2 for the beginning of the string
            if s[i] == ' ' or i == -1:
                ss.append(s[i+1:last])
                while s[i-1] == " ":  # eat all the spaces
                    i -= 1
                last = i
            i -= 1
        return " ".join(ss)


class Test(unittest.TestCase):
    def test1(self):
        s = OfficalSolution()
        self.assertSequenceEqual(s.reverseWords('the sky is blue'), 'blue is sky the')

    def test_special(self):
        s = OfficalSolution()
        self.assertSequenceEqual(s.reverseWords("  a  b"), "b a")
        self.assertSequenceEqual(s.reverseWords(""),"")
        self.assertSequenceEqual(s.reverseWords("a"),"a")

