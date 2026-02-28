import sys
import time

import pygame as pg
import torch


WIDTH = 1440
HEIGHT = 900

sc = pg.display.set_mode((WIDTH, HEIGHT))
phokus_pokus = (WIDTH/2, HEIGHT/2, 200)
X, Y, Z = -220, 0, 200


DOTS = []

class DOT_3_D:
    def __init__(self, x, y, z, color = (255, 255, 255)):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        DOTS.append(self)
    def get_pos_on_screen(self):
        k = ((self.y - Y)-phokus_pokus[1])/((self.z - Z)-phokus_pokus[2])
        y = phokus_pokus[1] - k*phokus_pokus[2]
        k = ((self.x- X)-phokus_pokus[0])/((self.z - Z)-phokus_pokus[2])
        x = phokus_pokus[0] - k*phokus_pokus[2]
        return x, y
    def draw(self):
        x, y = self.get_pos_on_screen()
        x = int(x)
        y = int(y)
        if x > 0 and x < WIDTH and y > 0 and y < HEIGHT:
            array[x, y, 0]= self.color[0]
            array[x, y, 1]= self.color[1]
            array[x, y, 2]= self.color[2]


#DOT1 = DOT_3_D(500, 300, 700, color=(255, 0, 255))
#DOT2 = DOT_3_D(510, 300, 700, color=(255, 0, 255))
#DOT3 = DOT_3_D(510, 310, 700, color=(255, 0, 255))
#DOT4 = DOT_3_D(500, 310, 700, color=(255, 0, 255))

#DOT11 = DOT_3_D(500, 300, 710, color=(25, 255, 255))
#DOT21 = DOT_3_D(510, 300, 710, color=(25, 255, 255))
#DOT31 = DOT_3_D(510, 310, 710, color=(25, 255, 255))
#DOT41 = DOT_3_D(500, 310, 710, color=(25, 255, 255))
x = 490
d = 0.5

while x <= 510:
    y = 500
    while y <= 520:
        z = 490
        while z <= 510:
            r = ((x-500)**2 + (y-510)**2 + (z-500)**2)
            if  r >= 90 and r <= 100:
                DOT_3_D(x, y, z, color = ((x-490)*255//20, (z-490)*255//20, (y-500)*255//20))
            z += d
        y += d
    x += d



while 1:
    array = torch.zeros([WIDTH, HEIGHT, 3], dtype=torch.float)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        Z += 1
    if keys[pg.K_s]:
        Z -= 1
    if keys[pg.K_a]:
        X += 1
    if keys[pg.K_d]:
        X -= 1
    if keys[pg.K_SPACE]:
        Y += 1
    if keys[pg.K_y]:
        Y -= 1

    for dot in DOTS:
        dot.draw()


    pg.surfarray.blit_array(sc, array.numpy())
    pg.display.update()
    time.sleep(1/60)