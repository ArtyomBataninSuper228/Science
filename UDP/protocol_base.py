import binascii
import queue
import socket
import threading
import time



class Datagram_Object:
    def __init__(self, soc, ip, port, timeout=1, buffersz=1024 * 1024 * 10):
        self.ip = ip
        self.port = port
        self.socket = soc#socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.timeout = timeout
        self.buffersz = buffersz
        self.psz = 1280
        self.delay = 1000
        self.frame = 2
        self.framesz = 1024*1024*10
        self.loss = 0
        self.time_of_start = time.time()
        self.send_block_number = 0
        self.recieve_block_number = 0
        self.is_alive = True

    def send_packet(self, id, block_id, data, to ,  num, ):
        '''

        Args:
            id: short Тип пакета (0 - handshake, 1 - keepalive, 2 - data, 3 - non-block data)
            block_id: short Номер блока
            data: bytearray Данные
            to: (str ip, int port)
            num: short Позиция стартового байта дынных пакета в блоке

        Returns: None

        '''
        all_data = id.to_bytes(1,byteorder='big')+block_id.to_bytes(4,byteorder='big')+num.to_bytes(4,byteorder='big')+bytes(data)
        hesh = binascii.crc32(all_data)
        all_data = all_data +hesh.to_bytes(4,byteorder='big')
        self.socket.sendto(all_data, to)




    def close(self):
        self.recieved_packets.clear()
        self.socket.close()
        self.is_alive = False

class Connection(Datagram_Object):
    def __init__(self,ip,port, timeout = 1, buffersz = 1024*1024*10):
        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        super().__init__(soc, ip, port, timeout, buffersz)
        self.recieved_packets  = queue.Queue()
        self.packets_to_send = []


        ### Trying_to_connect

        is_recieved = False
        for i in range(timeout*10):
            self.send_packet(0, 0,data = b'', to=(self.ip, self.port), num =0)
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
            id_p = int.from_bytes(data[:1], byteorder='big')
            block_id = int.from_bytes(data[1:5], byteorder='big')
            num = int.from_bytes(data[5:9], byteorder='big')
            data = data[9:]
            if id_p == 0:
                is_recieved = True
                break
        if not is_recieved:
            raise TimeoutError()
        sender_thread = threading.Thread(target=self.sender)
        sender_thread.start()

        reciver_thread = threading.Thread(target=self.reciever)
        reciver_thread.start()
        print('Succesful connected')
        #self.reciever()

    def reciever(self):
        """
        Эта функция принимает пакеты с сервера и складывает в буфер

        Исполнять в отдельном потоке!

        Returns: None

        """

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
            id_p = int.from_bytes(data[:1], byteorder='big')
            block_id = int.from_bytes(data[1:5], byteorder='big')
            num = int.from_bytes(data[5:9], byteorder='big')
            data = data[9:]
            self.recieved_packets.put((num, id_p, data))

    def sender(self):
        """
        Эта функция отправляет пакеты на сервер с соблюдением необходимых задержек

        Исполнять в отдельном потоке!

        Returns: None
        """

        number = 0
        t = time.time_ns()


        NSEC = 10 ** 9

        while self.is_alive:

            if self.packets_to_send:

                id_p, block_id, num, data = self.packets_to_send.popleft()


                t += (1 / self.delay) * NSEC
                self.send_packet(id_p, block_id, data, to=(self.ip, self.port), num=num)


                while time.time_ns() < t:
                    pass

            else:
                t += (1 / self.delay) * NSEC
                self.send_packet(3, 0, b'', to=(self.ip, self.port), num=number)

                number = (number + 1) % (2 ** 32)

                while time.time_ns() < t:
                    pass


    def close(self):
        self.is_alive = False
        time.sleep(1/5)
        self.socket.close()



class Server_Connection(Datagram_Object):
    def __init__(self,socket, ip,port,  raw_parametrs, timeout = 1, buffersz = 1024*1024*10):
        super().__init__(socket, ip, port, timeout, buffersz)
        self.recieved_packets  = queue.Queue()
        process_thread = threading.Thread(target = self.packet_process)
        process_thread.start()

    def packet_process(self):
        while self.is_alive:
            if not self.recieved_packets.empty():
                packet = self.recieved_packets.get()
                if packet[0] == 0:
                    self.send_packet(0, 0, b'', (self.ip, self.port), 0)  ### АСК
                if packet[0] == 1:
                    self.send_packet(1, 0, b'', (self.ip, self.port), 0)  ### АСК



    def sender(self):
        """
        Эта функция отправляет пакеты на сервер с соблюдением необходимых задержек

        Исполнять в отдельном потоке!

        Returns: None
        """

        number = 0
        t = time.time_ns()

        NSEC = 10 ** 9

        while self.is_alive:

            if self.packets_to_send:

                id_p, block_id, num, data = self.packets_to_send.popleft()

                t += (1 / self.delay) * NSEC
                self.send_packet(id_p, block_id, data, to=(self.ip, self.port), num=num)

                while time.time_ns() < t:
                    pass

            else:
                t += (1 / self.delay) * NSEC
                self.send_packet(3, 0, b'', to=(self.ip, self.port), num=number)

                number = (number + 1) % (2 ** 32)

                while time.time_ns() < t:
                    pass





class Server (Datagram_Object):
    def __init__(self,ip,port, handler, timeout = 1, buffersz = 1024*1024*10, ):
        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        super().__init__(soc, ip, port, timeout, buffersz)
        self.socket.bind((self.ip, self.port))
        self.socket.settimeout(timeout)
        self.connections = {}
        self.handler = handler
        reciever_thread = threading.Thread(target=self.reciever)
        reciever_thread.start()
    def reciever(self):
        while self.is_alive:
            try:
                data, addr = self.socket.recvfrom(1500)
            except socket.timeout:
                continue
            data_hash = data[-4:]
            data = data[:-4]
            if binascii.crc32(data).to_bytes(4, 'big') != data_hash:
                del data, addr
                continue
            id_p = int.from_bytes(data[:1],byteorder='big')
            block_id = int.from_bytes(data[1:5],byteorder='big')
            num = int.from_bytes(data[5:9],byteorder='big')
            data = data[9:]
            if addr in self.connections:
                self.connections[addr].recieved_packets.put((id_p, block_id, num, data))
            else:
                if id_p !=0:
                    continue
                print('Connected from', addr)
                #self.send_packet(0, 0, b'', addr, 0)### АСК
                New_connection = Server_Connection(self.socket, addr[0], addr[1], data, self.timeout, self.buffersz)
                self.connections[addr] = New_connection
                handler_thread = threading.Thread(target=self.handler, args=(New_connection,))
                handler_thread.start()









