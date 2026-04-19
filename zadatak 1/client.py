import socket

s = socket.socket()
s.connect(('127.0.0.1', 2026))
print('Povezao sam se na server')
print('Gasim konekciju...')
s.close()