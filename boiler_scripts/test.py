import socket, time, sys

ip = "10.10.3.39"
port = 1337
timeout = 5
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
print(s.recv(1024))
s.send(b'OVERFLOW1 test')
print(s.recv(1024))

