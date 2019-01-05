class Student(object):
    """
    访问限制： __变量名
    """
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


class Animal(object): #父类 base class
    name = 'animal'
    """
    实例属性属于各个实例所有，互不干扰；
    类属性属于类所有，所有实例共享一个属性；
    不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
    """
    def walk(self):
        print('Animal is walking')
    def run(self):
        print('Animal is running...')

class Dog(Animal):  #子类subclass

    def run(self):  #多态
        print('Dog is running')
    def eat(self):
        print('Dog is eating')

"""
对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，
就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，
由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，
而当我们新增一种Animal的子类时，
只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
对扩展开放：允许新增Animal子类；
对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
"""


"""
对于静态语言（例如Java）来说，如果需要传入Animal类型，
则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。
我们只需要保证传入的对象有一个run()方法就可以了：
"""
def run_twice(a):
    a.run()
    a.run()

if __name__ =='__main__':
    student1 = Student('George', 100)
    student1.print_score()
    run_twice(Dog())
    d = Dog()
    print(isinstance(d, Dog))
    print('ABC'.__len__())
