import pygame
import random
pygame.init()

win = pygame.display.set_mode((600, 600))

pygame.display.set_caption('SPACE INVADERS')

Clock = pygame.time.Clock()

music = pygame.mixer.music.load('images/music.mp3')
pygame.mixer.music.play(-1)

font = pygame.font.SysFont('comicsans', 20)


class SpaceShip(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 5
        self.color1 = (25, 25, 25)
        self.color2 = (100, 0, 0)
        self.color3 = (100, 100, 0)
        self.x2 = 520
        self.y2 = 570
        self.y3 = 530
        self.y4 = 490
        self.score = 0
        self.scoretext = font.render('Score: ' + str(self.score), 1, (255, 255, 255))
        self.lives = 4

    def draw(self, win):
        self.scoretext = font.render('Score: ' + str(self.score), 1, (255, 255, 255))
        win.blit(self.scoretext, (520, 10))
        if self.lives >= 1:
            pygame.draw.rect(win, self.color1, (self.x, self.y, 50, 10))
            pygame.draw.rect(win, self.color2, (self.x + 10, self.y - 10, 30, 10))
            pygame.draw.rect(win, self.color3, (self.x + 20, self.y - 20, 10, 10))
        if self.lives >= 2:
            pygame.draw.rect(win, self.color1, (self.x2, self.y2, 50, 10))
            pygame.draw.rect(win, self.color2, (self.x2 + 10, self.y2 - 10, 30, 10))
            pygame.draw.rect(win, self.color3, (self.x2 + 20, self.y2 - 20, 10, 10))
        if self.lives >= 3:
            pygame.draw.rect(win, self.color1, (self.x2, self.y3, 50, 10))
            pygame.draw.rect(win, self.color2, (self.x2 + 10, self.y3 - 10, 30, 10))
            pygame.draw.rect(win, self.color3, (self.x2 + 20, self.y3 - 20, 10, 10))
        if self.lives >= 4:
            pygame.draw.rect(win, self.color1, (self.x2, self.y4, 50, 10))
            pygame.draw.rect(win, self.color2, (self.x2 + 10, self.y4 - 10, 30, 10))
            pygame.draw.rect(win, self.color3, (self.x2 + 20, self.y4 - 20, 10, 10))


class Laser(object):
    def __init__(self, x, y, width, height, facing, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing = facing
        self.color = color
        self.vel = 10

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        self.y -= self.vel


class LittleAlien(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.color2 = (200, 0, 0)
        self.vel = 2
        self.hitbox = (self.x, self.y, 10, 10)

        self.left = False
        self.right = True

    def draw(self, win):
        self.move()
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, self.color2, (self.x - 2, self.y, 2, 10))
        pygame.draw.rect(win, self.color2, (self.x + 10, self.y, 2, 10))
        pygame.draw.rect(win, self.color2, (self.x, self.y - 2, 10, 2))
        pygame.draw.rect(win, self.color2, (self.x, self.y + 10, 10, 2))

    def move(self):
        if self.left:
            self.x -= self.vel
        if self.right:
            self.x += self.vel

        if self.x == 490:
            self.y += 100
            self.x = 490
            self.left = True
            self.right = False
        elif self.x == 0:
            self.y += 100
            self.x = 10
            self.left = False
            self.right = True

        self.hitbox = (self.x, self.y, 10, 10)


class UFO(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.color2 = (126, 195, 196)
        self.vel = 4
        self.moveability = 0
        self.hitbox = (self.x, self.y, 50, 50)

        self.superHeight = 10
        self.countCount = 0
        self.stopCount = 0

        self.powerupx = self.x
        self.powerupy = self.y + 30
        self.hitbox = (self.powerupx, self.powerupy, 30, 30)
        self.shoulddraw = False
        self.powerupCount = 0

        self.health = 5

    def draw(self, win):
        if self.health >= 1:
            self.beam(win)
            self.move()
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(win, self.color, (self.x + 7, self.y + 10, 36, self.height))
            pygame.draw.rect(win, self.color, (self.x + 7, self.y - 10, 36, self.height))
            pygame.draw.rect(win, self.color2, (self.x + 15, self.y, 20, self.height))

        if self.shoulddraw:
            if self.powerupy < 610:
                self.powerupy += 4
            pygame.draw.rect(win, (50, 50, 50), (self.powerupx, self.powerupy, 20, 20))
            pygame.draw.rect(win, (0, 100, 0), (self.powerupx - 5, self.powerupy, 5, 20))
            pygame.draw.rect(win, (0, 100, 0), (self.powerupx + 20, self.powerupy, 5, 20))
            pygame.draw.rect(win, (0, 100, 0), (self.powerupx, self.powerupy - 5, 20, 5))
            pygame.draw.rect(win, (0, 100, 0), (self.powerupx, self.powerupy + 20, 20, 5))

        self.hitbox = (self.x, self.y, 50, 50)


    def move(self):
        if self.x == spaceship.x:
            self.vel = 0
        elif (self.x != spaceship.x) and (self.countCount == 0):
            self.vel = 4
        if self.moveability != 53:
            self.moveability = random.randrange(100)

        if self.x >= 450:
            self.x = -100
            self.vel = 0

        if self.moveability == 53:
            self.x += self.vel
            self.moveability = 53
        else:
            self.x = -100

    def beam(self, win):
        if abs(self.x - spaceship.x) < 10:
            pygame.draw.rect(win, self.color2, (self.x + 15, self.y + 20, 20, self.superHeight))
            self.vel = 0
            if self.countCount >= 0:
                self.countCount += 1
                self.superHeight += 10
            if self.y + self.superHeight == spaceship.y:
                spaceship.lives -= 1
            if self.y + self.superHeight >= 600:
               self.vel = 4

        elif abs(self.x - spaceship.x) < 50:
            self.superHeight = 10
            self.vel = 4

    def powerup(self, win, shootLoopCount):
        print(self.powerupCount)
        if self.powerupCount >= 0 and self.powerupCount < 100:
            self.powerupCount += 1
        if self.powerupCount == 100:
            self.shoulddraw = False
            self.shootLoopCount = 5
            laser.width = 5
        if self.vel == 0:
            self.powerupx = self.x
        else:
            self.powerupx = 250

        self.shoulddraw = True





class BackgroundColor(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, (255, 255, 255), (500, 0, 10, 600))




def redrawGameWindow():
    bakcgroundcolor.draw(win)
    spaceship.draw(win)
    ufo.draw(win)
    for alien in littlealiens:
        alien.draw(win)

    for l in laserList:
        l.draw(win)

    pygame.display.update()

def createAliens():
    aliens = []

    for y in range(100, 200, 20):
        for x in range(100, 400, 20):
            aliens.append(LittleAlien(x, y, 10, 10, (25, 25, 25)))\

    return aliens

spaceship = SpaceShip(300, 500)
laserList = []
littlealiens = createAliens()
ufo = UFO(100, 100, 50, 10, (25, 25, 25))
bakcgroundcolor = BackgroundColor(0, 0, 600, 600, (0, 0, 0))
shootLoop = 0
shootLoopCount = 5
run = True
while run:
    Clock.tick(27)


    if shootLoop >= 0:
        shootLoop += 1
    if shootLoop == shootLoopCount:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    for alien in littlealiens:
        if alien.x > spaceship.x - 10 and alien.x < spaceship.x + 10:
            if alien.y > spaceship.y + 20:
                spaceship.lives -= 1


    for laser in laserList:
        for alien in littlealiens:
            if ((laser.y - laser.height) < (alien.hitbox[1] + alien.hitbox[3])) and ((laser.y + laser.height) > alien.hitbox[1]):
                if ((laser.x + laser.width) > alien.hitbox[0]) and ((laser.x - laser.width) < (alien.hitbox[0] + alien.hitbox[2])):
                    laserList.pop(laserList.index(laser))
                    littlealiens.pop(littlealiens.index(alien))
                    spaceship.score += 1
                    if len(littlealiens) == 0:
                        littlealiens = createAliens()
                    break


    for laser in laserList:
        if laser.y - laser.height < ufo.hitbox[1] + ufo.hitbox[3] and laser.y + laser.height > ufo.hitbox[1]:
            if laser.x + laser.width > ufo.hitbox[0] and laser.x - laser.width < ufo.hitbox[0] + ufo.hitbox[2]:
                ufo.vel = 0
                ufo.health -= 4
                ufo.powerup(win, shootLoopCount)

    if ufo.powerupx > spaceship.x - 10 and ufo.powerupx < spaceship.x + 50:
        if ufo.powerupy > spaceship.y - 50 and ufo.powerupy < spaceship.y + 10:
            ufo.shoulddraw = False
            shootLoopCount = 3
            ufo.powerupx = 1000


    if shootLoopCount == 3:
        for laser in laserList:
            laser.width = 10


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        laserList.append(Laser(round(spaceship.x + 50 // 2),
                           round(spaceship.y + 30 // 2),
                                                2,
                                                10,
                                                1,
                                                (255, 0, 0)))


    if keys[pygame.K_LEFT] and spaceship.x > spaceship.vel:
        spaceship.x -= spaceship.vel

    if keys[pygame.K_RIGHT] and spaceship.x < 500 - 50 - spaceship.vel:
        spaceship.x += spaceship.vel

    redrawGameWindow()

pygame.quit()
