a = open('chapter7.txt')
b = dict()
for line in a:
    if line.startswith('From'):
        line = line.rstrip()
        words = line.split()
        try:
            times = words[5]
        except:
            continue
        time = times.split(':')
        hour = time[0]
        b[hour] = b.get(hour, 0) + 1
print(b)
# get the hour and corresponding numbers in the dictionary Form

c = list(b.items())
biggest_key = None
biggest_number = 0
for key, number in c:
    print(int(key),number)
    if number > biggest_number:
        biggest_key = int(key)
        biggest_number = number
print('Maxinum hour: ', biggest_key)
print('Maxinum_number: ', biggest_number)
