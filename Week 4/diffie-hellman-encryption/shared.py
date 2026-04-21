import socket

def recieve_message(s: socket.socket, key: int = None) -> str:
    data = s.recv(1024)
    txt = data.decode()
    print('<< recieved:', txt)
    return txt

def send_message(s: socket.socket, message: str, key: int = None):
    print('>> send:', message)
    data = message.encode()
    s.sendall(data)