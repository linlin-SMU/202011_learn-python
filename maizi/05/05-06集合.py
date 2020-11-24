# 创建集合 {}
num_set = set()  # num_set = () 不能创建
set1 = {i for i in range(1, 20, 1)}

# 列表、字典和集合的互相转换
num_list = [10, 20, 30, 43, 10]
num_set = set(num_list)  # 转换为集合之后去重
newnum_list = list(num_set) # 集合转为列表
num_dict = {}
item = 0
for newnum in newnum_list:
    key = newnum
    item += 1
    num_dict.setdefault(key, item)
print(num_dict)

num_set.add('hello')
num_set.update([100,210,300]) # 多个元素添加的时候，输入以列表的形式，添加的时候，挨着取出来
print(num_set)  # 字典和集合不能排序，不支持下标的数字型索引→可以先转成列表，再排序

num_set.remove(600)  # remove可以删除指定数据，如果数据不存在，则报错
num_set.discard(600)  # discard 可以删除指定数据，如果数据不存在，则没有任何操作
num_set.pop()  # 从前开始删除，并返回删除的数据

# 一般集合会转成列表进行后续操作？？；

# 求集合的交集 a & b
a = {1, 2, 3, 4}
b = {3, 5, 5, 1}
a & b
# 并集 a | b  对于list a+b
# 差集 a 有的b没有 a - b

# 其他：+






