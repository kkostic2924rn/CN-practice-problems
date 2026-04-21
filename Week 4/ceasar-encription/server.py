import socket
from shared import send_message, recieve_message

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 2026))
s.listen(20)

print('Server is listening on port 2026')

while True:
    c, addr = s.accept()
    send_message(c, 'Welcome to server!')
    message = recieve_message(c)
    if message == 'end':
        break

s.close()
