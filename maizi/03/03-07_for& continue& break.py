# while 根据条件判断是否满足条件，ex： while True； for 对多个变量进行遍历
# break: 结束整个循环流程; contine: 不执行本次循环但进行下一个循环
s = 'He!llo World'
for i in s:
    if i == '!':
        continue
    print(i, end = '')
else:
    print()
    print('end')  # end 属于for的循环体，如果用break，则不会执行else；
    # 如果循环不会正常结束,有break，则执行else
print( )

# i = 0
# while i < 5:
#     print(i)  # 如果重启print 为换行打印
#     if i == 3:
#         break
#     i += 1

