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


'''


class Inner_Client_Connection:
    def __init__(self, conn:Connection):
        self.buffer = GlobalDataStream()
        self.conn = conn
        self.packets = []
        self.waiting = []
        self.last_sended_packet_id = 0
        self.last_recieved_id = -1
    def put_packet(self, id, data):



        num = int.from_bytes(data[0:1], byteorder='big')
        length = int.from_bytes(data[1:2], byteorder='big')
        packet_id = int.from_bytes(data[2:6], byteorder='big')


        ack_pack = data[2:6]

        self.conn.add_packet(global_id= 1, inner_id = 0, data = ack_pack, is_left=True)
        if packet_id <= self.last_recieved_id:
            return
        data = data[6:]
        self.last_recieved_id = max(self.last_recieved_id, packet_id)
        if self.last_recieved_id == 2**32 -1 :
            self.last_recieved_id = -1


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

        for i in range(int(self.conn.timeout/self.conn.ping*1000)):
            self.conn.add_packet(global_id= 0, inner_id = id, data = packet, is_left=True)
            time.sleep(self.conn.ping/1000)


ICC = Inner_Client_Connection



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
        self.inner_channel = ICC(self)
        self.inner_channel.send_msg(0, b'')

    def add_packet(self, global_id, inner_id, data, is_left = False):
        if is_left:
            self.packets_to_send.appendleft((global_id * 10 + inner_id, data))
        else:
            self.packets_to_send.append((global_id * 10 + inner_id,  data))

    def send_packet(self, id,  data):
        all_data = id.to_bytes(1, byteorder='big') + self.id.to_bytes(4, byteorder='big') + bytes(data)
        hesh = binascii.crc32(all_data)
        all_data = all_data + hesh.to_bytes(4, byteorder='big')
        self.socket.sendto(all_data, (self.ip, self.port))
    def packet_sender(self):
        t = time.time_ns()
        NSEC = 10 ** 9

        while self.is_alive:
            if len(self.packets_to_send) != 0:
                id_p, data = self.packets_to_send.popleft()
                t += (1 / self.delay) * NSEC
                self.send_packet(id_p, data)
                while time.time_ns() < t:
                    pass


            else:
                t += 2 * (1 / self.delay) * NSEC
                self.send_packet(40, b'')
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




'''
Packet Structure:
ID (Global id (0-9) + inner id (0-9)) ||| DATA ||| HESH 

Inner packet structure:
ID (Global id (0-9) + inner id (0-9))  ||| packet_id ||| Num (0-256) ||| Total message len (0-256) ||| DATA ||| HESH 


