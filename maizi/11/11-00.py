'''面向对象的3大特性: 封装，继承和多态
1、封装
2、继承
1）单继承
2）多继承
3）子类重写，则子类调用父类的方法(在定义中)
a.父类名.__init__(self)
父类名.method(self)
b. super()--只用于单继承
super().__init__()

class A(object):
    def __init__(self):
        self.num = 10

class B(A):
    def __init__(self):
        self.num = 100
        super().__init__()
所以在 obj = B()
print(obj.num) 值为10'''

'''析构函数 __del__:在对象删除/程序结束是会被调用--删除对该对象的引用，删除一个引用而已，
 当A()对应的引用为0 时，A被删除，
 a = 0 
 del a   0不会被删除
 
 a = 100
del a  100也会被删除
class A(object):
    def __init__(self, name, age)
        self.f = open('xx.txt', 'w')
        self.name = name
        self.age = age
        
    def write_file(self)
        self.f.write(name)
        self.f.write(age)
    
    def __del__(self)  删除了对象的引用， ：
        self.f.close()
    
vera = A（）
del（vera） 删除了vera对A 的引用'''

'''封装：
1、把属性和方法封装在一个类里面，可以隐藏实现细节，外部只需要和类的对象交互就可以了
2、添加访问权限控制
私有权限：__name 只能在类的内部使用，类的外部对象不能修改和访问，则可以进行以下操作
1）class A（object）:
    def __init__(self):
        self.__num = 10
        self. _A__num = 100 # 对象名._类名__name 进行修改

2）通过公有的实例方法：get_num()和set_num()来访问或者修改私有属性
def get_num(self):
    return self.__num
    
def set_num(self, n)
    return self.__num = n
    保护：_name 对象不建议修改和访问'''

'''多态
弱化类型：重点在于对象是否由指定的属性和方法，如果有认定就合格

1）静态语言：Java，C++在运行前就定义类型的
2）动态语言：在运行时就定义类型的python

# python是强类型-- 对类型有严格判断，str和字符串是不同的'''

'''类属性、类方法和静态方法
类属性：在类的内部、方法和外部的，所有对象共享，只占用一份内容，类属性一般设为私有权限
类方法：装饰器@classmethod，一般用来处理类属性，有一个唯一参数，cls表示当前类，可以被所有对象调用
class A(object):
    __name = 'Python'

    @classmethod\
    def make_cake(cls)\
        print(cls.__name)\
        print(A.__name)\

    def obj__func(self):\
        print(self.__name)\
        print(self.__class__.__name)
静态方法：装饰器 @staticmethod，就是类里面的普通函数，不需要传递self或cls，也可以被所有对象调用
    @staticmethod
    def func()
        print('hello world')'''