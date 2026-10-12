import time
import matplotlib.pyplot as plt
import usb.core
import usb.util
import sys

# 1. Находим плату (эквивалент выбора COM-порта)
dev = usb.core.find(idVendor=0x04B4, idProduct=0x1004)
if dev is None:
    print("Плата не найдена.")
    sys.exit()





# 2. Обязательное действие для USB: захватываем управление устройством

dev.reset()
dev.set_configuration()
'''
  Производитель USB‑устройства:	0x04b4
  Идентификатор USB‑устройства:	0x8613

'''
dev.set_interface_altsetting(0,0)
print("--- Список доступных Эндпоинтов ---")
cfg = dev.get_active_configuration()
for intf in cfg:
        for ep in intf:
            addr = ep.bEndpointAddress
            direction = "IN (Плата -> ПК)" if (addr & 0x80) else "OUT (ПК -> Плата)"
            print(f"Адрес: {hex(addr)} | Направление: {direction} | Тип: {ep.bmAttributes & 0x03}")





# Адреса труб (эндпоинтов), настроенные в прошивке bulkloop
EP_OUT = 0x02  # Труба для отправки из компьютера в плату
EP_IN = 0x86  # Труба для чтения из платы в компьютер

# 3. Формируем наш массив байтов
my_data = b"Hello, Radar!"
a = []
BIT_REVERSE_TABLE = bytes(
    int(f"{i:08b}"[::-1], 2) for i in range(256)
)

def get_data(length):
    try:
        # Пишем данные в EP2 (ПК -> Плата)
        #dev.write(EP_OUT, bytes(length))

        # Читаем данные из EP6 (Плата -> ПК)
        for i in range(100):
            dev.write(EP_OUT, b"0"*512)
        # 512 - это максимальный размер буфера, timeout в миллисекундах
        #response = dev.read(EP_IN, 2, timeout=1000)
        res = []
        # Превращаем полученный массив чисел обратно в строку для красоты
        #for byte in response:
        #    res.append(int(byte))#int(BIT_REVERSE_TABLE[int(byte)]))
        #return res
        #print(f"Получили обратно: {bytes(response)}")

    except usb.core.USBError as e:
        print(f"Ошибка обмена по USB: {e}")
        return [0]


for i in range(10):
    dev.write(EP_OUT, b"0"*512)
time.sleep(10000)
data = [0]
while max(data) <= 3:
    data = get_data(512)
plt.plot(data)
print(bin(max(data)))
plt.show()