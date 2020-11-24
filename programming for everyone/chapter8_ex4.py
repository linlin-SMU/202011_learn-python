example = []
a = open('chapter8.txt')
for line in a:
    line = line.rstrip()
    line = line.split(' ')
    for word in line:
        if word in example:
            continue
        else:
            example.append(word)
print(example)
