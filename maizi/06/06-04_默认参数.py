# 函数的默认参数
def person_info(name, age = 30):
    print(name)
    print(age)

print('python', 27)  # 如果没有指定默认参数的值，就使用默认参数
# 一般把默认参数写在后面/ 所有参数都是默认参数

# 默认参数一定不能使用可变数类型--列表，字典
# def add_100(num_list = [])
#       num_list.append(100)
#       print(num_list)

# def add_100(num_list = None):
#     if num_list == None:
#         num_list = []
#     num_list.append(100)

def person_info(name = 'vera', age = '22')
    print(name)
    print(age)
person_info(Bob, 30)

# 万物皆对象--有类型的对象
num = 10
print(id(num))
print(id(10))
# 都是引用的同一个10





