import socket

def primi_poruku(s: socket.socket) -> str:
    txt = s.recv(1024).decode()
    print(f'Server > {txt}')
    return txt

def posalji_poruku(s: socket.socket, txt: str):
    s.sendall(txt.encode())

s = socket.socket()
s.connect(('127.0.0.1',2026))
print('Povezao se na server')

primi_poruku(s)
posalji_poruku(s, input('Moja poruka > '))

print('Gasim konekciju...')
s.close()