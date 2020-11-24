class b(object):
    def __init__(self):
        self.num = 10
# boy = b()
# print(boy.num)

# class g(b)
#     pass
# girl = g()
# print(girl.num())

class g(b):  # g为b的子类，如果子类和父类有同名的方法和属性，默认使用子类
    def __init__(self):     # self为对象，xiaomao，查询xiaomao的地址，
        # 传参就是传的self的地址，修改的是self本身的性质
        self.num = 100
        b.__init__(self)

girl = g()
print(girl.num)

num = 10000
num1 = 10000
print(id(num))
print(id(num1))