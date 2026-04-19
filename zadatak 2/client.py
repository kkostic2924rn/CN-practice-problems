import socket

#slanje jedne poruke serveru
s = socket.socket()
s.connect(('127.0.0.1', 2026))
print('Povezao sam se na server')

poruka = s.recv(1024).decode()
#.decode() -> dekodira poslate enkriptovane podatke
print('Server >', poruka)

txt = input('Moja poruka >')
data = txt.encode()
s.sendall(data)

poruka = s.recv(1024).decode()
print('Server >', poruka)

print('Gasim konekciju...')
s.close()