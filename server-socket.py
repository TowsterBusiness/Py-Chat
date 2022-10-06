# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()

def connect():
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        return str(data)
        conn.sendall(data)

running = True
while running:
    print(connect())