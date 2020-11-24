# 老师傅精通煎饼果子制作
class Master(object):
    def __init__(self):
        self.kungfu = '古法煎饼果子配方'

    def make_cake(self):
        print('按照 %s 制作了一份煎饼果子。。' % self.kungfu)

    def dayandai(self):
        print('大眼袋')

# 1）
# 传承配方给徒弟--damao，继承--如果一个类里面的属性和方法可以复用，则可以用继承
# 父类--基类，子类--派生类
class Prentice(Master):   # prentice 可以继承master
    pass
laoli = Master()
damao = Prentice()

# 2）
class School(object):
    def __init__(haha):   # 如果是haha，在以后引用school，也是haha
        haha.kungfu = '现代方法'

    def make_cake(haha):
        print('按照 %s 制作了一份煎饼果子' % haha.kungfu)

    def dayandai(haha):
        print('小眼袋')

# 多继承可以继承多个父类，也继承了父类的属性和方法
# 父类有同名的属性和方法，则默认使用第一个; 如果出现不重名的属性和方法，就没有任何影响
# class Prentice(master, school):  # 优先使用master的属性方法
#     pass      # 融合古法的现代，创建了一种新方法

class Prentice(School, Master):
    pass
# 如果子类和父类同命，默认用子类的

laoli = Master()
damao = Prentice()   # 使用master 的父类
print(damao.kungfu)
damao.make_cake()
damao.dayandai()

# 3）小猫融合创建了一个全新的配方，猫氏煎饼果子配方
class Prentice(School, Master):
    def __init__(self):
        self.kungfu = '猫氏煎饼果子配方'

    def make_cake(self):
        print(self)
        self.__init__()   # 调用
        print('按照猫氏煎饼果子配方' )

    def make_old_cake(self):
        print(self)
        Master.__init__(self)   # 魔法函数，就是在调用的时候会自动执行，初始化变量
        Master.make_cake(self)   # 在类的外面，self自动传递；但在类的里面，无self，得设置self
        # 否则，这儿的self还是为prentice的self

    def make_new_cake(self):
        print(self)   # 输出self的地址
        School.__init__(haha)
        School.make_cake(haha)

# 如果子类和父类的方法名为一致，则默认使用子类，子类重写父类的方法名
xiaomao = Prentice()   # prentice则成为了一个子类，其中，被魔方函数有一个单独的变量，同时继承了父类的变量
make_cake = xiaomao.make_cake()  # 在类的外面，self自动传递；但在类的里面，无self
yandai = xiaomao.dayandai()

# 子类调用父类的同名方法，
damao = Prentice()
print(damao.kungfu)
damao.make_old_cake()
damao.make_new_cake()