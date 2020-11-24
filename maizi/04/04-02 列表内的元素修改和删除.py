# index()：返回列表里指定元素的下标
name_list = ['damao', 'dagou', 'xioamao', 'xiaogou'，11,22,33,44]
if 'damao' in name_list:
    index = name_list.index('damao')
    print(index)
else:
    print('数据不存在')

# 列表的修改
name_list[name_list.index('xiaomao')] = 'henxiaomao' #修改的方法：找到索引值，根据元素下标修改

# 列表的删除
name_list.remove('damao')  remove-配合数值使用
name_list.pop(5)  pop-配合下标使用
name_list.clear() clear-清空所有数据，为空列表
# del 为彻底清除
num = 13
del num
del name_list[0]
del name_list


