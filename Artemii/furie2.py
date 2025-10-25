import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq, ifft
import pygame, time


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


def db_to_magnitude(db_value, reference=1.0):
    """
    Переводит значение из децибелов обратно в амплитуду.

    Parameters:
    db_value (float): значение в децибелах
    reference (float): опорное значение (по умолчанию 1.0)

    Returns:
    float: значение амплитуды
    """
    return reference * 10 ** (db_value / 20)


def smooth_magnitudes(magnitudes, window_size=1001, iterations=1):
    """
    Сглаживание амплитуд с большим окном.

    Parameters:
    magnitudes (np.array): массив амплитуд
    window_size (int): размер окна сглаживания
    iterations (int): количество итераций сглаживания

    Returns:
    np.array: сглаженные амплитуды
    """
    smoothed = magnitudes.copy()
    half_window = window_size // 2

    for i in range(101):
        print(f"{i}%")
        for _ in range(iterations):
            temp = smoothed.copy()

            # Быстрое сглаживание с использованием векторных операций
            for i in range(len(smoothed)):
                start_idx = max(0, i - half_window)
                end_idx = min(len(smoothed), i + half_window + 1)
                temp[i] = np.mean(smoothed[start_idx:end_idx])

            smoothed = temp

    return smoothed

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

        return frequencies_positive, magnitudes, fft_result, sample_rate, audio_data

    except Exception as e:
        print(f"Ошибка при анализе файла: {e}")
        return None, None, None, None, None


def create_modified_audio(original_fft, original_magnitudes, smoothed_magnitudes, n):
    """
    Создает модифицированный FFT сигнал с уменьшенными амплитудами.

    Parameters:
    original_fft (np.array): исходный FFT сигнал
    original_magnitudes (np.array): исходные амплитуды
    smoothed_magnitudes (np.array): сглаженные амплитуды
    n (int): длина сигнала

    Returns:
    np.array: модифицированный FFT сигнал
    """
    modified_fft = original_fft.copy()

    # Для положительных частот
    for i in range(n // 2):
        if original_magnitudes[i] > 0:
            # Вычисляем коэффициент уменьшения
            reduction_factor = max(0, (original_magnitudes[i] - smoothed_magnitudes[i]) / original_magnitudes[i])
            # Применяем уменьшение к комплексному числу
            modified_fft[i] *= reduction_factor

    # Для отрицательных частот (симметрично)
    for i in range(n // 2, n):
        j = n - i  # симметричный индекс для положительных частот
        if j < len(original_magnitudes) and original_magnitudes[j] > 0:
            reduction_factor = max(0, (original_magnitudes[j] - smoothed_magnitudes[j]) / original_magnitudes[j])
            modified_fft[i] *= reduction_factor

    return modified_fft


def main():
    file_path = "s_shumom2.wav"
    frequencies, magnitudes, fft_result, sample_rate, audio_data = simple_fourier_analysis(file_path)

    if frequencies is None:
        print("Не удалось загрузить или проанализировать аудиофайл")
        return

    screen_x = 1500
    screen_y = 700

    # Создаем копии для отображения (прореженные)
    display_frequencies = frequencies[::1000]
    display_magnitudes = magnitudes[::1000]

    # Сглаживаем амплитуды (на полном наборе данных)
    print("Сглаживание амплитуд...")
    smoothed_magnitudes = smooth_magnitudes(magnitudes)

    # Создаем модифицированный аудиосигнал
    print("Создание модифицированного аудио...")
    modified_fft = create_modified_audio(fft_result, magnitudes, smoothed_magnitudes, len(audio_data))
    modified_audio = np.real(ifft(modified_fft))

    # Нормализуем и преобразуем к исходному типу данных
    modified_audio = np.int16(modified_audio / np.max(np.abs(modified_audio)) * 32767)

    # Сохраняем новый WAV-файл
    output_path = "s_shumom_modified.wav"
    wavfile.write(output_path, sample_rate, modified_audio)
    print(f"Модифицированный аудиофайл сохранен как: {output_path}")

    # Подготовка данных для отображения
    display_smoothed = smoothed_magnitudes[::1000]

    # Переводим амплитуды в децибелы для отображения
    display_magnitudes_db = np.array([magnitude_to_db(mag) for mag in display_magnitudes])
    display_smoothed_db = np.array([magnitude_to_db(mag) for mag in display_smoothed])

    poloska = int(max(1, screen_x / len(display_frequencies)))
    screen_x = poloska * len(display_frequencies)
    k = max(max(display_magnitudes_db), max(display_smoothed_db)) / screen_y

    running = True
    pygame.init()
    screen = pygame.display.set_mode((screen_x, screen_y))
    clock = pygame.time.Clock()

    f1 = pygame.font.Font(None, 30)

    # Переменная для переключения между отображением исходных и сглаженных данных
    show_smoothed = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    show_smoothed = not show_smoothed

        screen.fill((0, 0, 0))

        # Отображаем либо исходные, либо сглаженные данные
        current_magnitudes = display_smoothed_db if show_smoothed else display_magnitudes_db
        color = (0, 255, 0) if show_smoothed else (255, 255, 255)

        for i in range(len(display_frequencies)):
            height = current_magnitudes[i] / k
            pygame.draw.rect(screen, color, (i * poloska, screen_y - height, poloska, height))

        try:
            mp = pygame.mouse.get_pos()
            index = round(mp[0] / poloska)
            if 0 <= index < len(display_frequencies):
                text = f1.render(f"Амплитуда: {round(current_magnitudes[index], 2)} Дб", 1, (255, 255, 255))
                screen.blit(text, (mp[0], mp[1] + 20))
                text = f1.render(f"Частота: {round(display_frequencies[index], 2)} Гц", 1, (255, 255, 255))
                screen.blit(text, (mp[0], mp[1] + 40))

                # Показываем, что отображается
                mode_text = "Сглаженные амплитуды" if show_smoothed else "Исходные амплитуды"
                text = f1.render(f"Режим: {mode_text} (ПРОБЕЛ для переключения)", 1, (255, 255, 255))
                screen.blit(text, (10, 10))

                pygame.draw.line(screen, (255, 255, 255), (mp[0], 0), (mp[0], screen_y))
        except:
            pass

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    start_time = time.time()

    main()

    # Конец отсчёта времени
    end_time = time.time()
    # Вычисление времени выполнения
    execution_time = end_time - start_time
    print(f"\nВремя выполнения: {execution_time:.6f} секунд")