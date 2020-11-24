# 列表的合并 五角星
list1 = [10, 20, 30]
list2 = ['a', 'b', 'c']
print(id(list1))

list3 = list1 + list2
list1 += list2  # list1 中增加了list2，在list1中修改

# 将字符串转为列表 五角星
mystr = 'hello world hi love'
print(mystr.split(' '))  # 字符→列表：按分隔符成list
list(mystr)  # 字符→列表：将字符串的每个字符转换为元素

# 将列表转成字符串 五角星
str_list = ['A', 'B', 'B']
print('and'.join(str_list)) # join: 只能转全为字符串的列表，and连接;
num_list = [1, 2, 3, 4]
print(' '.join(str(i) for i in num_list))  # 对于num类型，先转为str

# 类型判断： 判断对象是否为指定的类型，True/False
password = input('请输入密码：')
print(type(password)) # input输入为str
if isinstance(password, str):
    print(password)
else:
    print('密码不正确')

num_list = [1, 2, 3, [3, 4, 5], [7, 8]]
for num in num_list:
    if isinstance(num, list):
        for i in num:
            print(i)
    else:
        print(num)

# enumerate: 返回一个列表，包含了列表的下标和值
num_list2 = [10, 20, 30]
for index, value in enumerate(num_list2):
    print(index, value)
for i in enumerate(num_list2):
    print(i)
