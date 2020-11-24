sum = 0
count = 0
b = open('chapter7-long.txt')
for line in b:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        c = line.find(' ')
        d = float(line[c+1:])
        sum = sum + d
        print(d)
print(count, sum)
print('average: ', sum/count)
