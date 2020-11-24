a = open('chapter7_short.txt')
for line in a:
    if line.startswith('X-DSPAM-Processed:'):
        b = line.split()
        print(b[1])
    elif len(line) <= 1:
        continue
