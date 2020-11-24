# [[], [], []]
collections = []

def add_info():
    name = input('please input a name: ')
    gender = input('please input a gender: ')
    collections.append([name,gender])
    print(collections)
    # break 不能单独放在函数里面

def delete_info():
    name = input('please input a name: ')
    for collection in collections:
        if name in collection:
            collections.remove(collection)
            print(collections)
            break  # break 控制for的，直到找到了名字为止
    else:
        print('the name is not in the collections')  # else 表示为for，到所有找完之后

def look_for_info():
    name = input('please input a name: ')
    for collection in collections:
        if name in collection:
            print(collection)
            break
    else:
        print('this name does not exist')

while True:
    num = input('please input a number: ')
    if num == '1':
        add_info()
        continue

    elif num == '2':
        delete_info()
        continue

    elif num == '3':
        look_for_info()
        continue

    else:
        break
print(collections)