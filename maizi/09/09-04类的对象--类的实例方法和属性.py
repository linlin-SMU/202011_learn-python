class Hero(object):
    '''定义了一个英雄类，可以移动和攻击'''

    # python 的类里面，2个下划线开始，2个下划线结束，就是魔法方法
    def__init__(self, name, skill, hp, atk, armor):
    # 在类实例化对象之后会自动被调用
    # __init__为构造函数，设计一个类，一定会有一个构造函数
    # 用来初始化变量，或赋值操作
        self.name = name
        self.hp = 200
        self.atk = 45
        self.armor = 2000

    def move(self):
        '''实例方法'''
        print('go %s' % self.name)
        # 在类里面，获取实例变量和实例方法，通过self获取
        # 在类外面，获取实例变量和实例方法，通过对象名获取

    def attack(self):
        print('come')

# 实例化了一个英雄对象：泰达米尔
taidamier = Hero()
# taidamier 为self，在类里面表示对象，用self；类外面用对象名

# # 生命值：hp就是对象达米尔的实例变量
# taidamier.hp = 2600
# # 攻击力
# taidamier.atk = 450
# # 护甲值
# taidamier.armor = 200

print('英雄泰达米尔的生命值：%d' % taidamier.hp)
print(':%d' % taidamier.atk)
print(':%d' % taidamier.armor)

print(taidamier.hp)

taidamier.move()
taidamier.attack()

def func(a, b, c):
    pass

func(10, 20, 30)
taidamier = Hero('泰达米尔'， '旋风斩'， 2600， 4500， 200)
# 构造对象时，参数默认传到

