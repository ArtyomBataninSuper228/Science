import qrcode

# Генерация и сохранение в файл
img = qrcode.make('https://github.com/ArtyomBataninSuper228/Science/tree/main/Labs/1p1')
img.save('qrcode.png')
