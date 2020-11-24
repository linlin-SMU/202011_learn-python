a = open('chapter10.txt')
#print(a.read())
b = dict()
c = '1234567890'
import string
for line in a:
    line = line.lower()
    line = line.rstrip()
    line = line.translate(str.maketrans('.', ' '))
    line = line.translate(line.maketrans(c, '          ', string.punctuation))
    print(line)
# modify the text from keeping the space between words to delete the nunmber and punctuations

    words = line.split()
    for word in words:
        b[word] = b.get(word, 0) + 1
print(b)
# get the word and numbers in a dictionary form
for key, value in b.items():
    print(key, value)
