import pygame
import random
pygame.init()

win = pygame.display.set_mode((850, 480))

pygame.display.set_caption('Zombie Attack')

background = pygame.image.load('images/bg.jpg')

clock = pygame.time.Clock()

music = pygame.mixer.music.load('images/music.mp3')
pygame.mixer.music.play(-1)

font = pygame.font.SysFont('comicsans', 50)


class player(object):
    walkRight = [pygame.transform.scale(pygame.image.load('images/character4.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/character5.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/character6.png'), (40, 60))]

    walkLeft = [pygame.transform.scale(pygame.image.load('images/character10.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/character11.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/character12.png'), (40, 60))]

    death = [pygame.transform.scale(pygame.image.load('images/character-death1.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/character-death2.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/character-death3.png'), (40, 60))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = True
        self.left = False
        self.right = False
        self.walkCount = 0
        self.deathCount = 0
        self.deathNumber = 0
        self.dead = False
        self.jumpCount = 10
        self.health = 100
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        if self.standing and self.deathNumber == 0:
            if self.right:
                win.blit(self.walkRight[1], (self.x, self.y))
            else:
                win.blit(self.walkLeft[1], (self.x, self.y))

        if self.deathNumber == 1:
            self.dead = True
            win.blit(self.death[self.deathCount // 10], (self.x, self.y))
            if self.deathCount < 20:
                self.deathCount += 1

        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (225, 0, 0), self.hitbox, 2)

    def hit(self):
        self.deathNumber = 1
        self.standing = True


class zombie(object):
    walkRight = [pygame.image.load('images/R1E.png'),
                 pygame.image.load('images/R2E.png'),
                 pygame.image.load('images/R3E.png'),
                 pygame.image.load('images/R4E.png'),
                 pygame.image.load('images/R5E.png'),
                 pygame.image.load('images/R6E.png'),
                 pygame.image.load('images/R7E.png'),
                 pygame.image.load('images/R8E.png'),
                 pygame.image.load('images/R9E.png'),
                 pygame.image.load('images/R10E.png'),
                 pygame.image.load('images/R11E.png')]
    walkLeft = [pygame.image.load('images/L1E.png'),
                pygame.image.load('images/L2E.png'),
                pygame.image.load('images/L3E.png'),
                pygame.image.load('images/L4E.png'),
                pygame.image.load('images/L5E.png'),
                pygame.image.load('images/L6E.png'),
                pygame.image.load('images/L7E.png'),
                pygame.image.load('images/L8E.png'),
                pygame.image.load('images/L9E.png'),
                pygame.image.load('images/L10E.png'),
                pygame.image.load('images/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.left = False
        self.right = False
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 50
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            pygame.draw.rect(win, (225, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (1 * (50 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(win, (225, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            self.left = False
            self.right = True

            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            self.left = True
            self.right = False

            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
            self.x = 900
            self.y = 900


class GunGun(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.gun = 'PISTOL'
        self.gunCount = 0
        self.bulletAmount = 1

    def guncounter(self):
        if self.gunCount == 0:
            self.gun = 'PISTOL'
            self.x = 300
            self.bulletAmount = 1
        if self.gunCount == 1:
            self.gun = 'TRIPLE SHOOTER'
            self.x = 200
            self.bulletAmount = 3

    def draw(self, win):
        gungun.guncounter()
        text = font.render('GUN: ' + self.gun, 1, self.color)
        win.blit(text, (self.x, self.y))

        pygame.display.update()


class Guntext(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.textCount = 0

    def draw(self, win):
        text = font.render('GUN ACQUIRED ' + gungun.gun, 1, (0, 0, 0))
        if self.textCount == 0:
            win.blit(text, (self.x, self.y))

        pygame.display.update()


class gun(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.visible = True

    def draw(self, win):
        if zombie.visible == False and self.visible == True:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))


class zombieBullet(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class characterBullet(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)




def redrawGameWindow():
    win.blit(background, (0, 0))
    gungun.draw(win)
    character.draw(win)
    zombie.draw(win)
    gun.draw(win)
    for z in zombieBullets:
        z.draw(win)
    for c in characterBullets:
        c.draw(win)

    pygame.display.update()


character = player(300, 410, 40, 60)
zombie = zombie(100, 410, 64, 64, 450)
gun = gun(425, 460, 50, 10, (0, 0, 0))
gungun = GunGun(300, 10, (0, 0, 0))
guntext = Guntext(150, 240)
zombieBullets = []
characterBullets = []
run = True
shootLoop = 1
gunnum = 0
while run:
    clock.tick(27)

    bulletnum = random.randrange(70)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    if gunnum == 0:
        if character.x > 425 and character.x < 475:
            if character.y > 400:
                if zombie.visible == False:
                    gungun.gunCount += 1
                    gun.visible = False
                    guntext.draw(win)

    if zombie.visible == False and gun.visible == False :
        if character.x < 425 or character.x > 475:
            gunnum += 1



    for bullet in zombieBullets:
        if bullet.y - bullet.radius < character.hitbox[1] + character.hitbox[3] and bullet.y + bullet.radius > character.hitbox[1]:
            if bullet.x + bullet.radius > character.hitbox[0] and bullet.x - bullet.radius < character.hitbox[0] + character.hitbox[2]:
                #hitSound.play()
                character.hit()
                zombieBullets.pop(zombieBullets.index(bullet))

        bullet.x += bullet.vel
        if bullet.x >= 850 or bullet.x <= 0:
            zombieBullets.pop(zombieBullets.index(bullet))

    if bulletnum == 37:
        if zombie.left:
            facing = -1
        else:
            facing = 1
        if len(zombieBullets) < 10:

            zombieBullets.append(zombieBullet(round(zombie.x + zombie.width //2),
                                      round(zombie.y + zombie.height //2),
                                      2,
                                      (0, 0, 0),
                                      facing))

    for bullet in characterBullets:
        if bullet.y - bullet.radius < zombie.hitbox[1] + zombie.hitbox[3] and bullet.y + bullet.radius > zombie.hitbox[1]:
            if bullet.x + bullet.radius > zombie.hitbox[0] and bullet.x - bullet.radius < zombie.hitbox[0] + zombie.hitbox[2]:
                #hitSound.play()
                zombie.hit()
                characterBullets.pop(characterBullets.index(bullet))

        bullet.x += bullet.vel
        if bullet.x >= 850 or bullet.x <= 0:
            characterBullets.pop(characterBullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        #bulletSound.play()
        if character.left:
            facing = -1
        else:
            facing = 1
        if len(characterBullets) < gungun.bulletAmount:
            print("added bullet")
            characterBullets.append(characterBullet(round(character.x + character.width //2),
                                      round(character.y + character.height //2),
                                      2,
                                      (0, 0, 0),
                                      facing))


    if keys[pygame.K_h]:
        zombie.health = 10

    if keys[pygame.K_LEFT] and character.x > character.vel and character.dead == False:
        character.x -= character.vel
        character.left = True
        character.right = False
        character.standing = False
    elif keys[pygame.K_RIGHT] and character.x < 850 - character.width - character.vel and character.dead == False:
        character.x += character.vel
        character.right = True
        character.left = False
        character.standing = False
    else:
        character.standing = True
        character.walkCount = 0

    if not character.isJump:
        if keys[pygame.K_UP] and character.dead == False:
            character.isJump = True
            character.right = False
            character.left = False
            character.walkCount = 0
    else:
        if character.jumpCount >= -10:
            neg = 1
            if character.jumpCount < 0:
                neg = -1
            character.y -= (character.jumpCount ** 2) * 0.5 * neg
            character.jumpCount -= 1
        else:
            character.isJump = False
            character.jumpCount = 10

    redrawGameWindow()

pygame.quit()
