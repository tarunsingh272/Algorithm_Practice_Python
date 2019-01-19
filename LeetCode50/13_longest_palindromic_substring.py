import unittest
from typing import List
"""简单解法和DP解法都值得学习"""

class DPSolution:
    def longestPalindrome(self, s):
        """
        Dynamic Programming Solution
        :type s: str
        :rtype: str
        """
        p: List[List[bool]] = [[False]*len(s) for _ in range(len(s))]
        j: int = 0
        max_len:int = 0
        best_i = 0
        best_j = 0
        while j < len(s):
            i = 0
            while i <= j:
                if i == j:
                    p[i][j] = True
                elif i + 1 == j and s[i] == s[j]:
                    p[i][j] = True
                    if max_len < 2:
                        best_i, best_j = i, j
                elif p[i+1][j-1] is True and s[i] == s[j]:
                    p[i][j] = True
                    if max_len < j-i+1:
                        max_len = j-i+1
                        best_i, best_j = i, j
                        print('x',best_i, best_j)
                i += 1
            j += 1
        # for line in p:
        #     print(line)
        return s[best_i:best_j+1]

class SimplerSolution():
    def longestPalindrome(self, s: str) -> str:
        start: int = 0
        end: int = 0
        for i in range(len(s)):
            len1 = self.expand_around_center(s, i, i)  # substring center at i， len1为奇数：2n+1
            len2 = self.expand_around_center(s, i, i+1)  # substring center between i and i+1, len2为偶数：2n
            larger_len = max(len1, len2)
            if end - start < larger_len:  # 这里是整合了前面两种中间点的情况
                # 为len1=2n+1时, start = i-(2n+1-1)//2 = i - n, end = i + (2n+1)//2 = i + 2n,
                # 例如： 0 （1 [2] 3） 4
                # 为len2=2n时，start = i-(2n-1)//2 = i - (n-1), end = i + 2n // 2 = i+n,
                # 例如： （0 [1] 2 3) 4, 注意i左右并不对称
                start = i - (larger_len - 1) // 2
                end = i + larger_len // 2
        return s[start: end+1]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # 这里用右-左-1是因为最终对称子字符串不包含左右


class Test(unittest.TestCase):
    def test_DP(self):
        s = DPSolution()
        self.assertSequenceEqual('a', s.longestPalindrome('abcda'))
    def test_simpler(self):
        s = SimplerSolution()
        self.assertSequenceEqual('a', s.longestPalindrome('abcda'))
