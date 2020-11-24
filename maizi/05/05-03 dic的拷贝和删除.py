# copy()
name_dict = {'name':'python','age':'23','gender':'female'}
newname_dict = name_dict.copy()   # 创建一个新字典，而不是引用
# 浅拷贝-对象和值都一样
name_dict1 = newname_dict
# 深拷贝-值一样，对象不一样
newname_dict = name_dict.copy()
# 深深拷贝-
import copy
newname_dict = copy.deepcopy(name_dict)

# pop()
name = newname_dict.pop('name')  # 删除name键值对，返回name对应的值
name = newname_dict.pop('name', 'hello')  # 删除name，没有name的话，返回hello

# popitem()
key, value = newname_dict.popitem() # 拆包（从后向前拆分元组，并用变量接收，一次只拆分一个）
print(key)
print(value)
print(newname_dict)

key_list = []
value_list = []
for i in range(len(newname_dict)):
    key, value = newname_dict.popitem()
    key_list.append(key)
    value_list.append(value)

newname_dict.clear()  # 清空字典，但不删除字典
del newname_dict  # 彻底删除字典



