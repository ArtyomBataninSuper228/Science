import serial
from matplotlib import pyplot as plt
import time


arduino = serial.Serial("/dev/cu.usbmodem101", 2000000)
time.sleep(1)
#arduino.write(b"start")
#for i in range(1000):
#    arduino.write(b"start")
#print("writed")
#print(arduino.readall())
#print(arduino.readall())
a = arduino.readline()
print(a)
while a != b"start\r\n":
    print(a)
    a = arduino.readline()
data = []
for i in range(800):
    print(i)
    data.append(int(arduino.readline()))
plt.plot(data)
plt.show()