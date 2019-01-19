import unittest
# todo: 读一下edit distance DP算法


def better_solution(s: str, t:str) -> bool:
    m: int = len(s)
    n: int = len(t)
    if m > n:   # 如果s更长则交换s，t
        return better_solution(t, s)
    if n - m > 1:  # 如果长度差距大于一则比为False
        return False
    i: int = 0  # i 来遍历m
    shift: int = n - m  # 偏移量：为0或者1
    while i < m and s[i] == t[i]:
        i += 1
    if i == m:  # 表示s[0:m]与t[0:m]一致，如偏移量为1则需要append
        return shift > 0
    if shift == 0:  # 如偏移量为0，则表示有一处不一致，跳过此处
        i += 1
    while i < m and s[i] == t[i + shift]:
        # 覆盖了两种情况：
        # 1. shift == 0时，16行，17行跳过了该字母
        # 2. shift == 1时， 18行的shift起效，表示让t跳过一个字母
        i += 1
    return i == m  # 检查能否到达末尾


def one_edit_distance(s: str, t: str) -> bool:
    if len(s) > len(t):
        s, t = t, s
    if len(t) - len(s) > 1:
        return False
    elif len(t) - len(s) == 1:
        # check append and insert
        one_difference = False
        i = 0
        j = 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                if not one_difference:
                    one_difference = True
                    j += 1
                else:  # second difference
                    return False
        return True
    else:  # len(t) - len(s) == 0
        # check modify
        one_difference = False
        for i in range(len(t)):
            if s[i] != t[i]:
                if not one_difference:
                    one_difference = True
                else:  # second difference
                    return False
        return True


class Test1(unittest.TestCase):
    def test_modify(self):
        self.assertTrue(one_edit_distance('abcde', 'abxde'))

    def test_insert(self):
        self.assertTrue(one_edit_distance('abcde', 'abcxde'))

    def test_append(self):
        self.assertTrue(one_edit_distance('abcde', 'abcdex'))

    def test_false(self):
        self.assertFalse(one_edit_distance('abcde', 'abcef'))
        self.assertFalse(one_edit_distance('abcde', 'abcxdf'))
        self.assertFalse(one_edit_distance('abcde', 'abcdefg'))


class Test2(unittest.TestCase):
    def test_modify(self):
        self.assertTrue(better_solution('abcde', 'abxde'))

    def test_insert(self):
        self.assertTrue(better_solution('abcde', 'abcxde'))

    def test_append(self):
        self.assertTrue(better_solution('abcde', 'abcdex'))

    def test_false(self):
        self.assertFalse(better_solution('abcde', 'abcef'))
        self.assertFalse(better_solution('abcde', 'abcxdf'))
        self.assertFalse(better_solution('abcde', 'abcdefg'))
