# 匿名函数 lamda
def func():
    return 100


print(func())

# lambda 表示创建一个lambda表达式，没有语句块，
# 只能用来编写简单的函数，def 可以处理复杂的业务模型
# lambda：自带return的返回值，即冒号后面，可以是if/
f = lambda : 100
print(f())   # print(lambda:100())

# 带参数的lamda表达式, 冒号之前是参数，冒号之后是返回值，另外一个括号是参数
def num(a,b):
    return a+b

f = lambda a, b : a + b
print(f(10, 20))

def func2(a, b):
    if a > b:
        return a
    else:
        return b

print((lambda a, b : a if a > b else b)(30, 80))
print((lambda a, b, c, d : max(a, b, c, d))(10, 20, 30, 40))
# 判断3个数：c if c > (a if a> b else b) else (a if a > b else b)

# 2. lambda的默认参数
f = (lambda a, b, c=30: a+b+c) * 2
print(f(10, 20, 30))

# 3 元组类型lambda的可变参数
def func(*args):
    pass


f = lambda *args, a=30, b=10: list(args) + [a, b]
print(f(4, 5, 6, 6,7, a=20, b=100))

# 4 字典类型lambda的可变参数
f = lambda **kwargs : (value : key for key, value in kwargs.items())
print(f(name='python', age=27, id=10))

# 5 lambda表达式作为参数传递
def func(a, b, f):   # f = lambda x, y : x + y
    return f(a, b)

func(10, 20, lambda x, y : x + y)