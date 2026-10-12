import usb.core
import sys

# Ищем дефолтное устройство (джампер EEPROM должен быть СНЯТ!)
dev = usb.core.find(idVendor=0x04B4, idProduct=0x8613)
if not dev:
    print("Чип не найден! Убедитесь, что сняли перемычку EEPROM.")
    sys.exit(1)

# 1. Останавливаем ядро 8051
dev.ctrl_transfer(0x40, 0xA0, 0xE600, 0, b'\x01')

# 2. Построчно парсим .ihx и отправляем байты в ОЗУ
print("Заливаем прошивку...")
for line in open('slave.ihx'):
    line = line.strip()
    if not line or line[0] != ':': continue
    b = bytes.fromhex(line[1:])
    length, addr, type_ = b[0], (b[1] << 8) | b[2], b[3]

    if type_ == 0:  # 0 = строка с данными
        dev.ctrl_transfer(0x40, 0xA0, addr, 0, b[4:4 + length])

# 3. Запускаем ядро 8051 с нашим кодом
dev.ctrl_transfer(0x40, 0xA0, 0xE600, 0, b'\x00')
print("Готово! На пине 36 (IFCLK) сейчас должно появиться 48 МГц.")