a = open('chapter7.txt')
b = {}
for line in a:
    line = line.rstrip()
    if line.startswith('From'):
        words = line.split()
        mail = words[1]
        b[mail] = b.get(mail, 0) + 1
print(b)
