import os

# 返回当前文件所在的绝对路径--从根目录开始到指定路径的完整路径
file_path = os.getcwd()  # 返回当前文件的绝对路径
print(file_path)
# 相对路径--cd/. 当前目录/.. 上一层目录/dir   cd..\software\dir

# 转义字符
s = 'hello\t\n\tworld'
# \t: tab; \n: 换行
s = r'hello\\tword'   # 表示所有的转移字符失效

# 判断文件是否存在, 返回布尔值
print(os.path.exists(r'.\test.txt'))

# 删除当前目录，相对目录和绝对路径的文件
os.remove(r'hello.text')

# 给指定文件重命名
os.rename(old_name, new_name)

# 获取目录下的所有文件，返回一个列表
file_name_list = os.dir(r'C:\Users')
print(file_name_list)

# 在指定位置创建目录，为一个目录 (如果目录存在则报错）
os.mkdir(r'C:\Users\test')
os.mkdirs(r'C:\Users\test\test')  # 创建多级目录

# 删除指定路径下的目录
os.rmdir('C:\Users\test\test')