import unittest; from typing import List
"""结合实例纸面推导，算法的设计思路是保持一个仅包含两种字符的窗口"""
def find_length_of_substring(s: str) -> int:
    # 假设有两种字符：字符1 与 字符2
    i: int = 0  # i 用来存放子字符串的开头
    j: int = -1  # j用来存放与当前字符不同但为字符1或字符2的最远的位置， 如果s[k]为字符1 则s[j]为字符2
    max_len: int = 0
    for k in range(1, len(s)):  # k 用来存放当前位置
        if s[k] == s[k-1]:  # 如果与之前的字符一致则不断前移，但不改变j的位置
            continue
        if j >= 0 and s[j] != s[k]:  # 第9行与第11行不成立，表示遇到了新的第三种字符或者j=-1表示遇到第二种字符
            max_len = max(k-i, max_len)
            i = j + 1  # 重置子字符串开头
        j = k - 1  # 第9行判断不成立，因此s[k-1]与s[k]分别是字符1与字符2，
        # 本质上是把子字符串中仅包含单独一种字符的子子符串的开头记录下来，
        # 因此 第13行可以用j来设置新字符串的开头
    return max(len(s) - i, max_len)


def better_solution(s: str) -> int:
    """改进的算法允许子字符串有K个不同种类的字符"""
    count: List[int] = [0] * 256  # 遇到某个字符的次数
    i: int = 0  # i是子字符串的开头
    number_distinct = 0
    max_len = 0
    for j in range(0, len(s)):
        if count[ord(s[j])] == 0:  # 如果从未遇到，则distinct计数加一
            number_distinct += 1
        count[ord(s[j])] += 1  # 遇到某个字符的次数+1
        while number_distinct > 2:  # 这里可以选允许的不同字符种类个数，
            # 出现第三种字符时，将i不断前移（36行）且减去s[i]的字符count计数（33行），
            # 直至为零表示子字符串中无此字符（34行），distinct计数减1（35行）
            count[ord(s[i])] -= 1
            if count[ord(s[i])] == 0:
                number_distinct -= 1
            i += 1
        max_len = max(j - i + 1, max_len)  # 子字符串是从i到j的
    return max_len


class Test(unittest.TestCase):
    def test(self):
        string = 'abaac'
        self.assertEqual(4, find_length_of_substring(string))
        self.assertEqual(4, better_solution(string))


