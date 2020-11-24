a = open('chapter11.txt')
import re
c = 0
count = 0
for line in a:
    line = line.rstrip()
    b = re.findall('^New Revision: ([0-9]*)', line)
    for d in b:
        d = int(d)
        c = c + d
        count = count + 1
print(c/count)
# get the numbers in a list form
# haw to make average of list when every element is listed?
? use for to pick every element by changing it to integer
