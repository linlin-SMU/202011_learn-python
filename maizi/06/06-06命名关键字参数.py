# 命名关键字参数：强制命名关键字参数的个数--某几个参数必须为关键字

def person_info(name, age):
    print(name)
    print(age)

person_info(age = 27, name = 'vera')

def person_info(name, age, *, city)  # * 之后的参数必须为关键字传参
    print(name)
    print(age)
    print(city)

person_info('vera',27, city = 'shenzhen')
