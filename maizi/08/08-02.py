# 文件的读写处理
f = open('text.txt', 'r+', encoding = 'utf-8')  # r+: 文件前提是存在；w+：文件存在与否都是可以的

# 写
f.write('hello ')

# 读
f.read()
f.readline()  # 读取一行内容；读完之后，readline默认在后面第二行开头
f.readline(100) # 向后读取100个字符
f.readlines()  # 返回一个列表，每一行对应列表每一行
print(f.encoding())  # 查看文件编码： GBK/utf-8
print(f.name)  # 查看文件名
f.close()
print(f.closed)  # 如果关闭，则返回True，反之为False

f.close()

# a
# 删除文件，文件还在，该位置可以被覆盖；文件恢复即为找到触头

f = open('text.txt','w',encoding = 'utf-8')
f.write('veravera')  # 数据写入缓冲区
f.flush()  # 数据从缓冲区写入硬盘，不会清空缓冲区，也不会关闭文件
time.sleep(10)  # 执行到这儿的时候，将会停10s





