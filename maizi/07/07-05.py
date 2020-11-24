# 什么是文件
# 文本文件：用文本编辑器打开--excel；二进制文件：需要指定编辑器--MP3, JPEG
# 文件缓冲区
# 【高速设备】 缓冲区 【低速设备】
# CPU, 内存            硬盘
  3GB/S    临时中转站   80MB/S

# 文件操作
# r: 只读文本文件，文件存在/文件不存在，报错
# rb：只读二进制文件、
# r+ ： 读+写：写的时候，从只覆盖写了的
# w：文件存在，则清空/文件不存在，新建/wb
# a：文件存在，加在末尾/文件不存在，新建

# 打开文件
f = open('helloworld.txt', 'w', encoding = 'utf-8')  # write 重新写/r/a 为append
# 按utf-8打开文件，同时文件转换为utf-8编码模式

f.write('hello world') # 表示向文件名写入字符串
f.read()  # 返回字符串

# 关闭文件，清空缓冲区数据
f.close()

# 中文GBK-- 文本以GBK 保存；ASCII--美国
# 打开cmd，在灰色条上右击→属性→看windows是怎样的编码--ASCII
# 1 string以Unicode-- 字符都是3-4个字节形式成为码点→→2 bytes，二进制的模式以UTF-8 是世界上流行的编码模式（字母和数字全为1个字节储存）
# 1→2：encode & 2→1：decode

# 文件的编码
f.encoding() # 打印文件的编码模式

# unicode→ 整数 ord() unicode: 仅限于单个字母和特殊符号，即单个字符a
# 整数 → unicode chr()

# string： 在python3的储存形式有2种，函数返回为string形式，直接输入为byte形式
# x = '您好'  # 以bytes储存，显示的类型仍为str
# x = u'您好'  # 以unicode储存，显示的类型为str

# import os
# y = os.getcwd()  # 以string方式储存
# print(y.encode('utf-8')) string→byte

'''self.response.out.write("你好"+self.request.get("argu"))
'ascii' codec can't decode byte 0xef in position 0: ordinal not in range(128)的错误
unicode指的是万国码，是一种“字码表”。而utf-8是这种字码表储存的编码方法。unicode不一定要由utf-8这种方式编成bytecode储存，也可以使用utf-16,utf-7等其他方式。目前大多都以utf-8的方式来变成bytecode。
其次，Python中字符串类型分为byte string 和 unicode string两种。
如果在python文件中指定编码方式为utf-8(#coding=utf-8)，
那么所有带中文的字符串都会被认为是utf-8编码的byte string（例如：mystr="你好"），
但是在函数中所产生的字符串则被认为是unicode string。'''
# 1.将字符串全都转成byte string。
# self.response.out.write("你好"+self.request.get("argu").encode("utf-8"))
# 2.将字符串全都转成unicode string。
# self.response.out.write(u"你好" + self.request.get("argu"))
# #
# s = '您好'→ s.encode() 为byte类型
# b'您好' → s.encode().decode() 为str类型
