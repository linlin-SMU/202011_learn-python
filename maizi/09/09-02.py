
print('---1 增加功能---')
print('---2 删除功能---')



import os
if os.path.exists('link_dict.txt'):
    f = open('link_dict.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()
else:
    f = open('link_dict.txt', 'w')
    f.close()

link_dict = {}
while True:
    num1 = input('请输入数字：')
    num = int(num1)
    if num == 1:
        link = input('请输入网址：')
        passcode = input('请输入密码：')
        if link in link_dict.keys():
            print('该网址已经存在')
        else:
            link_dict[link] = passcode
            print(link_dict)
            continue

    elif num == 2:
        link = input('请输入网址：')
        if link in link_dict.keys():
            print('该网址已经存在')
        else:
            del link_dict[link]
            print(link_dict)
            continue

    else:
        print('End!')
        break

f = open('link_dict.txt', 'a')
f.write(link_dict)
print(f.read())
f.close()




