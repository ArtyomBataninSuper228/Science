from stegano import lsb

# Скрываем сообщение в картинке
s = "WPLACE is a cool website"*100
secret_image = lsb.hide("mem.jpg", s)
secret_image.save("output.png")