class Hero():
    def __init__(self, name, skill, hp, atk, armor):
        self.name = name
        self.skill = skill
        self.hp = hp  # 生命值
        self.atk = atk
        self.armor = armor  # 护甲值


    def move(self):
        print('%s 正前往事发地点。。' % self.name)


    def attack(self, enemy):
       # 暴击-- 有50%的被暴击率

       import random
       crit = random.randint(1, 2)
       reduce_hp = self.atk * crit - enemy.armor
       enemy.hp -= reduce_hp
       if crit == 2:
           print('暴击', end = '')

       print('%s对 %s 发出了一招强力的%s, 造成了 %d 的伤害' % (self.name, enemy.name,self.skill, reduce_hp))

    def __str__(self):
        return'英雄 <%s> 数据：生命值 %d，攻击力 %d，护甲值 %d' % (self.name, self.hp, self.atk, self.armor)


taidamier = Hero('泰达米尔', '旋风斩', 4200, 260, 400)
gailun = Hero('盖伦', '大宝剑', 4200, 260, 400)

taidamier.move()
gailun.move()

# 回合数
round_num = 1
while True:
    print('\t\t当前为第 %d 回合' % round_num)
    input()
    print(taidamier)
    print(gailun)

    taidamier.attack(gailun)
    if gailun.hp <= 0:
        print('Game Over! %s 体力不支，被 %s 一刀砍倒在地。。' % (gailun.name, taidamier.name))
        break
    gailun.attack(taidamier)
    if taidamier.hp <= 0:
        print('Game Over! %s 体力不支，被 %s 一刀砍倒在地。。' % (taidamier.name, gailun.name))
        break
    round_num += 1
    print('again')
