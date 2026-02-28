import numpy as np
import sounddevice as sd
import pyfftw
from dearpygui.dearpygui import mvDragInt
from pyparsing import makeXMLTags

from integral import *
import time
from matplotlib import pyplot as plt

# Параметры
SAMPLE_RATE = 44100                # Гц
SYMBOL_DURATION = 1              # длительность символа (сек)
SAMPLES = int(SAMPLE_RATE * SYMBOL_DURATION*0.5)  # количество отсчётов на символ
smpls = int(SAMPLE_RATE * 0.1)

def median(M):
    return sum(M)/len(M)

def dispersion(M):
    dispersion = 0
    med = median(M)
    for i in range(0, len(M)):
        dispersion += (M[i] - med)**2
    return dispersion/len(M)

# Частоты для битов 0..7 (Гц)
FREQS = [400, 800, 1200, 1600, 2000, 2400, 2800, 3200]

# Порог обнаружения (подбери экспериментально)
THRESHOLD = 0.01

# --- НАСТРОЙКА PYFFTW (делается один раз) ---
# Создаём выровненные массивы для входных и выходных данных
# Тип complex128, так как FFT работает с комплексными числами
a = pyfftw.empty_aligned(SAMPLES, dtype='complex128')
b = pyfftw.empty_aligned(SAMPLES, dtype='complex128')
k = pyfftw.empty_aligned(smpls, dtype='complex128')
v = pyfftw.empty_aligned(smpls, dtype='complex128')
# Создаём «мудрый» план с использованием всех ядер процессора
# flags='FFTW_MEASURE' – потратить немного времени на поиск оптимального алгоритма
# threads – число потоков (можно поставить 0, чтобы использовать все доступные)
fft_obj2 = pyfftw.FFTW(k, v, axes=(-1,), direction='FFTW_FORWARD',
                       flags=('FFTW_MEASURE',), threads=0)
fft_obj = pyfftw.FFTW(a, b, axes=(-1,), direction='FFTW_FORWARD',
                       flags=('FFTW_MEASURE',), threads=0)

print("План FFT создан. Начинаем прослушивание...")

# --- НАСТРОЙКА ЗАХВАТА ЗВУКА (sounddevice) ---
# Открываем входной поток с нужными параметрами
# Блокирующий режим: будем читать блоками через stream.read()
stream = sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype='float32')
stream.start()
previous = 100
ok = 0
try:
    while ok <  2:
        t0 = time.time()
        data, overflowed = stream.read(smpls)

        # Преобразуем во float64 (требуется для pyfftw) и делаем плоским
        audio_chunk = data.flatten().astype(np.float64)

        # Копируем данные в массив a (входной для FFT)
        k[:] = audio_chunk

        # Выполняем БПФ (результат в b)
        fft_data = fft_obj2()

        # Берём амплитуды положительных частот (до SAMPLES//2)

        magnitude = np.abs(v[:smpls // 2])
        min_idx = int((min(FREQS) - 400) * smpls / SAMPLE_RATE)
        max_idx = int((max(FREQS) + 400) * smpls / SAMPLE_RATE)
        #median = np.median(magnitude[min_idx:max_idx])
        id  = int((440) * smpls / SAMPLE_RATE)
        if magnitude[id]-previous > 10:
            ts = t0
            ok += 1
        previous = magnitude[id]
        if ok == 1:
            ok = 2
    time.sleep(1-(time.time() - ts))
    num = 0
    ts = time.time()
    while True:
        # Читаем один блок данных (ровно SAMPLES отсчётов)
        #time.sleep(SYMBOL_DURATION * 0.2)
        data, overflowed = stream.read(SAMPLES)
        # Преобразуем во float64 (требуется для pyfftw) и делаем плоским
        audio_chunk = data.flatten().astype(np.float64)
        # Копируем данные в массив a (входной для FFT)
        a[:] = audio_chunk
        # Выполняем БПФ (результат в b)
        fft_data = fft_obj()
        # Берём амплитуды положительных частот (до SAMPLES//2)
        magnitude = np.abs(b[:SAMPLES//2])
        min_idx = int((min(FREQS)-400) * SAMPLES / SAMPLE_RATE)
        max_idx = int((max(FREQS) + 400) * SAMPLES / SAMPLE_RATE)
        m = []
        for bit, freq in enumerate(FREQS):
            # Индекс ближайшего бина к нашей частоте
            idx = int(freq * SAMPLES / SAMPLE_RATE)
            m.append(magnitude[idx])
        #print(dispersion(m))
        detected_byte = 0
        res = []
        res.append(median(m))
        for bit, freq in enumerate(FREQS):
            # Индекс ближайшего бина к нашей частоте
            idx = int(freq * SAMPLES / SAMPLE_RATE)
            res.append(float(magnitude[idx]))
            if idx < len(magnitude) and magnitude[idx] > 1000:
                detected_byte += 2**bit
        # Если хоть один бит обнаружен – выводим
        #if detected_byte != 0:
        print(f"Принят байт: {detected_byte:08b} ({detected_byte})", time.time(), res)
        num += 1
        time.sleep(SYMBOL_DURATION-(time.time() - ts - num*SYMBOL_DURATION))

except KeyboardInterrupt:
    print("\nОстановлено пользователем")
finally:
    stream.stop()
    stream.close()