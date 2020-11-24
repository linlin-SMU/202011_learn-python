a = open('chapter7.txt')
b = dict()
for line in a:
    if line.startswith('From'):
        line = line.rstrip()
        a = line.split(' ')
        name = a[1]
        b[name] = b.get(name, 0) + 1
print(b)
# get names and numbers in the dictionary Form

c = list(b.items())
big_value = 0
big_name = None
for name, value in c:
    if value > big_value:
        big_value = value
        big_name = name
print(big_name, big_value)
