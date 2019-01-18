import unittest
from typing import List

class Solution:
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
        for line in p:
            print(line)
        return s[best_i:best_j+1]



class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertSequenceEqual('a', s.longestPalindrome('abcda'))
