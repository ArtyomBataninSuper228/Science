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


"""def smooth_magnitudes(magnitudes, window_size=1001, iterations=1):
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

    return smoothed"""

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


def enhance_peaks_fft(fft_data, threshold_db=-30, max_boost=2.0, min_attenuation=0.5):
    """
    Усиливает громкие пики и ослабляет тихие звуки в FFT данных.

    Parameters:
    -----------
    fft_data : array_like
        Комплексный массив FFT данных
    threshold_db : float, optional
        Порог в dB выше которого начинается усиление (по умолчанию -30 dB)
    max_boost : float, optional
        Максимальное усиление для самых громких пиков (по умолчанию 2.0)
    min_attenuation : float, optional
        Минимальное ослабление для самых тихих звуков (по умолчанию 0.5)

    Returns:
    --------
    enhanced_fft : ndarray
        Обработанный комплексный массив FFT
    """

    # Вычисляем амплитуды (модули комплексных чисел)
    amplitudes = np.abs(fft_data)

    # Избегаем деления на ноль, заменяя нули очень маленьким числом
    amplitudes = np.where(amplitudes == 0, 1e-10, amplitudes)

    # Вычисляем мощность в dB
    max_amplitude = np.max(amplitudes)
    power_db = 20 * np.log10(amplitudes / max_amplitude)

    # Создаем маску для усиления/ослабления
    # Нормализуем мощность от 0 (тихие) до 1 (громкие)
    normalized_power = (power_db - threshold_db) / (-threshold_db)
    normalized_power = np.clip(normalized_power, 0, 1)

    # Создаем коэффициенты усиления/ослабления
    # Громкие звуки усиливаются до max_boost, тихие ослабляются до min_attenuation
    gain_factors = min_attenuation + (max_boost - min_attenuation) * normalized_power

    # Применяем коэффициенты к FFT данным
    # Умножаем амплитуды, сохраняя фазы
    enhanced_fft = fft_data * gain_factors

    return enhanced_fft
def smooth_magnitudes(magnitudes, num_points=30):
    """
    Очень агрессивное определение уровня шума.
    """
    n = len(magnitudes)

    # Разбиваем частотный диапазон на num_points сегментов
    segment_size = n // num_points
    noise_levels = np.zeros(num_points)

    for i in range(num_points):
        start_idx = i * segment_size
        end_idx = start_idx + segment_size if i < num_points - 1 else n

        segment = magnitudes[start_idx:end_idx]

        # Очень агрессивно - берем минимальные значения как шум
        base_noise = np.percentile(segment, 2)  # Всего 2-й процентиль!

        # Сильно увеличиваем предполагаемый уровень шума для агрессивного подавления
        noise_levels[i] = base_noise * 2.0  # Увеличиваем в 2 раза

    # Интерполируем уровни шума для всех частот
    x_points = np.linspace(0, n - 1, num_points)
    x_all = np.arange(n)

    # Используем линейную интерполяцию
    smoothed = np.interp(x_all, x_points, noise_levels)

    return smoothed


def create_modified_audio(original_fft, original_magnitudes, smoothed_magnitudes, n):
    """
    Улучшенное подавление шума с защитой от создания артефактов в противофазе.
    """
    modified_fft = original_fft.copy()

    # Минимальный уровень сигнала для предотвращения чрезмерного подавления
    min_level = np.max(original_magnitudes) * 0.001  # 0.1% от максимальной амплитуды

    # Для положительных частот
    for i in range(n // 2):
        if original_magnitudes[i] > 0:
            # Адаптивный порог шума
            noise_threshold = smoothed_magnitudes[i] * 3  # Менее агрессивный множитель

            # Сохраняем фазу исходного сигнала
            original_phase = np.angle(original_fft[i])

            # Вычитаем шум с защитой от чрезмерного подавления
            if original_magnitudes[i] > noise_threshold * 1.2:  # Сигнал значительно выше шума
                new_magnitude = max(min_level, original_magnitudes[i] - noise_threshold)
                new_magnitude = new_magnitude * 1.2  # Более умеренное усиление
            else:  # Сигнал близок к уровню шума
                # Плавное ослабление вместо резкого вычитания
                reduction_factor = max(0.1, (original_magnitudes[i] - noise_threshold * 0.5) /
                                       (noise_threshold * 0.7))
                new_magnitude = max(min_level, original_magnitudes[i] * reduction_factor)

            # Восстанавливаем комплексное число
            modified_fft[i] = new_magnitude * np.exp(1j * original_phase)

    # Для отрицательных частот (симметрично)
    for i in range(n // 2 + 1, n):
        j = n - i
        if j < len(original_magnitudes) and original_magnitudes[j] > 0:
            noise_threshold = smoothed_magnitudes[j] * 3.0
            original_phase = np.angle(original_fft[i])

            if original_magnitudes[j] > noise_threshold * 1.2:
                new_magnitude = max(min_level, original_magnitudes[j] - noise_threshold)
                new_magnitude = new_magnitude * 1.2
            else:
                reduction_factor = max(0.1, (original_magnitudes[j] - noise_threshold * 0.5) /
                                       (noise_threshold * 0.7))
                new_magnitude = max(min_level, original_magnitudes[j] * reduction_factor)

            modified_fft[i] = new_magnitude * np.exp(1j * original_phase)

    # Дополнительная защита: проверка на аномально низкие уровни
    modified_magnitudes = np.abs(modified_fft)
    avg_modified = np.mean(modified_magnitudes)

    # Если средний уровень стал слишком низким, ограничиваем минимальные значения
    if avg_modified < min_level * 10:
        for i in range(n):
            if modified_magnitudes[i] < min_level:
                # Сохраняем фазу, но устанавливаем минимальный разумный уровень
                phase = np.angle(modified_fft[i])
                modified_fft[i] = min_level * 0.5 * np.exp(1j * phase)

    modified_fft = enhance_peaks_fft(modified_fft)
    return modified_fft


def main():
    file_path = "2025-10-22 17.32.57.wav"
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
    smoothed_magnitudes = smooth_magnitudes(magnitudes, num_points=30)

    # Создаем модифицированный аудиосигнал
    print("Создание модифицированного аудио...")
    modified_fft = create_modified_audio(fft_result, magnitudes, smoothed_magnitudes, len(audio_data))
    modified_audio = np.real(ifft(modified_fft))

    # Нормализуем и преобразуем к исходному типу данных
    modified_audio = np.int16(modified_audio / np.max(np.abs(modified_audio)) * 32767)

    # Сохраняем новый WAV-файл
    output_path = "test_sound_cleaned.wav"
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