example = []
while True:
    a = input('Enter a number: ')
    try:
        b = float(a)
        if not b in example:
            example.append(b)
    except:
        break
print('Maximum: ', max(example))
print('Minimum: ', min(example))
