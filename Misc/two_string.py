def commonSubstring(a, b):
    """find whether two string has common substring"""
    for i in range(len(a)):
        aa = set(a[i])
        bb = set(b[i])
        if len(aa.intersection(bb)) >0:
            print('YES')
        else:
            print('NO')


a = ['hello', 'hi']
b = ['world', 'bye']

commonSubstring(a,b)