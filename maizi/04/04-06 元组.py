# 元组——列表之后不可修改 tuple()
t1 = tuple(range(1,10,3))
t2 = (100, ) # 创建一个数的元组
t3 = (i for i in range(1,8,2) if i % 2 == 0)
print(t3)

# index 返回元组下标值
t5 = ([1, 2, 3], 100, 200, 300, 'hello world') # 元组的元素不可变，但元组的元素的元素可变
t5[0][1] = 5
print(t5)
