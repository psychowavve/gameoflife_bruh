import pygame
import time
import classes

FPS = 5
pygame.init()
sc = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Game of Life")


class DeskGraphics(classes.Desk):
    def __init__(self, w, h, a):
        classes.Desk.__init__(self, w, h, a)

    def draw(self):
        y = 0
        for i in self.desk:
            x = 0
            for a in i:
                if a == 1:
                    pygame.draw.rect(sc, (255, 255, 255), (x * self.a, y * self.a, self.a, self.a))
                else:
                    pygame.draw.rect(sc, (0, 0, 0), (x * self.a, y * self.a, self.a, self.a))
                x += 1
            y += 1


a = DeskGraphics(50, 50, 10)

simulating = 0
time0 = time.time()
flRunning = True


while True:
    time1 = time.time()
    FPS = 1 // (time1)
    # pygame.display.set_caption("FPS = " + str(FPS))

    a.draw()
    if simulating:
        a.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Закрытие окна...")
            pygame.quit()
            flRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                a.kletka_klic(coord=event.pos)
            elif event.button == 3:
                if simulating:
                    simulating = 0
                else:
                    simulating = 1

    if not flRunning:
        break

    time0 = time1
    pygame.display.flip()
    #    time.sleep(0.05)
    sc.fill((0, 0, 0))