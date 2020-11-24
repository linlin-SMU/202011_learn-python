import re
b = 0
a= open('chapter7.txt')
for line in a:
    line = line.rstrip()
    if re.search('^From:', line):
        b = b +1
print('%s had %d lines tha matched ^From.' %(a, b))
