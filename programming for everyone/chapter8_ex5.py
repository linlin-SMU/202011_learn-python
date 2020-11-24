a = open('chapter7.txt')
count = 0
for line in a:
    if line.startswith('From'):
        count = count + 1
        b = line.split(' ')
        print(b[1])
print('There were %d lines in the file with From as the first word' % count)
