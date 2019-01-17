from typing import List
"""
两个数组表示瓜和盒子，限制条件：
1. 瓜小于盒子可以装下
2. 可以从任意位置开始装瓜，但开始后必须连续装瓜
3. 可以跳盒子，但是顺序不能变
"""


def melon_count(boxes: List[int], melons: List[int]) -> int:
    max_count = 0
    m = 0
    while m < len(melons):  # m是开始装瓜的位置，遍历一遍所有位置
        b = 0
        current = []
        count = 0
        while b < len(boxes) and m < len(melons):  # 遍历所有盒子
            if melons[m] <= boxes[b]:
                current.append(melons[m])
                m += 1
                count += 1
            b += 1
        if count > max_count:
            max_count = count
            best = [i for i in current]
            print(best)
        m += 1
    return max_count


box = [2, 3, 2, 2]
melon = [2, 4, 3, 2]
print(melon_count(box, melon))
