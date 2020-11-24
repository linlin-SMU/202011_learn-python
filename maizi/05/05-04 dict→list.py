num_list = [i for i in range(1,20,1) if True] # 列表推导式
num_dict = {i:i**2 for i in range(1,21,1) if True}  # 字典推导式

# 2个列表转为dictionary
key_list = ['name', 'age', 'id']
value_list = ['python', 18, 110]
key_dict = {key_list[i]:value_list[i] for i in range(len(key_list))}

# dic 转为 2个list
key_list1 = []
value_list1 = []
for key, value in key_dict.items():
    key_list1.append(key)
    value_list1.append(value)
print(key_list1)
print(value_list1)

# dic的键值对互相转换
{value:key for key, value in key_dict.items()}

#