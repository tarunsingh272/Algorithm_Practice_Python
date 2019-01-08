def array_swap(array):
    copied = [array[i] for i in range(len(array))]
    for i in range(len(copied)//2):
        copied[i], copied[len(copied)-1-i] = copied[len(copied)-1-i], copied[i]
    array = copied


def number_change(a):
    a += 1


"""python 传值始终传入的是对对象的引用（指针），对于可变对象（类似于list），函数直接修改原来的对象的内容，
起到Procedure的作用"""
x = [1, 2, 3, 4, 5]
array_swap(x)
print(x)

"""对于不可变对象，对传入变量的修改会导致函数内部新建一个新的对象，不会影响外部"""
b = 1
number_change(b)
print(b)
