# print('---1 表示添加名片---')
# print('---2 表示修改名片---')
# print('---3 表示删除名片---')
# print('---4 表示查询名片---')
# print('---其他数字 表示退出名片---')
#
# namecard_dict = {}
# while True:
#     num1 = input('please input a num: ')
#     num = int(num1)
#     if num == 1:
#         name = input('please input a name: ')
#         age = input('pleas input an age: ')
#         namecard_dict[name] = age
#         print(namecard_dict)
#         continue
#
#     elif num == 2:
#         name = input('please input a name: ')
#         if name in namecard_dict.keys():
#             age = input('please inout an age: ')
#             namecard_dict.update({name:age})
#             print(namecard_dict)
#         else:
#             print('the name is not in the system')
#         continue
#
#     elif num == 3:
#         name = input('please input a name: ')
#         if name in namecard_dict.keys():
#             del namecard_dict[name]
#         else:
#             print('the name is not in the system')
#         continue
#
#     elif num == 4:
#         name = input('please input a name: ')
#         if name in namecard_dict.keys:
#             print(namecard[name])
#         else:
#             print('the name is not in the system')
#
#     else:
#         print('end!!')
#         break

# aa = "[['vera', 20], ['Bob', '30']]"  为字符的list， 用eval(aa)

import os
info_list = []
def load_info():
    global info_list   # 声明为全局变量--info_list 为全局变量
    f = open('card_info.txt', 'r')
    info_list = eval(f.read())
    f.close()

def save_info():
    f = open('card_info.txt', 'w', encoding = 'utf-8')
    f.write(str(info_list))
    f.close()

def add_info():
    name = input('please input a name: ')
    age = input('pleas input an age: ')
    info_list.append([name, age])
    print(info_list)

def modify_info():
    name = input('please input a name: ')
    if name in info_list:
        age = input('please inout an age: ')
        num1 = info_list.index('name')
        info_list[num1][1] = age
        print(info_list)
    else:
        print('the name is not in the system')

def main():
    if os.path.exists('card_info.txt'):   # 查询是否有该文件存在，返回True
        load_info()
    while True:
        command = int(input(''))
        if command == 1:
            add_info()
            continue

        elif command == 2:
            modify_info()
            continue

        else:
            print('End!!')
            break

print('流程开始！')
main()
save_info()
print(card_info.read())
