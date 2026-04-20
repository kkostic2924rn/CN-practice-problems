import socket

s = socket.socket()
s.connect(('127.0.0.1', 2026))

print('Connected to server')

try:
    while True:
        sending_message = input('> ')
        s.send(sending_message.encode())
        answer = s.recv(1024).decode()
        print(answer)
        if answer == 'goodbye':
            break
except (OSError, socket.error) as e:
    print('Greska', e)
except Exception as e:
    print('Neocekivana greska', e)
finally:
    s.close()