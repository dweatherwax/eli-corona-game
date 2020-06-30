import pygame


class Aya(object):
    walkRight = [pygame.transform.scale(pygame.image.load('images/Aya1.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/Aya2.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/Aya3.png'), (40, 60))]

    walkLeft = [pygame.transform.scale(pygame.image.load('images/Aya4.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/Aya5.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/Aya6.png'), (40, 60))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0

        self.left = False
        self.right = True
        self.vel = 3

    def draw(self, win):
        self.path()
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if self.left:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

    def path(self):
        if self.x < 120:
            self.right = True
            self.left = False
        if self.x > 580:
            self.left = True
            self.right = False

        if self.right:
            self.x += self.vel
        if self.left:
            self.x -= self.vel


class Oliver(object):
    walkRight = [pygame.transform.scale(pygame.image.load('images/Oliver1.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/Oliver2.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/Oliver3.png'), (40, 60))]

    walkLeft = [pygame.transform.scale(pygame.image.load('images/Oliver4.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/Oliver5.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/Oliver6.png'), (40, 60))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.widht = width
        self.height = height

        self.left = True
        self.right = False
        self.walkCount = 0
        self.vel = 3

    def draw(self, win):
        self.path()
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if self.left:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

    def path(self):
        if self.left:
            self.x -= self.vel
        if self.right:
            self.x += self.vel

        if self.x < 60 and self.x > 50:
            self.right = True
            self.left = False
        if self.x > 540 and self.x < 560:
            self.left = True
            self.right = False


class Manager(object):
    walkRight = [pygame.transform.scale(pygame.image.load('images/Person4.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/Person5.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/Person6.png'), (40, 60))]

    walkLeft = [pygame.transform.scale(pygame.image.load('images/Person10.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/Person11.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/Person12.png'), (40, 60))]

    deathLeft = [pygame.transform.rotate(walkLeft[1], 45),
                 pygame.transform.rotate(walkLeft[1], 90)]

    deathRight = [pygame.transform.rotate(walkRight[1], 45),
                 pygame.transform.rotate(walkRight[1], 90)]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.left = True
        self.right = False
        self.walkCount = 0
        self.vel = 3

        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 2
        self.deathCounter = 0

    def draw(self, win):
        self.path()
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if self.left:
            if self.health > 0:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

        else:
            if self.health > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1



        if self.health <= 0:
            self.vel = 0
            self.deathCounter += 1
            if self.deathCounter < 10:
                win.blit(self.walkLeft[1], (self.x, self.y))
            if self.deathCounter >= 10 and self.deathCounter <= 15:
                self.y = 435
                win.blit(self.deathLeft[0], (self.x, self.y))
            if self.deathCounter > 15:
                self.y = 450
                win.blit(self.deathLeft[1], (self.x, self.y))
            if self.deathCounter >= 20:
                pygame.draw.rect(win, (200, 0, 0), (self.x + 25, self.y + 35, 10, 10))
            if self.deathCounter >= 35:
                pygame.draw.rect(win, (200, 0, 0), (self.x + 15, self.y + 35, 30, 10))
            if self.deathCounter > 50:
                pygame.draw.rect(win, (200, 0, 0), (self.x + 5, self.y + 35, 50, 10))
            if self.deathCounter >= 65:
                pygame.draw.rect(win, (200, 0, 0), (self.x - 5, self.y + 35, 70, 10))


    def path(self):
        if self.left:
            self.x -= self.vel
        if self.right:
            self.x += self.vel

        if self.x < 560 and self.x > 540:
            self.right = True
            self.left = False
        if self.x > 640 and self.x < 660:
            self.left = True
            self.right = False

    def hit(self):
        self.health -= 1



