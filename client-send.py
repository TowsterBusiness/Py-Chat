# echo-client.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def send(text):
    global HOST
    global PORT
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(text)
        data = s.recv(1024)

    print(f"Received {data!r}")

running = True
while running:
    message = input("chat: ")
    if message is "STOP":
        break
    else:
        send(bytes(message, 'utf-8'))
