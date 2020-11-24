# 把学校的配方、师父的配方和自己的配方也传承下去
# 老师傅精通煎饼果子制作
class Master(object):
    def __init__(self):
        self.kungfu = '古法煎饼果子配方'

    def make_cake(self):
        print('按照 %s 制作了一份煎饼果子。。' % self.kungfu)

    def dayandai(self):
        print('大眼袋')

# 2）
class School(object):
    def __init__(self):   # 如果是haha，在以后引用school，也是haha
        self.kungfu = '现代方法'

    def make_cake(self):
        print('按照 %s 制作了一份煎饼果子' % self.kungfu)

    def dayandai(self):
        print('小眼袋')

class Prentice(School, Master):
    def __init__(self):
        self.kungfu = '猫氏煎饼果子配方'
        self.__money = 1

    def get_money(self):
        return self.__money

    def set_money(self, num):
        self.__money = num


class PrenticePrentice(Prentice):  # 继承prentice
    pass
pp = PrenticePrentice()
print(pp.get_money())
# print(pp.__money)

pp.set_money(1000)

'''面向对象的3大特性：封装、继承和多态
封装
1、将属性和方法放在一起作为一个整体，然后可以在类里面直接访问
2、隐藏内部实现细节，只需要和对象数据和方法交互就可以了
3、对类的属性和方法增加访问权限控制'''

# money不继承，私有属性和私有方法
# 私有属性：不能通过对象直接访问；为__开头
# damao = Prentice()
# damao.__money  不能成功
# 私有方法：不能通过对象直接访问；
# 私有属性和私有方法不会被子类继承，子类也无法访问

# 则可以写一个方法名来获取
# 或者
print(pp._Prentice__money)
# pp._Prentice__money = 50   修改money的变量
# 如果看到了_开头的属性，用法和公有没有区别，但是表示不去随意修改和访问

# python 本身没有强制性的机制访问私有变量，一切靠自觉

'''多态？？
公有权限：public
保护权限：protected
私有权限：private'''



