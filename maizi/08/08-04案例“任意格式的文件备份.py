import os
love = os.getcwd()
print(love)   # 查看当前文件的绝对路径
love_list = os.listdir(love)   # 以列表的形式返回当前文件所在的文件夹的文件
print(love_list)

file_name = input('请输入需要备份的文件：')
if file_name not in love_list:
    print('文件不存在！')
else:
    position = file_name.rfind('.')   # find: 为从左向右，找到第一个点的为孩子；
    # rfind为从右向前，找到第一个点的位置
    newfile_name = file_name[:position] + '_backup' + file_name[position:]

data = source_file.read()   # 为一次性读取所有数据，如果文件过大，则会导致打开文件失败
backup_file.read()

while True:
    data = source_file.readline()   # 则改成分行进行读取
    if len(data)  == 0:
        break
    backup_file.write(data)