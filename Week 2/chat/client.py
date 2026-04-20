import socket

s = socket.socket()
s.connect(('127.0.0.1', 2026))

print('Connected to server')

while True:
    s.sendall(input('username >').encode())
    answer = s.recv(1024).decode()
    print(answer)
    if answer == 'Username accepted':
        break

while True:
    s.sendall(input('message >').encode())
    answer = s.recv(1024).decode()
    print(answer)
