import socket

def encryption(data: bytes, key: int) -> bytes:
    out = bytearray()
    for byte in data:
        out.append(byte ^ key)
    return bytes(out)

def decryption(data: bytes, key: int) -> bytes:
    return encryption(data, key)
    #because xor is symetric, so doing it 2 times gives us the original answer

def recieve_message(s: socket.socket, key: int = None) -> str:
    data = s.recv(1024)
    if key is not None:
        data = decryption(data, key)
    txt = data.decode()
    print('<< recieved:', txt)
    return txt

def send_message(s: socket.socket, message: str, key: int = None):
    print('>> send:', message)
    data = message.encode()
    if key is not None:
        data = encryption(data, key)
    s.sendall(data)