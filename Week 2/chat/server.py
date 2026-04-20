import socket
import threading
from collections import defaultdict

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 2026))
s.listen(10)

print('Server is listnenig on port 2026')
usernames = set()
messages = defaultdict(list)
# username -> list of messages for that user

def recieve_message(s: socket.socket) -> str:
    message = s.recv(1024).decode()
    print(f'Client [{s.getpeername()}] >', message)
    return message

def send_message(s:socket.socket, txt: str):
    s.sendall(txt.encode())

def process_client(c: socket.socket, addr: tuple):
    global usernames
    print('Connected', addr)
    while True:
        username = recieve_message(c)
        if username not in usernames:
            usernames.add(username)
            send_message(c, 'Username accepted')
            break
        else:
            send_message(c, 'Username rejected, send a new one')

    print('Username secured')
    while True:
        message = recieve_message(c)
        if message == 'citaj':
            send_message(c, '['+str(messages[username])+']')
            messages[username].clear()
        else:
            target_username, message = message.split(':', 1)
            message = f'{username}:{message}'
            messages[target_username].append(message)
            send_message(c, 'Message recieved and saved')

while True:
    c, addr = s.accept()
    t = threading.Thread(target=process_client, args=(c, addr))
    t.start()
