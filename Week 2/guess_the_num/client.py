import socket

s = socket.socket()
s.connect(('127.0.0.1', 2026))

print('Connected to server')

try:
    while True:
        sending_message = input('> ')
        try:
            int(sending_message)
        except:
            print('Message is not type int.')
            continue
        s.sendall(sending_message.encode())
        answer = s.recv(1024).decode()
        print(answer)
        if answer == 'Correct!' or 'Winner' in answer:
            break
except (OSError, socket.error) as e:
    print('Error', e)
except Exception as e:
    print('Unexpected error', e)
finally:
    s.close()