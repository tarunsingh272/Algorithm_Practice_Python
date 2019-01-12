import unittest
"""标准答案 第二个的思路和我的思路是一样的，
但是它将相同的语句放于if块外，并额外考虑到i可能减小的问题
并不需要length=0/1时的特殊判断，值得学习。"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if len(s) <= 1:
        #     return len(s)

        i = 0
        j = 0
        n = len(s)
        index_map = dict()
        max_len = 0
        while j < n:
            if s[j] in index_map and index_map[s[j]] >= i:
                # j>i 保证了反复重复时会把i减小的问题， 例如输入是tmmzuxt
                i = index_map[s[j]] + 1
            index_map[s[j]] = j
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len




class Test(unittest.TestCase):
    def test_basic(self):
        s = Solution()
        self.assertEqual(3, s.lengthOfLongestSubstring('abcabcbb'))
        self.assertEqual(1, s.lengthOfLongestSubstring('bbbbb'))
        self.assertEqual(3, s.lengthOfLongestSubstring('pwwkew'))
        self.assertEqual(2, s.lengthOfLongestSubstring('ab'))

    def test_empty(self):
        s = Solution()
        self.assertEqual(0, s.lengthOfLongestSubstring(''))
        self.assertEqual(1, s.lengthOfLongestSubstring('a'))

    def test_lc(self):
        s = Solution()
        self.assertEqual(5, s.lengthOfLongestSubstring('tmmzuxt'))
