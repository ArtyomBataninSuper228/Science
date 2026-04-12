import binascii
import queue
import socket
import threading
import time
import math
from collections import deque



class GlobalDataStream:
    def __init__(self):
        self.buffer = bytearray()
        self.lock = threading.Lock()

    def feed(self, data):
        with self.lock:
            self.buffer.extend(data)

    def extract_block(self, max_size=10 * 1024 * 1024):
        with self.lock:
            if not self.buffer:
                return None

            size_to_take = min(len(self.buffer), max_size)

            block_data = self.buffer[:size_to_take]

            del self.buffer[:size_to_take]

            return block_data

class Block_Builder():
    def __init__(self):
        self.buffer = GlobalDataStream()
        pass
    def get_block(self, blocksize):
        return self.buffer.extract_block(blocksize)

class Block_Getter:
    def __init__(self):
        self.buffer = GlobalDataStream()
    def process_block(self, block):
        self.buffer.feed(block)


'''
Global Packet ID:
0 - Send in inner chanel
1 - Ack in inner channel
2 - Packet in Outer channel
3 - ACK in Outer channel
4 - keepalive
'''

"""
Inner Packet ID:
0 - Handshake
1 - Start of block
2 - End of block
3 - User data
"""
'''
Packet Structure:
ID (Global id (0-9) + inner id (0-9)) ||| Connection ID ||| DATA ||| HESH 

Inner packet structure:
ID (Global id (0-9) + inner id (0-9)) ||| Connection ID  ||| packet_id ||| Num (0-256) ||| Total message len (0-256) ||| DATA ||| HESH 


#Inner connection ID:
#client: 0 2 4 6
#server: 1 3 5 7
'''


class Inner_Connection:
    def __init__(self, conn:Connection):
        self.buffer = GlobalDataStream()
        self.conn = conn
        self.packets = []
        self.waiting = []
        self.last_sended_packet_id = 0
    def put_packet(self, id, data):


        num = int.from_bytes(data[0:1], byteorder='big')
        length = int.from_bytes(data[1:2], byteorder='big')
        packet_id = int.from_bytes(data[2:6], byteorder='big')
        ack_pack = data[2:6]
        self.conn.add_packet(global_id= 1, inner_id = 0, data = ack_pack, is_left=True)
        data = data[6:]


        if num == 0 and len(self.packets) != length:
            self.packets = []
            for i in range(length):
                self.packets.append([])
        self.packets[num] = data
        if num == length - 1:
            message = bytes()
            for i in self.packets:
                message += i
            self.process_message(id, message)
    def process_message(self, id,  message):
        if id == 0:
            self.conn.is_started = True
            connection_id = int.from_bytes(message[:4], byteorder='big')
            self.conn.id = id
    def send_msg(self, id, msg):
        num_packets = math.ceil(len(msg)/self.conn.psz)
        packets = []
        for i in range(num_packets):
            packet = msg[i*self.conn.psz:(i+1)*self.conn.psz]
            self.send(id, packet, i, num_packets)

    def send(self, id, packet, message_num, total_num):
        self.last_sended_packet_id += 1
        self.last_sended_packet_id = self.last_sended_packet_id%(2**32)
        my_id = self.last_sended_packet_id
        self.waiting.append(self.last_sended_packet_id)
        packet = message_num.to_bytes(1, byteorder='big')+total_num.to_bytes(1, byteorder='big') + self.last_sended_packet_id.to_bytes(4, byteorder='big') + bytes(packet)

        while my_id in self.waiting:
            self.conn.add_packet(global_id= 0, inner_id = id, data = packet, is_left=True)
            time.sleep(self.conn.ping/1000)






class Connection():
    def __init__(self, ip, port, timeout = 1, buffersz = 1024 * 1024 * 10):
        self.buffer = GlobalDataStream()
        self.ip = ip
        self.port = port
        self.id = 0
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.timeout = timeout
        self.buffersz = buffersz
        self.psz = 1280
        self.delay = 1000
        self.ping = 50
        self.frame = 2
        self.loss = 0
        self.is_started = False
        self.time_of_start = time.time()
        self.send_block_number = 0
        self.recieve_block_number = 0
        self.is_alive = True
        self.recieved_packets = deque()
        self.packets_to_send = deque()
        self.input_buffer = GlobalDataStream()
        self.last_block_id = 0
        self.last_recieved_block_id = 0
        self.inner_channel = Inner_Connection(self)

    def add_packet(self, global_id, inner_id, data, is_left = False):
        if is_left:
            self.packets_to_send.appendleft((global_id * 10 + inner_id, self.id, data))
        else:
            self.packets_to_send.append((global_id * 10 + inner_id, self.id,  data))

    def send_packet(self, id, connection_id,  data):
        all_data = id.to_bytes(1, byteorder='big') + connection_id.to_bytes() + bytes(data)
        hesh = binascii.crc32(all_data)
        all_data = all_data + hesh.to_bytes(4, byteorder='big')
        self.socket.sendto(all_data, (self.ip, self.port))
    def packet_sender(self):
        t = time.time_ns()
        NSEC = 10 ** 9

        while self.is_alive:
            if len(self.packets_to_send) != 0:
                id_p, data = self.packets_to_send.get()
                t += (1 / self.delay) * NSEC
                self.send_packet(id_p, data)
                while time.time_ns() < t:
                    pass


            else:
                t += 2 * (1 / self.delay) * NSEC
                self.send_packet(40, 0, b'')
                while time.time_ns() < t:
                    pass
    def packet_reciever(self):
        while self.is_alive:
            self.socket.settimeout(1/10)
            try:
                data, addr = self.socket.recvfrom(1500)
            except socket.timeout:
                continue
            data_hash = data[-4:]
            data = data[:-4]
            if binascii.crc32(data).to_bytes(4, 'big') != data_hash:
                del data, addr
                continue
            id = int.from_bytes(data[:1], byteorder='big')
            data = data[1:]
            global_id = id//10
            inner_id = id%10
            if global_id in (0, 1): ## Inner Channel
                if global_id == 0:
                    self.inner_channel.put_packet(inner_id, data)
                if global_id == 1:
                    message_id = int.from_bytes(data[:4], byteorder='big')
                    if message_id in self.inner_channel.waiting:
                        self.inner_channel.waiting.remove(message_id)
            if global_id == 2:
                pass ### To construct block from packets
            if global_id == 3:
                pass ### To resend loss
            if global_id == 4:
                pass ### Keep alive









