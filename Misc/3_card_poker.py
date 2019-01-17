from collections import Counter

def p1_win_count(hands):
    """
    :type hands: List[List[int]]
    :rtype: int
    """
    p1_win = 0

    for hand in hands:
        print(hand)
        p1 = hand[0:3]
        p1_count = len(set(p1))
        p2 = hand[3:6]
        p2_count = len(set(p2))
        if p1_count < p2_count:
            p1_win += 1
            print('p1 win')
        elif p1_count > p2_count:
            pass
        else:  # same type
            if p1_count == 1:  # 3 of kind
                if p1[0] > p2[0]:
                    p1_win += 1
                    print('p1 win')
            elif p1_count == 2:  # one pair
                p1_counter = Counter(p1).most_common(2)
                p2_counter = Counter(p2).most_common(2)
                if p1_counter[0][0] > p2_counter[0][0]:
                    p1_win += 1
                    print('p1 win')
                elif p1_counter[0][0] == p2_counter[0][0]:  # same pair
                    if p1_counter[1][0] > p2_counter[1][0]:
                        p1_win += 1
                        print('p1 win')
            else:  # high card
                p1_sorted = sorted(p1, reverse=True)
                p2_sorted = sorted(p2, reverse=True)
                if p1_sorted[0] > p2_sorted[0]:  # compare first card
                    p1_win += 1
                    print('p1 win')
                elif p1_sorted[0] == p2_sorted[0]:
                    if p1_sorted[1] > p2_sorted[1]:  # compare second card
                        p1_win += 1
                        print('p1 win')
                    elif p1_sorted[1] == p2_sorted[1]:
                        if p1_sorted[2] > p2_sorted[2]:
                            p1_win += 1
                            print('p1 win')




    return p1_win


hands = [
    [7, 4, 2, 6, 5, 3],
    [8, 8, 2, 7, 4, 2],
    [7, 5, 2, 7, 4, 2],
    [8, 8, 4, 8, 8, 2],
    [8, 8, 8, 5, 5, 5]
]
p1_win_count(hands)