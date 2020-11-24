# debug：找出代码的bug，然后修改，
# 断点：程序执行后，将停留在断点的位置，等待程序员的下一步操作--在序号处右击
# 蓝色表示下一个执行

# 检查是否符合PEP8 标准--黄色表示不符合，红色表示错误
# def前和上一个代码需有2个空行
# 操作符左右各加一个空格，在函数里-指定参数的时候不加空格，end=''
# 用英文 new_name = 1, print('hello_world')

# 位置参数
# 调用有参数的函数--形式参数（形参），实际参数（实参）
# def add2num(a, b):
#     c = a + b
#     print(c)
#
# # 没有参数，也没有返回值
# def person_info():
#     print(27)
#
# person_info()
#
# # 有参数，没有返回值
# def person_info(name):
#     print(name)
#
# # 没有参数，但有返回值
# def person_info():
#     age = 27
#     if age > 10:
#         return name
#
# # 有参数， 也有返回值
# def person_info(age):
#     if age > 10:
#         return age
#
# 参数位置必须对应，不能缺少参数

# 关键字参数：
person_info(name , age )

person_info(name='vera', age='12')
