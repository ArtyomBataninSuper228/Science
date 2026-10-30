import time

import usb.core
import usb.util
import sys

EP_IN = 0x86

#dev = usb.core.find(idVendor=0x04B4, idProduct=0x1004)
dev = usb.core.find(idVendor=0x04B4, idProduct=0x8613)
#VID = 0x04B4
# PID = 0x8613
if dev is None:
    sys.exit("Устройство не найдено")

dev.set_configuration(1)

cfg = dev.get_active_configuration()
intf = None
ep_in = None

# Перебираем все alternate settings для интерфейса 0
for alt in range(3):
    try:
        current_intf = usb.util.find_descriptor(cfg, bInterfaceNumber=0, bAlternateSetting=alt)
        # Ищем точку 0x86 с типом Bulk (bmAttributes & 0x03 == 2)
        match_ep = usb.util.find_descriptor(
            current_intf,
            custom_match=lambda e: e.bEndpointAddress == EP_IN and (e.bmAttributes & 0x03) == 2
        )
        if match_ep is not None:
            intf = current_intf
            ep_in = match_ep
            # Передаем параметры строго позиционно: (интерфейс, альт-сеттинг)
            dev.set_interface_altsetting(0, alt)
            print(f"Успешно активирован Alt Setting {alt}, где 0x86 — это Bulk-канал!")
            break
    except usb.core.USBError:
        continue

if ep_in is None:
    sys.exit("Критическая ошибка: в дескрипторах устройства вообще нет Bulk-точки 0x86!")

# Захватываем интерфейс
try:
    usb.util.claim_interface(dev, 0)
except usb.core.USBError:
    pass

# Выполняем чтение
total = 0
p = 0
m = []
try:
    while 1:
        t1 = time.time()


        for i in range(10000):
            # print("Ожидание данных от ПЛИС...")
            data = ep_in.read(512, timeout=2000)
            total += len(data)
            p += len(data) >52
            if len(data) not in m:
                m.append(len(data))
            if(len(data) != 0):
                pass
                #print(data, len(data))

            # print(f"Успешно прочитано {len(data)} байт!")
            # print("Данные:", list(data[:10]))
        t2 = time.time()
        print(total / (t2 - t1) / 1000000, total /10000, p, sorted(m))
        total = 0
        p = 0
        m = []

except usb.core.USBError as e:
    print(f"Статус чтения: {e}")
finally:
    try:
        usb.util.release_interface(dev, 0)
    except:
        pass
