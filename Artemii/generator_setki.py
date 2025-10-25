import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser
from PIL import Image, ImageTk, ImageDraw
import numpy as np


class PixelGridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Grid Generator")
        self.root.geometry("800x600")

        self.original_image = None
        self.processed_image = None
        self.image_path = None

        # Параметры сетки по умолчанию
        self.grid_thickness = tk.IntVar(value=1)
        self.grid_frequency = tk.IntVar(value=10)
        self.grid_color = "#000000"

        self.setup_ui()

    def setup_ui(self):
        # Основной фрейм
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Левая панель - настройки
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        # Кнопка загрузки изображения
        ttk.Button(left_frame, text="Загрузить изображение",
                   command=self.load_image).pack(fill=tk.X, pady=5)

        # Настройки сетки
        settings_frame = ttk.LabelFrame(left_frame, text="Настройки сетки")
        settings_frame.pack(fill=tk.X, pady=10)

        # Толщина сетки
        ttk.Label(settings_frame, text="Толщина сетки:").pack(anchor=tk.W)
        thickness_scale = ttk.Scale(settings_frame, from_=1, to=10,
                                    variable=self.grid_thickness, orient=tk.HORIZONTAL)
        thickness_scale.pack(fill=tk.X, pady=5)

        # Частота сетки (размер ячейки)
        ttk.Label(settings_frame, text="Размер ячейки (пикселей):").pack(anchor=tk.W)
        frequency_scale = ttk.Scale(settings_frame, from_=1, to=50,
                                    variable=self.grid_frequency, orient=tk.HORIZONTAL)
        frequency_scale.pack(fill=tk.X, pady=5)

        # Цвет сетки
        ttk.Label(settings_frame, text="Цвет сетки:").pack(anchor=tk.W)
        color_frame = ttk.Frame(settings_frame)
        color_frame.pack(fill=tk.X, pady=5)

        self.color_preview = tk.Label(color_frame, bg=self.grid_color, width=5, height=1)
        self.color_preview.pack(side=tk.LEFT, padx=(0, 5))

        ttk.Button(color_frame, text="Выбрать цвет",
                   command=self.choose_color).pack(side=tk.LEFT)

        # Кнопки применения и сохранения
        ttk.Button(left_frame, text="Применить сетку",
                   command=self.apply_grid).pack(fill=tk.X, pady=5)

        ttk.Button(left_frame, text="Сохранить изображение",
                   command=self.save_image).pack(fill=tk.X, pady=5)

        # Правая панель - предпросмотр
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Canvas для отображения изображения
        self.canvas = tk.Canvas(right_frame, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Привязка событий для обновления предпросмотра
        thickness_scale.configure(command=self.on_slider_change)
        frequency_scale.configure(command=self.on_slider_change)

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")]
        )

        if file_path:
            try:
                self.image_path = file_path
                self.original_image = Image.open(file_path)
                self.show_image()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {str(e)}")

    def choose_color(self):
        color = colorchooser.askcolor(initialcolor=self.grid_color)[1]
        if color:
            self.grid_color = color
            self.color_preview.configure(bg=color)
            if self.original_image:
                self.apply_grid()

    def on_slider_change(self, event=None):
        if self.original_image:
            self.apply_grid()

    def apply_grid(self):
        if self.original_image is None:
            return

        try:
            # Создаем копию оригинального изображения
            self.processed_image = self.original_image.copy()
            draw = ImageDraw.Draw(self.processed_image)

            width, height = self.processed_image.size
            cell_size = self.grid_frequency.get()
            thickness = self.grid_thickness.get()

            # Рисуем вертикальные линии
            for x in range(0, width, cell_size):
                draw.line([(x, 0), (x, height)], fill=self.grid_color, width=thickness)

            # Рисуем горизонтальные линии
            for y in range(0, height, cell_size):
                draw.line([(0, y), (width, y)], fill=self.grid_color, width=thickness)

            self.show_image()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось применить сетку: {str(e)}")

    def show_image(self):
        if self.processed_image is None and self.original_image:
            self.processed_image = self.original_image.copy()

        if self.processed_image:
            # Масштабируем изображение для отображения в canvas
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()

            if canvas_width > 1 and canvas_height > 1:
                img = self.processed_image.copy()
                img.thumbnail((canvas_width, canvas_height), Image.Resampling.LANCZOS)

                self.tk_image = ImageTk.PhotoImage(img)
                self.canvas.delete("all")
                self.canvas.create_image(canvas_width // 2, canvas_height // 2,
                                         image=self.tk_image, anchor=tk.CENTER)

    def save_image(self):
        if self.processed_image is None:
            messagebox.showwarning("Предупреждение", "Нет изображения для сохранения")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"),
                       ("All files", "*.*")]
        )

        if file_path:
            try:
                self.processed_image.save(file_path)
                messagebox.showinfo("Успех", "Изображение успешно сохранено!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить изображение: {str(e)}")


def main():
    root = tk.Tk()
    app = PixelGridApp(root)

    # Обработка изменения размера окна
    def on_resize(event):
        app.show_image()

    root.bind('<Configure>', on_resize)
    root.mainloop()


if __name__ == "__main__":
    main()