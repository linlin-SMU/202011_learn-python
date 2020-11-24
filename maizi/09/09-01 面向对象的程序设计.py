print('hello world')
def print_info():
    print('hello world')
    print('hello world')

class A:
    brand = apple
    xianka = 'GTX1080'
    cpu = 'Ryzen 7* 1800x'
my_pc1 = A()
your_pc1 = A()
id(my_pc1)
id(your_pc1)
my_pc1.cpu
your_pc1.xianka
# 面向过程的程序设计：从计算机的角度思考问题
# 面向对象的程序设计（OOP）: Objected oriented Programming
# 类 对象--模具 产品--配电脑的配置单 电脑
# 类 为多个函数的集合

# 创建类 class A:
a = A()
a.info()  # 当对象调用实例方法时，
# python会自动将对象本身的引用作为参数
id(a)  # 打印对象的id，会默认打印对象在的内存地址
b = A()
b.info()
print(b)

