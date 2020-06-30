import pygame


class Pistol(object):
    def __init__(self):
        self.magazine = 5
        self.bullets = 75
        self.font = pygame.font.SysFont('comicsans', 50)
        self.updateMagazineText()
        self.PistolText = self.font.render('PISTOL', 1, (255, 255, 255))
        self.counter = 0
        self.relodingText1 = self.font.render('RELOADING.', 1, (255, 255, 255))
        self.relodingText2 = self.font.render('RELOADING..', 1, (255, 255, 255))
        self.relodingText3 = self.font.render('RELOADING...', 1, (255, 255, 255))

    def updateMagazineText(self):
        self.magazineText = self.font.render(str(self.magazine), 1, (255, 255, 255))
        self.bulletsText = self.font.render(str(self.bullets), 1, (255, 255, 255))


    def draw(self, win, x, y, left):
        if left == False:
            pygame.draw.rect(win, (0, 0, 0), (x + 25, y + 35, 3, 10))
            pygame.draw.rect(win, (0, 0, 0), (x + 25, y + 33, 16, 3))
        else:
            pygame.draw.rect(win, (0, 0, 0), (x + 15, y + 35, 3, 10))
            pygame.draw.rect(win, (0, 0, 0), (x + 2, y + 33, 16, 3))

        pygame.draw.rect(win, (255, 255, 255), (55, 47, 5, 25))
        win.blit(self.PistolText, (10, 10))

    def shoot(self, win, x, y, left, shoot):
        if self.counter == 0:
            if left == False and shoot == True:
                pygame.draw.rect(win, (200, 150, 0), (x + 41, y + 32, 8, 5))
                self.magazine -= 1
            if left == True and shoot == True:
                pygame.draw.rect(win, (200, 150, 0), (x - 5, y + 32, 8, 5))
                self.magazine -= 1

    def bulletTracker(self, win):
        if self.magazine <= 0:
           self.magazine = 0
           self.counter += 1
        if self.counter >= 90:
            self.bullets -= 5
            self.magazine = 5
            self.counter = 0

        if self.counter < 30 and self.magazine <= 0:
            win.blit(self.relodingText1, (250, 150))
        if self.counter >= 30 and self.counter < 60 and self.magazine <= 0:
            win.blit(self.relodingText2, (250, 150))
        if self.counter >= 60 and self.counter <= 90 and self.magazine <= 0:
            win.blit(self.relodingText3, (250, 150))


        self.updateMagazineText()

        win.blit(self.magazineText, (30, 44))
        win.blit(self.bulletsText, (65, 44))
        pygame.display.update()






