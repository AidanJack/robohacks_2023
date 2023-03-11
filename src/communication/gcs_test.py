import socket
from time import sleep

host = "192.168.4.1"
port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
s.connect((host, port))
angles = [25, 40, -15, 80, -30, 10, 70, 0, -60, 0, -90]

for angle in angles:
    new_angle = 90+angle
    if new_angle >= 0 and new_angle <= 180:
        print(f'Sent: {new_angle}')
        s.sendall(bytes(str(new_angle), 'utf-8'))
        sleep(1)
s.close()
