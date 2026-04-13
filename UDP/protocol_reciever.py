from protocol_2_0 import *

class Zero_Handler:
    def __init__(self, connection):
        self.is_alive = False
        time.sleep(1)
        connection.is_alive = 0

server = Server('192.168.1.8', 55432, Zero_Handler)