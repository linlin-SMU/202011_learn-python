# try:
#     f = open('love.txt', 'r')
# except Exception as e:
#     print(e)

# class AgeError(Exception):
#     def __init__(self):
#         self.msg = 'Age_Error: 年龄应该在1-100之间'
#     def __str__(self):
#         return self.msg
#
#
# class Person(object):
#     def __init__(self):
#         self.age = 0
#     def get_age(self):
#         return self.age
#     def set_age(self, num):
#         if num < 0 or num > 100:
#             raise AgeError
#         else:
#             return num
#
# xiaoming = Person()
# xiaoming.get_age()
# try:
#     xiaoming.set_age(300)
# except Exception as e:
#     print(e)

class Test(object):
    def __init__(self, switch):
        self.switch = switch
    def calc(self, a, b):
        try:
            return a/b
        except Exception as result:
            if self.switch:
                print('捕获到异常')
                print(result)
            else:
                raise

a = Test(False)
try:
    a.calc(10, 0)
except Exception as result:
    print(result)


