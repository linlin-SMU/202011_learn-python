# 用字典处理
mystr = 'i love you '
num_dict = {}
for s in mystr:
    if s not in num_dict:
        num_dict.setdefault(s,1)
    else:
        num_dict[s] += 1
print(num_dict)