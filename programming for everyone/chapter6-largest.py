largest = None
smallest = None
count = 0
sum = 0
while True :
    A = input('Enter a number: ')
    if A == 'done':
        break
    try:
       B = float(A)
       if largest == None or B > largest:
           largest = B
       if  smallest == None or B < smallest:
           smallest = B
    except:
       print('Invalid input')
       continue
    count = count + 1
    sum = sum + B
print ('ALL DONE')
print('count:', count)
print('sum: ', sum)
print('largest:',largest)
print('smallest:',smallest)
