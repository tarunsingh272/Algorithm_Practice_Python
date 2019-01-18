import unittest
from typing import List, Tuple
"""给开头和结尾加上两个虚拟的变量-1， 100能让代码简洁不少"""


def missing_ranges(inp: List[int], ran: Tuple[int, int] = (0, 99)) -> List[str]:
    result: List[str] = []
    prev: int = ran[0] - 1
    inp.append(ran[1] + 1)
    for i in range(len(inp)):
        if inp[i] - prev > 2:
            result.append('%d->%d' % (prev+1, inp[i]-1))
        elif inp[i] - prev == 2:
            result.append('%d' % (inp[i] - 1))
        prev = inp[i]
    return result


class Test(unittest.TestCase):
    def test(self):
        self.assertListEqual(['2', '4->49', '51->74', '76->99'], missing_ranges([0, 1, 3, 50, 75]))
        self.assertListEqual(['0->99'], missing_ranges([]))
        self.assertListEqual([], missing_ranges(list(range(0, 100))))
