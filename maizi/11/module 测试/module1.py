__all__ = ['add_num'] #只允许add_num 被导入，只作用于from module1 import *

# python 中模块的使用--协同开发，模块化编程
# main() --模块的入口
def add_num(a, b):
    '''打印2个参数的和'''
    print(a+b)

 # 写完代码之后，一定先测试好