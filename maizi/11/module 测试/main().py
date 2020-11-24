# 1、直接导入模块，并且默认会执行模块--最常用
import module1
import module2
module1.add_num(2,4)
print(module2.__name__)
module1.main()
# 注意模块里面只能留定义，执行和测试需要删除，否则在import时会被执行

#2、从模块导入指定的函数/类/全局变量
from module1 import add_num
add_num(1,2)

# 3、从模块里导入所有的函数/类/全局变量, 但如果module1和module2中有相同的函数，会被替代为最新的函数
from module1 import *
add_num(2,6)

# github 世界上最大的代码托管网站
# stackoverflow 世界上最大的程序员托管平台
# pypi.python.org python所有的包和模块的网站
# C:\Users\l3880\AppData\Local\Programs\Python\Python38-32\Lib 包的所在位置
