import usb.core

def load_firmware(filename):
    VID = 0x04B4
    PID = 0x8613

    dev = usb.core.find(idVendor=VID, idProduct=PID)#Поиск устройства
    if dev is None:
        raise ValueError("Устройство FX2LP не найдено. Проверьте подключение.")

    print("Остановка процессора FX2LP...")
    # Вводим процессор в состояние сброса (reset = 1)
    dev.ctrl_transfer(0x40, 0xA0, 0xE600, 0, b'\x01')

    print("Парсинг и загрузка .ihx прошивки...")
    # Открываем файл как обычный текст ("r"), а не бинарник ("rb")
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            # Пропускаем пустые строки и строки, не начинающиеся с двоеточия
            if not line or line[0] != ':':
                continue

            # Превращаем HEX-строку в массив байтов (без учета двоеточия)
            b = bytes.fromhex(line[1:])

            # Извлекаем длину данных, адрес назначения и тип записи
            length = b[0]
            addr = (b[1] << 8) | b[2]
            record_type = b[3]

            # Тип 0 означает, что в строке лежат полезные данные прошивки
            if record_type == 0:
                data_chunk = b[4: 4 + length]
                dev.ctrl_transfer(
                    bmRequestType=0x40,
                    bRequest=0xA0,
                    wValue=addr,
                    wIndex=0x0000,
                    data_or_wLength=data_chunk
                )
    print("Запуск процессора...")
    # Снимаем сброс (reset = 0) — код начинает выполняться
    dev.ctrl_transfer(0x40, 0xA0, 0xE600, 0, b'\x00')

if __name__ == "__main__":
    load_firmware("fifo2.ihx")