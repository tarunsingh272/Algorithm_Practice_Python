def countDuplicates(array):
    """count the number of duplicate elements in an array"""
    count = 0
    seen = set()
    seen2 = set()
    for i in array:
        if i in seen:
            if i not in seen2:
                seen2.add(i)
                count += 1
        else:
            seen.add(i)
    return count

a = [1, 1, 2, 2, 2, 3, 4, 3, 9]
print(countDuplicates(a))