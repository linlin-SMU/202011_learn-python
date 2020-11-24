class A(object): # 类
    def __init__(self, name, energy):
    # 构造函数
        self.name = name   # 实例变量
        self.energy = energy
    def move(self):
        # 实例方法
        print('%s has moved into her dream with %d' % (self.name, self.energy))

me = A('vera', 2300) # 实例化的对象
energy1 = me.energy
print(energy1)
biaoda = me.move()
