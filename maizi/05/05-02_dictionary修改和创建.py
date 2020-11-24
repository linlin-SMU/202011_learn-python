# dictionary--index一般用字符串表示 键：值
'''[1, 2, 'vera', 1, 2]
{'name':'vera', 'age':'18'}
{1, 2, 3, 4}--集合去重'''
num_dict = {'name':'python', 'age':'26', }
print(num_dict['name'])

len(num_dict)
dict.keys()   # 返回所有的键
dict.values()  # 返回所有的值
dict.items()  # 返回所有的值和键

for key, value in dic.items()

## 创建空字典
num_dict = {}
print(num_dict.fromkeys('abcd', 10))  # 第一参数为键的序列，第二个参数为值

## 字典的添加和修改
num_dict['name'] = 'python'  # 没有name 则添加，反之则修改name的值

# setdefault()
print(num_dict.setdefault('name'))  # 如果有这个键，则返回这个键对应的值；
# 没有则返回None，同时创建键值对（'name':'None'）
print(num_dict.setdefault('name', 'vera')) # 如果没有则增加，反之就修改

# get()
num_dict.get('name')  # 如果有这个键，就返回这个键的值，没有就返回None、不会有增加新键值对
if num_dict.get('test'):
    print(name_dict['test'])
else:
    print('不存在')

# update()  修改已有的，创建没有的，修改的是在原来的基础上，不会创新
info_dic = {'name':'vera', 'age':10}
newinfo_dict = {'name':'Bob', 'gender':'male'}
newinfo_dict.update(info_dict)
print(info_dict)