'''


class Inner_Server_Connection:
    def __init__(self, conn:Server_Connection):
        self.buffer = GlobalDataStream()
        self.conn = conn
        self.packets = []
        self.waiting = []
        self.last_sended_packet_id = 0
        self.last_recieved_id = -1
    def put_packet(self, id, data):



        num = int.from_bytes(data[0:1], byteorder='big')
        length = int.from_bytes(data[1:2], byteorder='big')
        packet_id = int.from_bytes(data[2:6], byteorder='big')


        ack_pack = data[2:6]

        self.conn.add_packet(global_id= 1, inner_id = 0, data = ack_pack, is_left=True)
        if packet_id <= self.last_recieved_id:
            return
        data = data[6:]
        self.last_recieved_id = max(self.last_recieved_id, packet_id)
        if self.last_recieved_id == 2**32 -1 :
            self.last_recieved_id = -1


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
            self.conn.add_packet(global_id= 0, inner_id = 0, data = self.id.to_bytes(4, byteorder='big'), is_left=True)
            #todo
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

        for i in range(int(self.conn.timeout / self.conn.ping * 1000)):
            self.conn.add_packet(global_id=0, inner_id=id, data=packet, is_left=True)
            time.sleep(self.conn.ping / 1000)

ISC = Inner_Server_Connection

class Server_Connection():
    def __init__(self,socket, id,  ip,port,  raw_parametrs, server:Server, timeout = 1, buffersz = 1024*1024*10):
        self.socket = socket
        self.ip = ip
        self.id = id
        self.psz = 1280
        self.delay = 1000
        self.ping = 50
        self.frame = 2
        self.loss = 0
        self.port = port
        self.raw_parametrs = raw_parametrs
        self.server = server
        self.timeout = timeout
        self.buffersz = buffersz
        self.recieved_packets = queue.Queue()
        self.packets_to_send = deque()
        process_thread = threading.Thread(target = self.packet_process)
        process_thread.start()
        self.server = server
        self.inner_channel = ISC(self)

    def packet_process(self):
        last_con = time.time()
        while self.is_alive:
            if not self.recieved_packets.empty():
                while not self.recieved_packets.empty():
                    id, data, addr = self.recieved_packets.get()
                    if addr != (self.ip, self.port):
                        self.server.registered_addreses.remove((self.ip, self.port))
                        self.server.registered_addreses.append(addr)
                        self.ip = addr[0]
                        self.port = addr[1]

                    global_id = id // 10
                    inner_id = id % 10
                    if global_id in (0, 1):  ## Inner Channel
                        if global_id == 0:
                            self.inner_channel.put_packet(inner_id, data)
                        if global_id == 1:
                            message_id = int.from_bytes(data[:4], byteorder='big')
                            if message_id in self.inner_channel.waiting:
                                self.inner_channel.waiting.remove(message_id)
                    if global_id == 2:
                        pass  ### To construct block from packets
                    if global_id == 3:
                        pass  ### To resend loss
                    if global_id == 4:
                        pass  ### Keep alive


                last_con = time.time()
            time.sleep(1/100000)
            if time.time() - last_con > self.timeout:
                self.close()
                break
    def add_packet(self, global_id, inner_id, data, is_left = False):
        if is_left:
            self.packets_to_send.appendleft((global_id * 10 + inner_id, data))
        else:
            self.packets_to_send.append((global_id * 10 + inner_id,  data))
    def send_packet(self, id,  data):
        all_data = id.to_bytes(1, byteorder='big')  + bytes(data)
        hesh = binascii.crc32(all_data)
        all_data = all_data + hesh.to_bytes(4, byteorder='big')
        self.socket.sendto(all_data, (self.ip, self.port))
    def close(self):
        self.is_alive = False
        self.server.connections.remove(self)

    def packet_sender(self):
        t = time.time_ns()
        NSEC = 10 ** 9

        while self.is_alive:
            if len(self.packets_to_send) != 0:
                id_p, data = self.packets_to_send.popleft()
                t += (1 / self.delay) * NSEC
                self.send_packet(id_p,  data)
                while time.time_ns() < t:
                    pass


            else:
                t += 2 * (1 / self.delay) * NSEC
                self.send_packet(40,  b'')
                while time.time_ns() < t:
                    pass




class Server :
    def __init__(self,ip,port, handler, timeout = 1, buffersz = 1024*1024*10, ):
        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        soc.settimeout(None)
        self.ip = ip
        self.port = port
        self.handler = handler
        self.timeout = timeout
        self.buffersz = buffersz
        self.socket.bind((self.ip, self.port))
        self.socket.settimeout(timeout)
        self.connections = {}
        self.handler = handler
        reciever_thread = threading.Thread(target=self.reciever)
        reciever_thread.start()
        self.registered_addreses = []
        self.last_id = 0

    def packet_reciever(self):
        while self.is_alive:
            self.socket.settimeout(1 / 10)
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
            connection_id = int.from_bytes(data[1:5], byteorder='big')
            data = data[5:]
            if id == 0 and connection_id == 0 and addr not in self.registered_addreses :
                self.last_id += 1
                ip = addr[0]
                port = addr[1]
                new_connection = Server_Connection(self.socket, self.last_id, ip, port, raw_parametrs= data, server=self, timeout= self.timeout, buffersz= self.buffersz)
                self.connections[id] = new_connection
                self.registered_addreses.append(addr)
                continue
            try:
                self.connections[connection_id].recieved_packets.put((id, data, addr))
            except :
                pass






