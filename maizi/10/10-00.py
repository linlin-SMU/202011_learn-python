# 老师傅精通煎饼果子制作
class Master(object):
    def __init__(self):
        self.kungfu = '古法煎饼果子配方'

    def make_cake(self):
        print('按照 %s 制作了一份煎饼果子。。' % self.kungfu)

    def dayandai(self):
        print('dayandai')


# 传承配方给徒弟, 父类--基类，子类--派生类
class Prentice(Master):
    pass

class School(object):
    def __init__(self):
        self.kungfu = '现代方法'

    def make_cake(self):
        print('按照 %s 制作了一份煎饼果子' % self.kungfu)

    def dayandai(self):
        print('小眼袋')

# 多继承可以继承多个父类，也继承了父类的属性和方法
# 父类有同名的属性和方法，则默认使用第一个
class Prentice(master, school):  # 优先使用master的属性方法
    pass

# 融合古法的现代，创建了一种新方法

# class Prentice(School, master):   # 多继承，继承了多个父类, 优先使用School的属性和方法
#     def __init__(self):
#         self.kungfu = '猫氏'
#
#     def make_cake(self):
#         print('按照猫氏')

# class Prentice(school):  # 继承school 的类别
#    pass
# damao = Prentice()
# damao.make_cake()

class Prentice(School, Master):
    def __init__(self):
        self.kungfu = 'maoshi'

    def make_cake(self):
        print('anzhaomaoshi')
# 如果子类和父类同命，默认用子类的

laoli = Master()
damao = Prentice()   # 使用master 的父类
print(damao.kungfu)
damao.make_cake()
print(prentice.make_cake())