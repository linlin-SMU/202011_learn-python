'''if: else, elif, if嵌套 ，逻辑符'''

age = int(input('请输入你的年龄'))
if age < 18:
    print('欢迎光临')
else:
    print('you are too old!')
print('go back to home!')

if age < 18:
    print('welcome!')
elif age < 20:
    print('hellp')
else:
    print('bye')

chepiao = 1
daoju = 10
yeti = 80
if chepiao:
    print('please go to station')
    if daoju < 10 and yeti < 100:
        print('you hava past it')
    else:
        print('thow it')
else:
    print('go out')

if (1==1) and (10 > 3):  # or
    print('条件成立！')
if not (1==1): # 如果1不等于1，表达式的结果取反
    print('条件成立！')
