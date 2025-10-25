import cv2
import numpy as np
from collections import deque
import os
import sys


class GridRemover:
    def __init__(self, blur_radius=2):
        self.blur_radius = blur_radius

    def find_grid_color(self, image):
        """Определяет цвет сетки и возвращает список пикселей сетки"""
        height, width = image.shape[:2]
        visited = np.zeros((height, width), dtype=bool)
        grid_pixels = []

        print("Анализ изображения для поиска сетки...")

        # Проходим по всем пикселям изображения
        for y in range(0, height, 3):  # Шаг для ускорения обработки
            for x in range(0, width, 3):
                if visited[y, x]:
                    continue

                current_color = image[y, x]
                similar_pixels = self._find_similar_pixels(image, visited, x, y, current_color)

                # Если найдена достаточно большая группа похожих пикселей - считаем это сеткой
                if len(similar_pixels) > 50:  # Увеличим минимальный размер для лучшего определения
                    grid_pixels.extend(similar_pixels)
                    print(f"Найдена группа сетки из {len(similar_pixels)} пикселей")

        return grid_pixels

    def _find_similar_pixels(self, image, visited, start_x, start_y, target_color):
        """Находит все пиксели, похожие на целевой цвет (разница <= 1 по каждому каналу)"""
        height, width = image.shape[:2]
        similar_pixels = []
        queue = deque([(start_x, start_y)])

        while queue:
            x, y = queue.popleft()

            if x < 0 or x >= width or y < 0 or y >= height or visited[y, x]:
                continue

            current_color = image[y, x]

            # Для grayscale изображений
            if len(image.shape) == 2:
                color_diff = abs(int(current_color) - int(target_color))
                if color_diff <= 1:
                    visited[y, x] = True
                    similar_pixels.append((x, y, current_color))

                    # Добавляем соседние пиксели в очередь
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        queue.append((x + dx, y + dy))
            else:
                # Для цветных изображений
                color_diff = np.abs(current_color.astype(int) - target_color.astype(int))

                # Проверяем, отличается ли цвет не более чем на 1 по каждому каналу
                if np.all(color_diff <= 1):
                    visited[y, x] = True
                    similar_pixels.append((x, y, current_color))

                    # Добавляем соседние пиксели в очередь
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        queue.append((x + dx, y + dy))

        return similar_pixels

    def remove_grid(self, image_path, output_path):
        """Основная функция для удаления сетки"""
        # Загружаем изображение с проверкой ошибок
        print(f"Попытка загрузить изображение: {image_path}")

        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Файл не существует: {image_path}")

        # Пробуем разные способы загрузки
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

        if image is None:
            # Пробуем загрузить как цветное
            image = cv2.imread(image_path, cv2.IMREAD_COLOR)

        if image is None:
            # Пробуем загрузить как grayscale
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:
            raise ValueError(f"Не удалось загрузить изображение: {image_path}. "
                             "Проверьте путь и корректность файла.")

        print(f"Изображение загружено успешно. Размер: {image.shape}")

        # Конвертируем в BGR если нужно
        if len(image.shape) == 2:
            image_bgr = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        elif image.shape[2] == 4:  # RGBA
            image_bgr = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
        elif image.shape[2] == 3:
            image_bgr = image
        else:
            image_bgr = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        print("Поиск пикселей сетки...")
        grid_pixels = self.find_grid_color(image_bgr)
        print(f"Найдено пикселей сетки: {len(grid_pixels)}")

        if not grid_pixels:
            print("Сетка не найдена на изображении. Попробуйте уменьшить шаг поиска.")
            # Сохраняем оригинал
            cv2.imwrite(output_path, image_bgr)
            return

        print("Замена цвета пикселей сетки...")
        self._replace_grid_pixels(image_bgr, grid_pixels)

        # Сохраняем результат
        cv2.imwrite(output_path, image_bgr)
        print(f"Результат сохранен в: {output_path}")

    def _replace_grid_pixels(self, image, grid_pixels):
        """Заменяет цвет пикселей сетки на цвет соседних пикселей"""
        height, width = image.shape[:2]
        grid_mask = np.zeros((height, width), dtype=bool)

        # Создаем маску сетки
        for x, y, _ in grid_pixels:
            if 0 <= x < width and 0 <= y < height:
                grid_mask[y, x] = True

        print("Обработка пикселей сетки...")
        total_pixels = len(grid_pixels)

        for i, (x, y, _) in enumerate(grid_pixels):
            if i % 1000 == 0:  # Прогресс каждые 1000 пикселей
                print(f"Обработано {i}/{total_pixels} пикселей")

            if 0 <= x < width and 0 <= y < height:
                new_color = self._get_replacement_color(image, x, y, grid_mask)
                if new_color is not None:
                    image[y, x] = new_color

    def _get_replacement_color(self, image, x, y, grid_mask):
        """Получает цвет для замены на основе соседних пикселей"""
        height, width = image.shape[:2]
        radius = self.blur_radius
        max_radius = min(width, height) // 4  # Максимальный радиус

        while radius <= max_radius:
            neighbors = []

            # Собираем соседние пиксели в заданном радиусе
            for dy in range(-radius, radius + 1):
                for dx in range(-radius, radius + 1):
                    if dx == 0 and dy == 0:
                        continue

                    nx, ny = x + dx, y + dy

                    if 0 <= nx < width and 0 <= ny < height:
                        if not grid_mask[ny, nx]:  # Только не сеточные пиксели
                            neighbors.append(image[ny, nx])

            # Если нашли соседей не из сетки - возвращаем средний цвет
            if neighbors:
                return np.median(neighbors, axis=0).astype(np.uint8)

            # Если вокруг только пиксели сетки - увеличиваем радиус
            radius += 1

        # Если не нашли замену - возвращаем черный цвет
        return np.array([0, 0, 0], dtype=np.uint8)


def check_file_path(file_path):
    """Проверяет корректность пути к файлу"""
    if not os.path.exists(file_path):
        print(f"Ошибка: Файл '{file_path}' не существует!")
        return False

    if not os.path.isfile(file_path):
        print(f"Ошибка: '{file_path}' не является файлом!")
        return False

    # Проверяем расширение файла
    valid_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.tif'}
    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext not in valid_extensions:
        print(f"Предупреждение: Нестандартное расширение файла: {file_ext}")
        print(f"Поддерживаемые форматы: {', '.join(valid_extensions)}")

    return True


def main():
    # Настройки программы
    BLUR_RADIUS = 3  # Начальный радиус размытия

    print("=== Программа для удаления сетки с изображения ===")
    print()

    # Запрос путей у пользователя
    input_image = input("Введите путь к входному изображению: ").strip().strip('"')

    if not check_file_path(input_image):
        return

    output_image = input("Введите путь для сохранения результата: ").strip().strip('"')

    if not output_image:
        # Генерируем автоматическое имя
        name, ext = os.path.splitext(input_image)
        output_image = f"{name}_no_grid{ext}"
        print(f"Автоматически сгенерирован путь: {output_image}")

    # Создаем экземпляр класса и запускаем обработку
    remover = GridRemover(blur_radius=BLUR_RADIUS)

    try:
        remover.remove_grid(input_image, output_image)
        print("Обработка завершена успешно!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        print("Попробуйте следующее:")
        print("1. Проверьте путь к файлу")
        print("2. Убедитесь, что файл не поврежден")
        print("3. Попробуйте конвертировать изображение в другой формат")
        print("4. Уменьшите размер изображения если оно очень большое")


if __name__ == "__main__":
    main()