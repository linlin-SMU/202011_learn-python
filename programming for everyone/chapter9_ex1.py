a = open('chapter9.txt')
b = dict()
for line in a:
    line = line.rstrip()
    words = line.split()
    for word in words:
        b[word] = b.get(word, 'red')
d = list(b.values())
print(d)

if 'red' in d:
    print('True')
