import sounddevice as sd
import numpy as np
import threading
import time
from matplotlib import pyplot as plt
import json
fs = 88100
fs_record = 360000
duration = 0.01
duration_record = 1
freq = 10000

# Создаем сигнал
t = np.linspace(0, duration, int(fs * duration), False)
signal = np.sin(2 * np.pi * freq * t)

# Флаг остановки
stop_flag = threading.Event()
recorded = np.zeros(int(fs_record*duration_record*2))
k = 0
def record_audio():
    global recorded, k
    """Функция записи в отдельном потоке"""
    print("Запись начата")

    recorded_data = []

    def callback(indata, frames, time_info, status):
        if status:
            print(f"Статус записи: {status}")
        recorded_data.append(indata.copy())
        if stop_flag.is_set():
            raise sd.CallbackStop()

    with sd.InputStream(samplerate=fs_record,
                        channels=1,
                        dtype='float32',
                        callback=callback):
        while not stop_flag.is_set():
            sd.sleep(100)

    if recorded_data:
        for m in recorded_data:
            for i in m:
                recorded[k] = i[0]
                k += 1
        #return np.vstack(recorded_data)
    #return np.array([])


def play_audio():
    """Воспроизведение"""
    print("Воспроизведение начато")
    sd.play(signal, fs)
    #sd.wait()
    time.sleep(duration_record-duration)
    stop_flag.set()


# Запускаем потоки
record_thread = threading.Thread(target=record_audio, daemon=True)
play_thread = threading.Thread(target=play_audio, daemon=True)

record_thread.start()
time.sleep(0.1)  # Задержка для инициализации записи
play_thread.start()

# Ждем завершения
play_thread.join()
record_thread.join()

print("Готово")
print(k)

js = {
    "f": freq,
    "dt":1/fs_record,
    "desc":"Наушники",
    "tos":0,
    "mA":recorded.tolist(),
    "mB":recorded.tolist(),
}
file = open("Наушники.json", "w")
json.dump(js, file)
file.close()



