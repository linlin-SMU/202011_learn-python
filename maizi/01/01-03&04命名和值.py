print('hello world')
# 这句代码会打印hello world
'''可以写很多行注释内容
对于括号里的内容，单引号/双引号/三个单引号/三个双引号 都可以用'''

number = 10
name = '司马'
age ='hello'
# 存储的时候，数据就放在内存里，一段就一个字节（byte），一段是存储数据10，一段存’司‘，’马‘，一段存’h‘，’e‘，’l‘，’l‘，’o‘
# 没有存num，num只是程序员和解释器交流的方式；每段都是有地址的，解释器会去根据地址提取数据，存储到内存
# 程序是用来处理数据的，变量是用来出来数据的
'''变量类型：1、数字：int/long/float/complex为复数 (int的长度不可限量）
2、布尔类型bool：true/false
3、字符串：string
4、list[,,有顺序]/turple(集合,,）/dictionary{2:qq,3:oe}'''
b = 1==1
print(type(b))

'''标识符的命名规则：标识符为自定义的名称，不能以数字开头，
由数字、字母和符号只能用_下划线
Andy不等于andy
大驼峰命名法：每一个单词以大写开头-FirstName
小驼峰命名法：第一个单词以小写开头，以后的单词以大写开头-firstName
建议的命名规则my_first_name'''
# 不能使用关键字

a='1234'
print(type(a))
b=int('1234')








