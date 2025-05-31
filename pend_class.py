from math import *


class pendulum:
    x = 0
    y = 0
    vx = 0
    vy = 0
    ax = 0
    ay = 0
    m = 0
    def __init__(self, x, y, m):
        self.x = x
        self.y = y
        self.m = m

class double_pendulum():


    def __init__(self, x1, x2, y1, y2, m1, m2):

        self.dt = 10 ** (-5)
        self.g = 9.8
        self.time_of_simulation = 0
        self.p1 = pendulum(1, -1, 1)
        self.p2 = pendulum(1, -1, 1)
        self.T1 = 0
        self.T2 = 0
        self.l1 = (self.p1.x ** 2 + self.p1.y ** 2) ** 0.5
        self.l2 = (self.p2.x ** 2 + self.p2.y ** 2) ** 0.5
        self.cosa = self.p1.y / self.l1
        self.sina = self.p1.x / self.l1
        self.cosb = self.p2.y / self.l2
        self.sinb = self.p2.x / self.l2
        # cosy = p1.ax / (p1.ax ** 2 + (p1.ay - g) ** 2) ** 0.5
        self.a = acos(self.cosa)
        self.b = acos(self.cosb)
        self.p1.x = x1
        self.p1.y = y1
        self.p2.x = x2
        self.p2.y = y2
        self.p1.m = m1
        self.p2.m = m2
    def update(self):
        t2 = self.T2


        pcosb = self.cosb
        psinb = self.sinb
        pcosa = self.cosa
        psina = self.sina

        # p1.ax = 10
        # p1.ay = 0
        l1 = (self.p1.x ** 2 + self.p1.y ** 2) ** 0.5
        l2 = (self.p2.x ** 2 + self.p2.y ** 2) ** 0.5
        self.p1.ax *= -1
        self.p1.ay *= -1
        cosa = self.p1.y / l1
        sina = self.p1.x / l1
        cosb = self.p2.y / l2
        sinb = self.p2.x / l2

        if (self.p1.ax ** 2 + (self.p1.ay - self.g) ** 2) != 0:
            cosy = (self.p1.ay - self.g) / (self.p1.ax ** 2 + (self.p1.ay - self.g) ** 2) ** 0.5
            siny = self.p1.ax / (self.p1.ax ** 2 + (self.p1.ay - self.g) ** 2) ** 0.5
        else:
            siny = 0
            cosy = 0

        T2 = self.p2.m * (self.p2.vx ** 2 + self.p2.vy ** 2) / l2 + self.p2.m * (self.p1.ax ** 2 + (self.p1.ay - self.g) ** 2) ** 0.5 * (
                    cosb * cosy + siny * sinb)
        T1 = self.p1.m * (self.p1.vx ** 2 + self.p1.vy ** 2) / l1 - self.p1.m * self.g * self.cosa + t2 * (pcosa * pcosb + psina * psinb)
        self.p2.ax = -T2 * sinb / self.p2.m + self.p1.ax
        self.p2.ay = -T2 * cosb / self.p2.m + self.p1.ay - self.g
        self.p2.vx += self.p2.ax * self.dt
        self.p2.vy += self.p2.ay * self.dt
        self.p2.x += self.p2.vx * self.dt
        self.p2.y += self.p2.vy * self.dt
        self.p1.ax *= -1
        self.p1.ay *= -1

        self.p1.ax = -T1 * sina / self.p1.m + t2 * psinb / self.p1.m
        self.p1.ay = -T1 * self.cosa / self.p1.m - self.g + t2 * pcosb / self.p1.m
        self.p1.vx += self.p1.ax * self.dt
        self.p1.vy += self.p1.ay * self.dt
        self.p1.x += self.p1.vx * self.dt
        self.p1.y += self.p1.vy * self.dt

        # va = (a-preva)/self.dt
        # vb = (b - prevb)/self.dt
        # massive_of_angles.append(a)
        # massive_of_angle_speed[0].append(va)
        self.time_of_simulation += self.dt

        # print(a, b, y, a+b)
    def start_updating(self, time_of_stop):
        while self.time_of_simulation < time_of_stop:
            #print(self.time_of_simulation, self.p1.x)
            t2 = self.T2

            pcosb = self.cosb
            psinb = self.sinb
            pcosa = self.cosa
            psina = self.sina

            # p1.ax = 10
            # p1.ay = 0
            l1 = (self.p1.x ** 2 + self.p1.y ** 2) ** 0.5
            l2 = (self.p2.x ** 2 + self.p2.y ** 2) ** 0.5
            self.p1.ax *= -1
            self.p1.ay *= -1
            self.cosa = self.p1.y / l1
            self.sina = self.p1.x / l1
            self.cosb = self.p2.y / l2
            self.sinb = self.p2.x / l2

            if (self.p1.ax ** 2 + (self.p1.ay - self.g) ** 2) != 0:
                cosy = (self.p1.ay - self.g) / (self.p1.ax ** 2 + (self.p1.ay - self.g) ** 2) ** 0.5
                siny = self.p1.ax / (self.p1.ax ** 2 + (self.p1.ay - self.g) ** 2) ** 0.5
            else:
                siny = 0
                cosy = 0

            self.T2 = self.p2.m * (self.p2.vx ** 2 + self.p2.vy ** 2) / l2 + self.p2.m * (
                        self.p1.ax ** 2 + (self.p1.ay - self.g) ** 2) ** 0.5 * (
                         self.cosb * cosy + siny * self.sinb)
            self.T1 = self.p1.m * (self.p1.vx ** 2 + self.p1.vy ** 2) / l1 - self.p1.m * self.g * self.cosa + t2 * (
                        pcosa * pcosb + psina * psinb)
            self.p2.ax = -self.T2 * self.sinb / self.p2.m + self.p1.ax
            self.p2.ay = -self.T2 * self.cosb / self.p2.m + self.p1.ay - self.g
            self.p2.vx += self.p2.ax * self.dt
            self.p2.vy += self.p2.ay * self.dt
            self.p2.x += self.p2.vx * self.dt
            self.p2.y += self.p2.vy * self.dt
            self.p1.ax *= -1
            self.p1.ay *= -1

            self.p1.ax = -self.T1 * self.sina / self.p1.m + t2 * psinb / self.p1.m
            self.p1.ay = -self.T1 * self.cosa / self.p1.m - self.g + t2 * pcosb / self.p1.m
            self.p1.vx += self.p1.ax * self.dt
            self.p1.vy += self.p1.ay * self.dt
            self.p1.x += self.p1.vx * self.dt
            self.p1.y += self.p1.vy * self.dt

            # va = (a-preva)/self.dt
            # vb = (b - prevb)/self.dt
            # massive_of_angles.append(a)
            # massive_of_angle_speed[0].append(va)
            self.time_of_simulation += self.dt




