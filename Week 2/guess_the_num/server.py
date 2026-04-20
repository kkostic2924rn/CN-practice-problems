import socket
import threading
import random

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 2026))
s.listen(10)

ran = random.randint(1, 20)
print('Random number is: ', ran)
winner = None

def recieve_message(s: socket.socket) -> str:
    message = s.recv(1024).decode()
    print(f'Client [{s.getpeername()}] >', message)
    return message

def recieve_message_int(s: socket.socket) -> str:
    txt = recieve_message(s)
    try:
        x = int(txt)
        return x
    except:
        print('Wrong number format')
        return None

def send_message(s:socket.socket, txt: str):
    s.sendall(txt.encode())

def client_handle(c:socket.socket, addr:tuple, client_num: int):
    global ran, winner
    client_id = f'{addr[0]}:{addr[1]}:{client_num}'
    print('Connected', client_id)
    try:
        while True:
            num = recieve_message_int(c)
            if winner is not None:
                send_message(c, f'Winner is {winner}')
                break
            elif num is None:
                send_message(c, 'Wrong number format')
            elif ran == num:
                send_message(c, 'Correct!')
                winner = client_id
                break
            elif ran < num:
                send_message(c, 'Smaller')
            else:
                send_message(c, 'Bigger')
    except (OSError, socket.error) as e:
        print('Greska', e)
    except Exception as e:
        print('Neocekivana greska', e)
    finally:
        c.close()

client_num = 1
while True:
    c, addr = s.accept()
    t = threading.Thread(target=client_handle, args=(c, addr, client_num))
    t.start()
    client_num += 1