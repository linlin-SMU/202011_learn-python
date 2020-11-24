i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print('%d * %d = %d' % (j, i ,j*i), end='')
#         j += 1
#     i += 1
#     print()

# for i in range(1, 10):
#     j = 1
#     for j in range(1, i+1):   # range 为左闭右开
#         print('%d * %d = %d' % (j, i, j*i), end='')
#         j += 1
#     i += 1
#     print()

# 判断是某年月第几天
day = input('请输入年月日： ')
# 20170203
year = int(day[:4])
month =int(day[4:6])
day = int(day[6: ])

day_list = [31, 28, 21, 30, 31, 30 , 31, 31, 30, 31,30, 31]
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    # 可以改成函数 is_ruinian--返回True和函数用is 开头
    # def is_runnian[year]:
    #     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0:
    #         return True
    day_list[1] = 29
    print('闰年')
    # 判断年份是否为闰年：能被4整除，但不能被100整除；能被400整除
else:
    print('不是闰年')
for i in range(month - 1):
    day = day + day_list[i]

print(day)