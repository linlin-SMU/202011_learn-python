'''Java, C++为强类型语言，涉及到类型检查，为静态语言，在编译前确定好了数据类型
python 为动态语言，在编译时确定好了语言
多态的方式：不关心类型，只要具备该对象特定的属性和方法，名字，生命值等，就为taidamier一类'''
class Hero():
    def __init__(self, name, atk, crit):
        self.name = name
        self.atk = atk
        self.crit = crit
        self.weapon = None

    def __str__(self):
        return '英雄%s数据：攻击力 %d， 暴击值%d’ % (self.name, self.atk, selt.crit)  '

    def get_weapon(self, weapon):
        if not self.weapon:
            pass
        else:
            print('英雄%s卸下了武器' % (self.name, self.weapon.name))
            self.crit -= self.weapon.crit

        self.weapon = weapon
        print('英雄%s装备了武器%s' % (self.name, weapon.name))
        self.atk += weapon.atk
        self.crit += weapon.atk


class Weapon(object):
    def __init__(self, name, atk = 0, crit = 0, xixue = 0):
    # 默认初始化为0，创建的时候会进行赋值
        self.name = name
        self.atk = atk
        self.crit = crit

# class DragonSlayer(object):
#     def __init__(self):
#         self.name = '屠龙刀'
#         self.atk = 100
#         self.crit = 50
#
# class KitchenKnife(object):
#     def __init__(self):
#         self.name = '菜刀'
#         self.atk = 10
#         self.crit = 5


taidamier = Hero('泰达米尔', 60, 0)
wujinzhiren = Weapon('无尽之刃', 80, 20, 30)
taidamier.get_weapon(wujinzhiren)
print(taidamier.atk)
print(taidamier.crit)