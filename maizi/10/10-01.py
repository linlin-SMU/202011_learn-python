class Master(object):
    def __init__(self):
        self.kungfu = '古法煎饼果子配方'
        self.time = 1
    def make_cake(self):
        print('按照%s制作了一份煎饼果子。。' % self.kungfu)
    def dayandai(self):
        print('大眼袋')

# # 把任务传给了徒弟：
# class Prentice(Master):
#     pass
# laoli = Master()
# damao = Prentice()
# print(damao.time)
# print(damao.kungfu)
# damao.dayandai()

# 从学校学习
class School(object):
    def __init__(self):
        self.kungfu = '现代方法'

    def make_cake(self):    # 该self为init 的self
        print('按照%s制作了一份煎饼果子' % self.kungfu)

    def xiaoyandai(self):
        print('小眼袋')

# class Prentice(School,Master):
#     pass
# laoli = Master()
# damao = Prentice()
# print(damao.kungfu)
# damao.dayandai()

# 3)给了一个全新的配方，猫氏煎饼果子
class Prentice(School, Master):
    def __init__(self):
        self.kungfu = '猫氏煎饼果子'

    def make_cake(self):
        print(self)
        self.__init__()      # 在里面定义的时候，不需要传参
        print('按照猫氏煎饼果子配方')

    def make_old_cake(self):
        print(self)  # self为对象，xiaomao，查询xiaomao的地址，
        # 传参就是传的self的地址，修改的是self本身的性质
        Master.__init__(self)   # 在外面定义的时候需要传参
        print(self)
        Master.make_cake(self)

    def make_new_cake(self):
        School.__init__(self) # 就是普通函数，不过目的是确定参数
        School.make_cake(self)   # 传到school的类


xiaomao = Prentice()
print(xiaomao.kungfu)
xiaomao.make_cake()
xiaomao.make_old_cake()
xiaomao.make_new_cake()
