# 文件指针：内存加载到缓冲区，硬盘的内容+文件指正加载到缓冲区，
# f为txt类型
# w,r 打开件，文件指针在开始
f = open('love.txt', 'w', encoding = 'utf-8')

# print(f.read())   # 前提是文件存在
f.write('i love you. \r\n')
f.close()

f = open('love.txt', 'a')
f.write('hello\r\n world')

f.tell()  # 返回文件的读写位置，当前位置到开头的距离
# 换行一共2个字符：\r\n
print(f.tell())
f.seek(5, 0)
# 10表示向后移动10；-10表示向前移动10；
# 2表示文件末尾位置，1表示当前位置，0 表示开头位置--文本文件，只能从0 开始读
print(f.seek(10, 0))


f = open('love.txt', 'r+')
print(f.readline())
print(f.readline())
# 会在光标后面接着读，

f.write('abcd')  # 会从指针开始处覆盖
f.close()
