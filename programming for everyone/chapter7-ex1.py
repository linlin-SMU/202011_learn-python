a = input('Enter a filename: ')
b = open(a)
for line in b:
    line = line.upper()
    print(line)
