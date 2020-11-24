t = [6,2,3,7]
largest = None
print('start: ', largest)
for tm in t:
    if largest is None or tm > largest:
        largest = tm
    print('loop: ', tm, largest)
print('largest: ', largest)
