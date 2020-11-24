# Master 继承 object； School继承Master；Prentice继承School
# 为单继承

class Master(object):
    def __init__(self):
        self.kungfu = '古老的配方'

    def make_cake(self):
        print('按照%s的方法制作了一份煎饼果子' % self.kungfu)

class School(Master):
    def __init__(self):
        self.kungfu = '教学方法'

    def make_cake(self):
        print('按照%s制作了一份煎饼果子' % self.kungfu)
        super().__init__()  # 执行父类的构造函数
        super().make_cake()

class Prentice(School):
    def __init__(self):
        self.kungfu = '猫氏的配方'

    def make_cake(self):
        print('按照%s制作了一份煎饼果子' % self.kungfu)

    def make_all_cake(self):
        # 1.
        # School.__init__(self)
        # School.make_cake(self)
        #
        # Master.__init__(self)
        # Master.make_cake(self)
        #
        # self.__init__()
        # self.make_cake()

        # 2
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()
        self.make_cake()
        super().__init__()  # 执行父类的构造函数， 用于单继承， pythonic
        super().make_cake()

damao = Prentice()
damao.make_all_cake()

# 同时执行所有父类方法
# 子类继承了多个父类，如果父类类名修修改了，那么子类也要多次修改
# 子类继承了多个父类，需要重复多次调用，代码比较臃肿

# super()：执行父类的方法

# 使用super()可以逐一调用所有的父类方法，并且只执行一次
# 调用顺序遵循__mro__类属性
# Prentice.__mro__获取所有父类的序列
