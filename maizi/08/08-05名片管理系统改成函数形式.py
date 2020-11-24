# 一般情况下用main表示程序入口 main()
print('---1 表示添加名片---')
print('---2 表示修改名片---')
print('---3 表示删除名片---')
print('---4 表示查询名片---')
print('---其他数字 表示退出名片---')

def add_namecard():
    name = input('please input a name: ')
    age = input('please input an age: ')
    namecard_dict[name] = age
    print(namecard_dict)

def update_namecard():
    if name in namecard_dict.keys():
        age = input('please input an age: ')
        namecard_dict.update({name: age})
        print(namecard_dict)
    else:
        print('the name is not in the system')

def delete_namecard():
    if name in namecard_dict.keys():
        namecard_dict.pop(name)
        print(namecard_dit)
    else:
        print('the name is not in the system')

def searchfor_namecard():
    if name in namecard_dict.keys():
        print(namecard_dict.get(name))
    else:
        print('the name is not in the system')

namecard_dict = {}
import os

if os.path.exists('love.txt'):
    f = open('love.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()
else:
    f = open('love.txt', 'w', encoding = 'utf-8')
    f.write(eval({vera : 22}))
    f.readlines()
    f.close

while True:
    num = input('please input a num: ')
    num = int(num)
    if num == 1:
        add_namecard()
        continue

    elif num == 2:
        name = input('please input a name: ')
        update_namecard()
        continue

    elif num == 3:
        name = input('please input a name: ')
        delete_namecard()
        continue

    elif num == 4:
        name = input('please input a name: ')
        searchfor_namecard()
        continue

    else:
        print('end!!')
        break

f = open('love.txt', 'w', encoding = 'utf-8')
f.write(str(namecard_dict()))    # 字典不能通过str转换写入文本文件，list可以
f.readlines()
f.close()
print('流程结束')