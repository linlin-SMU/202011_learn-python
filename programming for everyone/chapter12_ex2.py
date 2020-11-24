a = list()
import socket
mysock = socket. socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4e.com',80))
cmd = 'GET https://www.py4e.com/ HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(200)
    data = data.decode()
    if len(data) < 1:
        break
    a.append(data)
print(a[:3000])
print(len(a))
# count the len of whole file but show the first 3000 bytes
mysock.close()
