import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
c = list()
for line in fhand:
    words = line.decode().split()
    for word in words:
        c.append[word]
print(c[:10])
print(len(c))
