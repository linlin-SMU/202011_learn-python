# 面向对象：基于对象的概念建立模型
class Heros():
    def __init__(self, name, skill, hp, armor, attack):
        self.name = name
        self.skill = skill
        self.hp = hp
        self.armor = armor
        self.attack = attack

    def move(self):
        print('英雄 %s 正在前往，，，' % self.name)


    def attack(self, enemy):
        import random
        cri = random.randint(1, 2)
        if cri == 2:
            print('暴击')
        reduce_hp = self.attack * cri - enemy.armor
        enemy.hp -= reduce_hp
        print('%s attack %s and %s 的生命值减少了 %d, 现在为 %d' % (self.name, enemy.name, enemy_name, reduce_hp, enemy.hp))


    def __str__(self):
       return '%s--生命值：%d， 防御值：%d，攻击值：%d' % (self.name, self.hp, self.armor, self.attack)


taidamier = Heros('taidamier', '旋风斩', 1000, 100 ,500)
gailun = Heros('gailun', '大风车', 2000, 300, 200)
print(taidamier)
print(gailun)
taidamier.move()
gailun.move()

num = 1
while True:
    taidamier.attack(gailun)
    if gailun.hp <= 0:
        print('taidamier has won')
        break

    gailun.attack(taidamier)
    if taidamier.hp <= 0:
        print('gailun has won')
        break
    num += 1
    print('\t\t 现在是第 %d 回合' % num)