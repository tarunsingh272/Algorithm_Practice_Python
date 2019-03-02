from typing import List
from unittest import TestCase
"""关键是用一个参考变量i来记录走了几步，然后记录目前的位置，记得在while循环结束后将当前坐标减一，避免越界"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        height = len(matrix)
        if height == 0:
            return []
        width = len(matrix[0])
        if width == 0:
            return []
        h = w = 0  # initialize current place

        while height > 0 and width > 0:
            # move right
            i = 0
            while height > 0 and width > 0 and i < width:
                result.append(matrix[h][w])
                w += 1
                i += 1
            w -= 1
            h += 1
            height -= 1
            # move down
            i = 0
            while height > 0 and width > 0 and i < height:
                result.append(matrix[h][w])
                h += 1
                i += 1
            h -= 1
            w -= 1
            width -= 1
            # move left
            i = 0
            while height > 0 and width > 0 and i < width:
                result.append(matrix[h][w])
                i += 1
                w -= 1
            w += 1
            h -= 1
            height -= 1
            # move up
            i = 0
            while height > 0 and width > 0 and i < height:
                result.append(matrix[h][w])
                i += 1
                h -= 1
            h += 1
            w += 1
            width -= 1
        return result


class Test(TestCase):
    def test_1(self):
        s = Solution()
        in_ = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertListEqual([1,2,3,6,9,8,7,4,5], s.spiralOrder(in_))

    def test_2(self):
        s = Solution()
        in_ = [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12]
        ]
        self.assertListEqual([1,2,3,4,8,12,11,10,9,5,6,7], s.spiralOrder(in_))
