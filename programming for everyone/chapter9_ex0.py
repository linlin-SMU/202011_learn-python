a = open('chapter8.txt')
b = dict()
for line in a:
    line = line.rstrip()
    words = line.split()
    for word in words:
        b[word] = b.get(word, 0)+1
# count the number of words(remember the way in counting the number of characters)
b={'a':2 , 'b': 4, 'c' :3}
big_word = None
big_count = None
for count, word in b.items() :
    if big_count == None or count > big_count:
        big_count = count
        big_word = word
    else:
        continue
print('big_count: ',count,'big_word: ',word)
# ??
