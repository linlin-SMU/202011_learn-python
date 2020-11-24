a = open('chapter7.txt')
b = {}
for line in a:
    line = line.strip()
    if line.startswith('From'):
        words = line.split()
        word = words[1]
        w = word.split('@')
        domain_name = w[1]
        b[domain_name] = b.get(domain_name,0) + 1
print(b)
