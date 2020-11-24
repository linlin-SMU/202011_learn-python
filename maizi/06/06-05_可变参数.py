# def num(*args)  收集所有的位置参数，合为元组turple
# def num(**kw)  收集所有的关键字参数，合为字典;
# 为可变参数--不确定调用时的参数个数

def person_info(*args):
    print(type(args))
    for i in args:
        print(i)
person_info('vera','22','female')

def person_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
person_info(name = 'vera', age = 18, job = 'programmer')