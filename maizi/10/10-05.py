# __del__ 析构函数
import time

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        self.f = open('test.txt', 'a+')

    def get_age(self):
        return self.__age

    def set_age(self, num):
        while num < 0 or num > 100:
            print('输入的年龄不合理')
            num = str(input('请重新输入：'))
        self.__age = num


    def save_info(self):
        self.f.write(self.name)
        self.f.write(str(self.__age))

    def __del__(self):
        print('调用了析构函数，对象%s被删除' % self.name)
        self.f.close()


p = Person('Python', 27)
print(p._Person__age)
print(p.get_age())
p.save_info()

time.sleep(3)  # 暂停3s

print('流程结束，，')
# 这个方法是魔法方法，用来显示一些信息
# 这个方法return一个字符串，并且只有self一个参数
# def __str__(self):
#     return'英雄<%s> 数据：生命值%d' % ()
# 当实例化对象有str之后，打印对象就会打印str 的返回值