# 返回一个值
def calc_func(num1, num2, num3):
    '''num1: 左操作数
    num2: 算术运算符
    num3: 右操作符'''
    if num3 == '+':
        return num1 + num2
    elif num3 == '-':
        return num1 - num2
    else:
        pass # 什么也不做，保证代码没有语法错误


print(calc_func(10, 20, '-'))

# 返回多个值
def square_num(num1, num2):
    return num1 ** 2, num2 ** 3    # 输入的变量为元组的形式


print(square_num(2, 3))
s_num1, s_num2 = square_num(10, 20)
print(s_num1, s_num2)

# 局部变量：在函数内部定义的变量；
# 只能在函数内部定义和使用--在函数调用时，变量使用  ex：默认变量，函数停止后就不能用了
# 全局变量：作用范围在模块内部--该python文件
# 如果在局部改变全局变量：
# global a
# a = 100

# 命名空间：为了防止多个变量名冲突，而引入的一种变量名作用范围分组的机制
# 全局命名空间，局部命名空间，内置命名空间（在任意模块都可以使用）

# 命名空间的访问：
# locals(): 在全局下面locals，就是全局；在函数的locals，就是函数的变量
# locals()[num1]: 以字典的形式
# globals()：无论是在全局还是函数，都是全局
# globals()[num2]=

# 命名空间的查找顺序, 变量先在局部查找→全局：
# LEGB-locals, Enclosing function--嵌套函数的命名空间，global--全局命名空间, Builtin--内置，规则

# 命名空间的生命周期： 局部，全局，内置
#