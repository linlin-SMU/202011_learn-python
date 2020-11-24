#ctrl+c 中断代码执行
def load_info():
    global info_list
    f = open('text.txt', 'r')
    f.close()


try:
    load_info()
except:
    print('load_info()异常')

class AgeExceptionError(Exception):
    def __init__(self):
        self.error_msg = 'AgeError: 年龄应在1-100之间'

    def __str__(self):
        return self.error_msg

class Person(object):
    def __init__(self):
        self.__age = 0

    def get_age(self):
        return self.__age

    def set_age(self, num):
        if num < 0 or num > 100:
            # raise 抛出异常，异常为自定义的异常类
            raise AgeExceptionError()  # （）返回对象，raise为异常的对象，用于except/return为返回对象
        self.__age = num

p = Person()
print(p.get_age())
try:
    p.set_age(300)  #可能出现的异常放在try里面
except Exception as e:  # exception包括了AgeExcetionError，所以可以捕获到set里面的AgeExceptionError
    print(e)  # 或者可以为e.error_msg

