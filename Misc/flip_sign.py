"""
https://blog.csdn.net/ac_hell/article/details/51077320
翻转问题技巧详解
"""


def flip_sign(s: str, k) -> int:
    s = list(s)
    print(s)
    count = 0
    for i in range(len(s)-k+1):
        if s[i] == '-':
            count += 1
            for j in range(0, k):
                if s[i+j] == '+':
                    s[i+j] = '-'
                else:  # s[i+j]=='-
                    s[i+j] = '+'
            print(s)
    if s[-1] == '-':
        print('fail to find')
        return -1
    else:
        print('need', count, 'flip')
        return count


string = '-+-++--+'
flip_sign(string, 2)
