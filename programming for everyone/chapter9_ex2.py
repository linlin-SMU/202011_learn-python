a = open('chapter7.txt')
b = dict()
for line in a:
    if line.startswith('From'):
        line = line.rstrip()
        line = line.split(' ')
        try:
            time = line[2]
            b[time] = b.get(time, 0) + 1
        except:
            continue
print(b)
