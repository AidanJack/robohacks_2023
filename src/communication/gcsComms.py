import socket
import time as t
# from robohacks_2023.src.vision.color_detection.py import objectDetection

auv_ip = "192.168.4.1"
auv_port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((auv_ip, auv_port))

# string_recv = ""

def estimatePos(gx, gy, gz, ax, ay, az):
    pass

def stringDataConverter(String):
    pass

def objectDetection(image):
    pass

while(True):
    # sock.send(bytes(input("Message to Send") + "\n", "utf-8"))
    string_recv = sock.recv(8)
    if len(string_recv) > 0:
        # string_recv = string_recv.decode("utf-8")
        print(string_recv)
        # gx, gy, gz, ax, ay, az, image = stringDataConverter(string_recv)
        # posx, posy, posz = estimatePos(gx, gy, gz, ax, ay, az)
        # obs, coral = objectDetection(image)



        
    t.sleep(0.5)
