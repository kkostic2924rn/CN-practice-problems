import socket
from shared import send_message, recieve_message

key = 7

s = socket.socket()
s.connect(('127.0.0.1', 2026))

recieve_message(s, key)
send_message(s, input(), key)

s.close()