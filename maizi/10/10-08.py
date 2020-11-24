# 类属性，类方法和实例属性
class Person(object):

    # 类属性
    cls_number = 100 # 类属性归本类所有对象共享，只在内存中保存一份
    # 也可以设定私有类属性 __cls_number = 100
    # 类方法：@classmethod 装饰器，用来装饰一个函数，让这个函数有特殊的作用
    # 类方法一般用来处理类属性，有个唯一参数cls，表示当前类
    # 类方法可以被对象和类访问
    @classmethod
    def get_cls_number(cls):
        return cls.__cls_number   # 通过访问类属性并返回

    # self：为了访问实例属性和实例方法
    # cls：表示类，为了类属性和类方法


    # 实例方法
    def print_info(self):
        # 通过对象访问类，在通过类，访问类属性
        print('类属性 cls_number: %d' % self.__class__.__cls__number)

        # 通过对象直接访问类属性
        print('类属性 cls_number: %d' % self.__cls_number)

    # 静态函数：装饰器 @staticmethod;
    # 静态函数就是类里面的普通函数，不需要传递self和cls，不需要访问实例属性和实例方法或者类属性和类方法
    def haha(a, b):
        return a+b

    def __init__(self, name):
        self.name = name # 为实例属性