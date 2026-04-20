import socket
from logging import exception
from time import sleep

def primi_poruku(s: socket.socket) -> str:
    txt = s.recv(1024).decode()
    print('Server: ', txt)
    return txt

def posalji_poruku(s: socket.socket, txt: str):
    s.sendall(txt.encode())

for i in range(100_000):
    try:
        s = socket.socket()
        s.connect(('127.0.0.1', 2026))
        primi_poruku(s)
        posalji_poruku(s, f"Poruka broj {i}")
        s.close()
    except OSError as e:
        print('Greska: ', e)
        sleep(50)