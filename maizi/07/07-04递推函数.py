# 递归函数：
i = 5
num = 1
while i >= 1:
    num += i
    i -= 1
print(num)

num = 1
for i in range(5, 0, -1):   # -1 表示输入的函数为倒序
    num *= i
print(num)

def func5(num):
    return 1

def func4(num):
    return num * func5(num - 1)

def func3(num):  # 3 * 2!
    return num * func4(num - 1)

def func2(num):  # 4* 3!
    return num * func3(num - 1)

def func1(num):   # 5 * 4!
    return num * func2(num - 1)

# o递推函数：不是一直调用自己，而是调用自己的拷贝,返回值会调用给它的拷贝函数
# 2. 一定要有一个结束条件，不再调用函数，反之，会让系统崩溃--一般公司禁止用递归函数
def func(num):
    if num == 1:
        return(num)
    else:
        return num * func(num - 1)
