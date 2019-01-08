import unittest


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
        while i > -2:
            if s[i] == ' ' or i == -1:
                ss.append(s[i+1:last])
                while s[i-1] == " ":  # eat all the spaces
                    i -= 1
                last = i
            i -= 1
        return " ".join(ss)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertSequenceEqual(s.reverseWords('the sky is blue'), 'blue is sky the')

    def test_special(self):
        s = Solution()
        self.assertSequenceEqual(s.reverseWords("  a  b"), "b a")

