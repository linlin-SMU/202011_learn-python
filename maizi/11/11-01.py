# 单例模式（为一种设计模式：前辈所总结的一些经验）：不管做了多少次实例化操作，只会创建一个对象

# __new__ 传入类，输出对象，__init__传入对象，初始化
class Person(object):

    # def __str__(self):
    #     return 'i love you with all hearts'

    __instance = None # 保存实例对象，为类属性，默认值为None，保证为单利模式
    __is_first = True # 用来判断是否为第一次执行，类属性
    def __new__(cls, *args, **kwargs): # *args 表示未知参数，**kwargs表示关键参数
        print('__new__被调用')
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
            # 将当前类传入父类，返回对象
        return cls.__instance
        # new方法：必须返回一个实例对象，如果对象时当前类，则接下来调用__init__
        # 通过调用父类的__new__来创建对象并返回

    def __init__(self, name, age, id):
        # init 的初始化对象为self，在调用的时候self已经被创建了
        if self.__is_first:
            self.name = name
            self.age = age
            self.id = id
            print('__init__被调用')

p1 = Person('vera', 18, id = 100)
p2 = Person('bob', 22, id = 30)
print(p1)
print(p2)

