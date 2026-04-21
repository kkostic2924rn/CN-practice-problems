import socket
from shared import send_message, recieve_message

s = socket.socket()
s.connect(('127.0.0.1', 2026))

print('Connected')

recieve_message(s)
send_message(s, input())

s.close()