# 异常处理 try except--处理可能出现问题的代码，将代码放到Try里面
# try上面出问题，会立刻转到except上面去执行，不会执行try后面的内容
#  一般情况，try只写一个代码，就是可能出现的一个问题
# open('text.txt','r+')  # r+执行的前提是文件存在
# r：只读模式；r+：读和追加，w：创建空文件；a：追加/创建新文件；a：追加/创建新文件+读
try:
    f = open('text.txt','r+')
    print('---')
except Exception as e:
    print(e) # 会打印为FileExistsError: e
# except Exception as e:
#     print(e) # Exception 为所有异常的父类
# except FileExistsError:
#     print('文件打开失败')
# 如果不为File异常，则会报错
else:
    print('代码有异常')
finally:
    print('不管有误异常，都会执行')
