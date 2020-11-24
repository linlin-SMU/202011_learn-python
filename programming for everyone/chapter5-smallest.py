smallest = None
t = [6, 3, 4, 9]
for tm in t:
    if smallest is None or tm <= smallest:
       smallest = tm
    print('loop: ', tm, smallest)
print('smallest:', smallest, 'good job')
