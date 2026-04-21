import socket
from shared import *
import random

s = socket.socket()
s.connect(('127.0.0.1', 2026))

message = recieve_message(s)
p, g, A = map(int, message.split(':'))
b = random.randint(2, p - 2)
B = pow(g, b, p)
K = pow(A, b, p)
send_message(s, str(B), K)
print('K:', K)