import socket
import threading
from asyncio import exceptions

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 2026))
s.listen(10)

print('Server is listening on port 2026')

clients = []

def safe_closing(s: socket.socket):
    try:
        s.close()
    except OSError:
        pass

def server_closing():
    global clients, s
    s.close()
    for client in clients:
        safe_closing(client)

def handle_client(c:socket.socket, addr:tuple):
    print('Client connected', addr)
    try:
        while True:
            message = c.recv(1024).decode()
            if message == 'ping':
                c.sendall(b'pong')
            elif message == 'end':
                c.sendall(b'goodbye')
            elif message == 'END':
                c.sendall(b'goodbye')
                server_closing()
                break
    except (OSError, socket.error) as e:
        print('Error', e)
    except Exception as e:
        print('Unexpected error', e)
    finally:
        safe_closing(c)

try:
    while True:
        c, addr = s.accept()
        clients.append(c)
        t = threading.Thread(target=handle_client, args=(c, addr))
        t.start()
except (OSError, socket.error) as e:
    print('Error', e)
except Exception as e:
    print('Unexpected error', e)
