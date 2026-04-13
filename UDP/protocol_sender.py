from protocol_2_0 import *
import binascii

con = Connection('192.168.1.8', 55432, timeout=3)
f = open('C:\\Users\\artyo\\Pictures\\Обои\\DSC03714.jpg', mode = 'rb')
data = f.read()
data = data[:1280*255]
f.close()
con.send_inner(data)
recieved_data = con.recv_inner()
con.close()
print('Closed')
print(binascii.crc32(data), binascii.crc32(recieved_data))
