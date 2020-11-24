a = open('chapter7_short.txt')
for line in a:
    line = line.strip()
    if line.startswith('X-DSPAM-Processed:'):
        words = line.split()
        if len(words)>= 2:
            print(words[1])
