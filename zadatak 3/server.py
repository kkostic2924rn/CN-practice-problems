import socket

def primi_poruku(s: socket.socket) -> str:
    txt = s.recv(1024)
    print(f'Klijent {s.getpeername()}> {txt}')
    return txt

def posalji_poruku(s: socket.socket, txt: str):
    s.sendall(txt.encode())

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 2026))
s.listen(5)

def chat(client_socket:socket.socket):
    poruka = ''
    while True:
        poruka = primi_poruku(client_socket)
        if poruka in ['kraj', 'kraj!']:
            break
        posalji_poruku(client_socket, poruka)

        return poruka

while True:
    poruka = ''
    try:
        c, addr = s.accept()
        print('Klijent se povezao')
        poruka = chat(c)
    except (OSError, socket.error) as e:
        print('Greska', e)
    except Exception as e:
        print('Neocekivana greska', e)
    finally:
        print('Gasimo konekciju ka klijentu')
        c.close()
    if(poruka == 'kraj'):
        break

print('Gasimo server...')
s.close()