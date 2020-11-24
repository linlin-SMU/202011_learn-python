while True:
    file_name = input('Enter the file name: ')
    try:
        refile_name = open(file_name)
        break
    except:
        if file_name == 'na na boo boo':
            print("NA NA BOO BOO - You habe been punk'd")
            continue
        else:
            print('File cannot be opened: %s' % file_name)
            continue
count = 0
for line in refile_name:
    count = count + 1
print(count)
