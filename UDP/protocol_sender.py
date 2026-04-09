import socket

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


data = []
for i in range(1024*1024*10):
    data.append(i%256)
data = bytes(data)

packets = []

psz = 1280
delay = 1000
frame = 2

