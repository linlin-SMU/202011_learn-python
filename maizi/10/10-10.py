class Person(object):
# 3、类属性
    cls1_number = 50
    __cls_number = 100 # 类属性--类属性归本类所有对象共享，仅在内从中保存一份
    # 私有类属性，__cls_number

# 4、类方法
    @classmethod
    def get__cls__number(cls):
        return cls.__cls__number
    # 类方法；@classmethod 装饰器，用来修饰一个函数，让这个函数有特殊作用
    # 类方法有唯一参数，cls来表示当前类（self：为了访问实例属性，cls为了访问类属性）
    # 在外面定义时，不需要传参
    # 类方法一般可以用来处理类属性


# 5、实例方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 类方法可以被对象和类访问
    def print_info(self):
        print('类属性 cls_number: %d' % self.__class__.__cls_number) # 通过对象访问类，通过类访问类属性
        print('类属性 cls_number：%d' % self.__cls_number)# 通过对象直接访问类属性


    def __del__(self):
        print('对象%s已被删除' % self.name)

# 6、静态函数：装饰器 @staticmethod
# 静态函数为类里面的普通函数，不需要传递实例属性、实例方法和类属性、类方法
    @staticmethod
    def add_num(a,b):
        return a + b

p = Person('Python', 27)
p.print_info()
print(p.cls1_number)

# 装饰器就是让这个函数具有特点的作用，成为静态函数、成为类方法等