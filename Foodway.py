import pygame
import People


class Foodway(object):
    def __init__(self):

        self.parkinglot = False
        self.checkout = False
        self.manager1 = False

        self.font = pygame.font.SysFont('comicsans', 50)
        self.text = self.font.render('QUICK, KILL THE MANAGER', 1, (255, 255, 255))
        self.text2 = self.font.render('GREAT, NOW GRAB SOME STUFF', 1, (255, 255, 255))
        self.text3 = self.font.render('THE COPS WILL BE HERE SOON', 1, (255, 255, 255))
        self.excapetextCounter = 0
        self.textCounter = 0
        self.policeCounter = 0

        self.stuff = 0

    def draw(self, win, aya, oliver, manager):
        if self.parkinglot:
            pygame.draw.rect(win, (0, 0, 0), (660, 300, 40, 300))
            pygame.draw.rect(win, (200, 200, 0), (640, 260, 60, 40))

        if self.checkout:
            pygame.draw.rect(win, (0, 0, 0), (100, 300, 10, 100))
            pygame.draw.rect(win, (0, 0, 0), (300, 300, 10, 100))

            pygame.draw.rect(win, (0, 0, 0), (110, 330, 200, 10))
            pygame.draw.rect(win, (0, 0, 0), (110, 380, 200, 10))


            pygame.draw.rect(win, (0, 100, 0), (110, 305, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (120, 305, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (130, 305, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (140, 305, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (150, 307, 10, 23))
            pygame.draw.rect(win, (0, 100, 0), (160, 305, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (170, 305, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (180, 305, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (190, 308, 10, 22))
            pygame.draw.rect(win, (100, 0, 0), (200, 305, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (210, 305, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (220, 305, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (230, 305, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (240, 308, 10, 22))
            pygame.draw.rect(win, (100, 0, 0), (250, 305, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (260, 305, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (270, 305, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (280, 305, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (290, 305, 10, 25))

            pygame.draw.rect(win, (0, 100, 0), (110, 355, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (120, 355, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (130, 355, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (140, 355, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (150, 357, 10, 23))
            pygame.draw.rect(win, (0, 100, 0), (160, 355, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (170, 355, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (180, 355, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (190, 358, 10, 22))
            pygame.draw.rect(win, (100, 0, 0), (200, 355, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (210, 355, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (220, 356, 10, 24))
            pygame.draw.rect(win, (0, 100, 0), (230, 355, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (240, 355, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (250, 355, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (260, 358, 10, 22))
            pygame.draw.rect(win, (100, 0, 0), (270, 355, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (280, 355, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (290, 355, 10, 25))

            pygame.draw.rect(win, (0, 0, 0), (400, 300, 10, 100))
            pygame.draw.rect(win, (0, 0, 0), (600, 300, 10, 100))

            pygame.draw.rect(win, (0, 0, 0), (410, 330, 200, 10))
            pygame.draw.rect(win, (0, 0, 0), (410, 380, 200, 10))

            pygame.draw.rect(win, (0, 100, 0), (410, 305, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (420, 305, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (430, 305, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (440, 305, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (450, 307, 10, 23))
            pygame.draw.rect(win, (0, 100, 0), (460, 305, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (470, 305, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (480, 305, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (490, 308, 10, 22))
            pygame.draw.rect(win, (100, 0, 0), (500, 305, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (510, 305, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (520, 305, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (530, 305, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (540, 308, 10, 22))
            pygame.draw.rect(win, (100, 0, 0), (550, 305, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (560, 305, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (570, 305, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (580, 305, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (590, 305, 10, 25))

            pygame.draw.rect(win, (0, 100, 0), (410, 355, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (420, 355, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (430, 355, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (440, 355, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (450, 357, 10, 23))
            pygame.draw.rect(win, (0, 100, 0), (460, 355, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (470, 355, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (480, 355, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (490, 358, 10, 22))
            pygame.draw.rect(win, (100, 0, 0), (500, 355, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (510, 355, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (520, 356, 10, 24))
            pygame.draw.rect(win, (0, 100, 0), (530, 355, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (540, 355, 10, 25))
            pygame.draw.rect(win, (100, 0, 0), (550, 355, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (560, 358, 10, 22))
            pygame.draw.rect(win, (100, 0, 0), (570, 355, 10, 25))
            pygame.draw.rect(win, (0, 100, 0), (580, 355, 10, 25))
            pygame.draw.rect(win, (0, 0, 100), (590, 355, 10, 25))

            aya.draw(win)
            oliver.draw(win)

        if self.manager1:
            self.textCounter += 1

            if self.textCounter < 100 and manager.health > 0:
                win.blit(self.text, (100, 200))

            if manager.health <= 0:
                self.excapetextCounter += 1
            if self.excapetextCounter > 0 and self.excapetextCounter < 101:
                win.blit(self.text2, (100, 200))
                win.blit (self.text3, (100, 250))


            manager.draw(win)


    def changer(self, character):
        if self.parkinglot:
            if character.x > 640 and character.y > 300:
                character.x = 20
                self.checkout = True
                self.parkinglot = False

        if self.checkout:
            if character.x < 20 and character.y > 300:
                character.x = 620
                self.checkout = False
                self.parkinglot = True
            if character.x > 650 and character.y > 300:
                character.x = 20
                self.manager1 = True
                self.checkout = False
                self.parkinglot = False

        if self.manager1:
            if character.x < 20 and character.y > 300:
                character.x = 620
                self.manager1 = False
                self.parkinglot = False
                self.checkout = True

    def stuffGrabber(self, win, keys, character, manager):
        self.stufftext = self.font.render(str(self.stuff) + '/20 STUFF', 1, (255, 255, 255))

        if manager.health <= 0:
            win.blit(self.stufftext, (500, 10))
            if self.stuff >= 20:
                self.stuff = 20

            if keys[pygame.K_e] and self.checkout:
                if character.x < 600 and character.x > 400 or character.x < 300 and character.x > 100:
                    self.stuff += 1

        if self.excapetextCounter > 101:
            self.policeCounter += 1
        if self.policeCounter > 300:
            print('no')




