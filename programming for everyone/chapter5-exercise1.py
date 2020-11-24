aa = 1
count = 0
sum = 0
while True :
    A = input('Enter a number: ')
    if A == 'done':
        break
    try:
       B = float(A)
    except:
       print('Invalid input')
       continue
    count = count + 1
    sum = sum + B
print ('ALL DONE')
print('count:', count)
print('sum: ', sum)
print('average: ', sum/count)
