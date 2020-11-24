url = input('Enter URL: ')
a = url.split('/')
print(a)
hostname = a[2]
print(hostname)

import socket
try:
    mysock = socket. socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((hostname,80))

    cmd = 'GET' + url + ' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(100)
        print(data.decode(), end = '')
        if len(data) < 1:
            break

    mysock.close()
except:
    print('bad URL')
