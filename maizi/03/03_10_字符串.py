# [] 表示下标注， 从0开始, [0], [0, 2]-切片
s = 'hello world！'
print(s[:])  # print(s)
print(s[:0]) # ! 为0，d为-1
# 字符串是不可变数的类型 s[1] = E为错误
# 可变数据类型： 列表，字典
# 不可变数据类型：元组
mm = [1, 2, 3]
mm[1] = 23
print(mm)

# replace(): 替换mystr中指定的子串，为另一个字符串
mystr = '  i itcast you   '
str1 = mystr.replace('itcast', 'itlove')

# 在[-5, 256]之间，python创建好了地址（id查地址），方便用户取值、
print(id(29))

# strip(): 去除首尾空格，lstrip(): 去除左边空格，rstrip()去除右边空格
print(mystr.strip())

# split(): 按指定的分隔符分割字符串，并返回分隔之后的列表--3个空格连在一起，就是3个空格
print(mystr.strip().split(' '))
print(mystr.strip().partition('and'))   # and 分为3部分，字符前一部分，and一部分，字符后一部分

print(mystr.lower())    # 将myst的所有字符串转换为lower()
print(mystr.upper())
print(mystr.swapcase())    # 大小写互转
print(mystr.captalize())   # 第一个字母大写，其他小写
print(mystr.center(100))   # 在100的长度中。string居中对齐
print(len(mystr))       # 看 mystr的长度

print(mystr.isalpha())   # 判断是否由纯字母组成，是为True，否为False
print(mystr.isdigital)   # 判断是否由纯数字组成，是为True，否为False


print(mystr[:-1])
