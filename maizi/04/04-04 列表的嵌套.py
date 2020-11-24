num_list = []
for i in range(1,21):
    if i % 2 == 0:
        num_list.append(i**2)

# [i for i in range(10) if True/...]
numlist1 = [i**2 for i in range(1, 21) if i % 2 ==0]  ## very importtant

schoolnames = [['北京大学','天津大学'],['上海大学','复旦大学','同济大学']]
a = len(schoolnames[1])
print(a)

import random
offices = [[],[],[]]
names = ['A','B','C','D','E','F']
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

i = 1
for templates in offices:
    print('办公室%d的人数为：%d' %(i,len(templates)))
    i += 1
    for tem in templates:
        print(tem, end = '')
    print( )
    print('-' * 30)