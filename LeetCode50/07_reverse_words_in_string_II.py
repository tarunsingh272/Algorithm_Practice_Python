import unittest
"""string is not editable in Python
Python不支持直接对字符串进行改变，这个设定太SB了"""


def reverse(string, begin=0, end=None):
    """因为Python特别SB的不允许直接改字符串的特性，
    这个函数的设计比标准答案复杂很多，且多了更多创建列表与连接字符串的操作"""
    if end is None:
        end = len(string) - 1
    left = string[0:begin]
    right = string[end+1:len(string)]
    temp = ['0']*(end-begin+1)
    i = 0
    while i <= (end-begin+1) // 2:
        temp[i], temp[end-begin - i] = string[end - i], string[begin+i]
        i += 1

    return left + ''.join(temp) + right


def reverse_words(string):
    if len(string) <= 1:
        return string
    string = reverse(string)
    i = 0
    for j in range(len(string)+1):
        if j == len(string) or string[j] == ' ':
            string = reverse(string, i, j-1)
            i = j + 1
    return string


class Test(unittest.TestCase):
    def test_reverse(self):
        s = 'abcde'
        s = reverse(s)
        self.assertSequenceEqual(s, 'edcba')

    def test_reverse_2(self):
        s = 'xabcdezz'
        s = reverse(s, 1, 5)
        self.assertSequenceEqual(s, 'xedcbazz')

    def test_reverse_words(self):
        self.assertSequenceEqual(reverse_words('the sky is blue'), 'blue is sky the')

    def test_empty(self):
        self.assertEqual('', reverse_words(''))
