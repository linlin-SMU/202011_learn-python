# sort 列表排序-数字→a →b →A →B； 反之reverse=True
num_list = [11,22,33,100]
num_list.sort(reverse= True)
print(num_list)
# sorted: 排序之后返回新列表
num_list2 = sorted(num_list, reverse = True)
print(num_list2)

# 浅拷贝
numb_list2 = num_list # 如果修改了num_list2, num_list 也会被修修改

# 深拷贝
num_list3 = num_list.copy() # 修改3，对num_list 没有影响

