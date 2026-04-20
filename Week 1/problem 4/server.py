import socket

def primi_poruku(s: socket.socket) -> str:
    txt = s.recv(1024)
    poruka = txt.decode()
    print(f'Klijent {s.getpeername()} > {poruka}')

    return poruka

def posalji_poruku(s: socket.socket, tsxt: str):
    s.sendall(tsxt.encode())

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 2026))
s.listen(100)
poruka = 'Vi ste prvi korisnik'

while True:
    try:
        c, addr = s.accept()
        print('Povezao se', addr)
        za_slanje = f'Prosla poruka: "{poruka}"'
        posalji_poruku(c, za_slanje)
        print('Saljem >', za_slanje)
        poruka = primi_poruku(c)
    except (OSError, socket.error) as e:
        print('Greska', e)
    except Exception as e:
        print('Neocekivana greska', e)
    finally:
        print('Gasimo konekciju ka klijentu')
        c.close()
    if poruka == 'kraj!':
        break

print('Gasimo server...')
s.close()
