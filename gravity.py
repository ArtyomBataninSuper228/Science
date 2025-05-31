import random
import time
from threading import Thread
import pygame as pg
import math
import sys

pg.init()
masses = []#x, y, mass
objects = []
sc = pg.display.set_mode((1600, 900))
G = 6.67/10**11
air = 1.0000
font = pg.font.Font(None, 50)
zoom = 1/1000000000
is_clear = True
is_update = True
pos = [0, 0]
is_button = False
dt = 100
cx = 0
cy = 0
is_run = True

class Object():
    mass = 0
    spedx = 0
    spedy = 0
    x = 0
    y = 0
    num = 0
    fx = 0
    fy = 0
    is_stable = False
    is_alive = True
    def __init__(self, massa, spx, spy, xpos, ypos, n, stb):
        self.spedx = spx
        self.mass = massa

        self.x = xpos
        self.y = ypos
        self.spedy = spy
        self.num = n
        self.is_stable = stb





    def update(self):
        if self.is_alive:
            num = 0
            if self.is_stable:
                pass


            else:



                for i in masses:
                    if i == num:
                        continue
                    delx = -(self.x - i[0])
                    dely = -(self.y - i[1])
                    #vectr = [delx, dely]

                    distance = math.sqrt((delx ** 2) + (dely ** 2))
                    if (distance != 0):
                        self.fx += ((self.mass * i[2] * G) / (distance ** 2)) * (delx/distance)
                        self.fy += ((self.mass * i[2] * G) / (distance ** 2)) * (dely/distance)

                    num += 1
                self.spedx += (self.fx / self.mass)*dt
                self.spedy += (self.fy / self.mass)*dt
                self.fx = 0
                self.fy = 0
                self.x += (self.spedx)*dt
                self.y += (self.spedy)*dt



    def upd(self):
        if self.is_alive:
            if is_button:
                x = pos[0] - 500
                y = -(pos[1] - 250)
                if x < int(self.x*zoom) + 10 and x > int(self.x*zoom) - 10:
                    if y < int(self.y*zoom) + 10 and y > int(self.y*zoom) - 10:
                        self.is_alive = False
            dat = [self.x, self.y, self.mass]
            masses[self.num] = dat
            if self.is_stable:
                pg.draw.rect(sc, (25, 255, 25), (int((self.x - cx) * zoom) + 700, int((self.y - cy) * zoom) * (-1) + 450, 10, 10))
            else:
                pg.draw.rect(sc, (255, 255, 255), (int((self.x - cx) * zoom) + 700, int((self.y - cy) * zoom) * (-1) + 450, 10, 10))
        else:
            dat = [0, 0, 0]
            masses[self.num] = dat


a = Object(10**(30.29863478312443), 0, 0, 0, 0, 0, True)
objects.append(a)
masses.append([0, 0, 0])
#for i in range(1, 10):

a = Object(10**(24.776119799052988), 29722.222222222222222, 0, 0, 149597871000, 1, False)# Земля
objects.append(a)
masses.append([0, 0, 0])
print(50*a.spedx**2/(a.y))

a = Object(10**(23.8055008581584), 24130, 0, 0, 228000000000, 2, False)# Марс
objects.append(a)
masses.append([0, 0, 0])



a = Object(10**(23.5165353738958), 47900, 0, 0, 57910000000, 3, False)# Меркурий
objects.append(a)
masses.append([0, 0, 0])


a = Object(4.8675*(10**24), 35020, 0, 0, 107476259000, 4, False)# Венера
objects.append(a)
masses.append([0, 0, 0])

a = Object(5.6846 * (10**26), 9690, 0, 0, 1353572956000, 5, False)# Юпитер
objects.append(a)
masses.append([0, 0, 0])


a = Object(7.3477*(10**22), 30745, -100, 0, 149960975000, 6, False)# Луна
objects.append(a)
masses.append([0, 0, 0])

def f():
    while is_run== True:
        if is_update == True:
            for i in range(0, len(objects)):
                objects[i].update()
        global cx, cy
        #cx = objects[1].x
        #cy = objects[1].y
        for i in range(0, len(objects)):
            objects[i].upd()
        #pg.display.update()

t = Thread(target= f)
t.start()


real_t = 0
while 1:
    t1 = time.time()
    for i in pg.event.get():
        pok = True
        if i.type == pg.QUIT:
            is_run = False
            sys.exit()
        elif i.type == pg.MOUSEBUTTONDOWN:
            is_button = True
        elif i.type == pg.MOUSEBUTTONUP:
            is_button = False
        elif i.type == pg.MOUSEMOTION:
            pos[0] = i.pos[0]
            pos[1] = i.pos[1]
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_PLUS:
                zoom *= 1.5
            elif i.key == pg.K_MINUS:
                zoom/= 1.5
            elif i.key == pg.K_RETURN:
                is_clear *= -1
            elif i.key == pg.K_d:
                is_update *= -1
            elif i.key == pg.K_a:
                a = Object(random.randint(1, 10), random.randint(-100, 100) / 10, random.randint(-100, 100) / 100,
                           random.randint(-5000, 5000), random.randint(-5000, 5000), len(objects), False)
                objects.append(a)
                masses.append([0, 0, 0])
            elif i.key == pg.K_t:
                print(real_t)

    '''
    if is_update == True:
        for i in range(0, len(objects)):
            objects[i].update()
    
    for i in range(0, len(objects)):
        objects[i].upd()
    pg.display.update()
    '''
    if is_clear == 1:
        sc.fill((0, 0, 0))
    t2 = time.time()
    #real_t += dt
    pg.display.update()

    #dt = t2-t1









