# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
#
# line = 1
# while line <= 5:
#     print('*' * 5)
#     line += 1
# print('流程结束！')

# 打印九九乘法表
line = 1
while line <= 9:
    j = 1
    while j <= line:
        print('%d * %d = %d' % (line, j, line*j), end = '\t')
        j += 1
    line += 1
    print()  # 控制换行
