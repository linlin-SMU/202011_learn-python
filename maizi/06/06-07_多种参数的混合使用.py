def num_func(a, b ,c = 20, *args, *kwargs)：
    print(a)
    print(b)
    print(args)
    print(kwargs)

num_func(100, 200, 300, 500, pi = 3.14)
# args = (300, 500)
# kwargs = {pi:3.14} 所有关键字参数为放到一起，放到最后