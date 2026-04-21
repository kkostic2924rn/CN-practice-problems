import socket

def encoding(data: bytes):
    K = 55
    enc_data = list()
    for byte in data:
        enc_data.append((byte + K) % 256)
    return bytes(enc_data)

def decoding(data: bytes):
    K = 55
    enc_data = list()
    for byte in data:
        enc_data.append((byte - K) % 256)
    return bytes(enc_data)

def send_message(s: socket.socket, message: str):
    print('<<', message)
    data = message.encode()
    data = encoding(data)
    s.sendall(data)

def recieve_message(s: socket.socket) -> str:
    data = s.recv(1024)
    data = decoding(data)
    txt = data.decode()
    print('>>', txt)
    return txt