import numpy as np


class Desk:
    def __init__(self, w, h, a):
        self.old_desk = np.int8(np.zeros((h, w)))
        self.new_desk = np.int8(np.zeros((h, w)))
        self.desk = self.old_desk
        self.w = w
        self.h = h
        self.a = a

    def kletka_klic(self, coord=(0, 0)):
        x = coord[0] // self.a
        y = coord[1] // self.a
        if x < self.w + 1 and y < self.h + 1:
            self.delta_color(x, y, self.desk)
        else:
            print("такой клетки нет!")

    def delta_color(self, x, y, desk):
        if desk[y][x] == 1:
            desk[y][x] = 0
        else:
            desk[y][x] = 1

    def update(self):
        old_desk = self.old_desk
        new_desk = self.new_desk
        w, h = self.w, self.h
        for y, i in enumerate(old_desk):
            for x, a in enumerate(i):
                c = -old_desk[y][x]
                for x1 in range(x - 1, x + 2):
                    for y1 in range(y - 1, y + 2):
                        c += old_desk[y1 % h][x1 % w]
                if a == 1:
                    if c < 2 or c > 3:
                        new_desk[y][x] = 0
                    else:
                        new_desk[y][x] = 1
                else:
                    if c == 3:
                        new_desk[y][x] = 1
                    else:
                        new_desk[y][x] = 0
        self.desk = new_desk
        self.new_desk = old_desk
        self.old_desk = new_desk
