import socket
from shared import *
import random

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 2026))
s.listen(20)

p, g = 251, 2
a = random.randint(2, p-2)

while True:
    c, addr = s.accept()
    print('Connected by', addr)
    A = pow(g, a, p)
    send_message(c, f"{p}:{g}:{A}")
    B = int(recieve_message(c))
    K = pow(B, a, p)
    print('K:', K)
    c.close()