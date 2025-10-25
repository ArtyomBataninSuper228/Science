import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
import pygame


def magnitude_to_db(magnitude, reference=1.0):
    """
    Переводит значение амплитуды в децибелы.

    Parameters:
    magnitude (float): значение амплитуды
    reference (float): опорное значение (по умолчанию 1.0)

    Returns:
    float: значение в децибелах
    """
    if magnitude <= 0:
        return -np.inf
    return 20 * np.log10(magnitude / reference)


def simple_fourier_analysis(file_path):
    try:
        # загрузка
        sample_rate, audio_data = wavfile.read(file_path)

        if len(audio_data.shape) > 1:
            audio_data = audio_data.mean(axis=1)

        n = len(audio_data)
        fft_result = fft(audio_data)
        frequencies = fftfreq(n, 1 / sample_rate)

        # Амплитуды для положительных частот
        magnitudes = np.abs(fft_result[:n // 2])
        frequencies_positive = frequencies[:n // 2]

        return frequencies_positive, magnitudes

    except:
        return None, None


def main():
    file_path = "shum.wav"
    frequencies, magnitudes = simple_fourier_analysis(file_path)
    screen_x = 1500
    screen_y = 700

    # понижаем длины списков в 1000 раз, чтобы было проще отобразить
    frequencies = frequencies[::1000]
    magnitudes = magnitudes[::1000]

    # переводим амплитуды в децибелы
    magnitudes = np.array([magnitude_to_db(mag) for mag in magnitudes])

    poloska = int(max(1, screen_x / len(frequencies)))
    screen_x = poloska * len(frequencies)
    k = max(magnitudes) / screen_y

    running = True
    pygame.init()
    screen = pygame.display.set_mode((screen_x, screen_y))
    clock = pygame.time.Clock()

    f1 = pygame.font.Font(None, 30)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        for i in range(len(frequencies)):
            height = magnitudes[i] / k
            pygame.draw.rect(screen, (255, 255, 255), (i * poloska, screen_y - height, poloska, height))
        try:
            mp = pygame.mouse.get_pos()
            index = round(mp[0] / poloska)

            text = f1.render(f"Амплитуда: {round(magnitudes[index], 2)} Дб", 1, (255, 255, 255))
            screen.blit(text, (mp[0], mp[1] + 20))
            text = f1.render(f"Частота: {round(frequencies[index], 2)} Гц", 1, (255, 255, 255))  # Измененная строка
            screen.blit(text, (mp[0], mp[1] + 40))
            pygame.draw.line(screen, (255, 255, 255), (mp[0], 0), (mp[0], screen_y))
        except:
            pass
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


main()