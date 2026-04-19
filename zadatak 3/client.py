import socket

def primi_poruku(s: socket.socket) -> str:
    txt = s.recv(1024).decode()
    print(f'Server > {txt}')
    return txt

def posalji_poruku(s: socket.socket, txt: str):
    s.sendall(txt.encode())

def chat(server_socket: socket.socket):
    while True:
        poslata_poruka = input('Moja poruka > ')
        posalji_poruku(server_socket, poslata_poruka)
        if poslata_poruka in ['kraj', 'kraj!']:
            break
        primi_poruku(server_socket)

s = socket.socket()
s.connect(('127.0.0.1', 2026))
print('POvezao sam se na server')

chat(s)

print('Gasim konekciju...')
s.close()