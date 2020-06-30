import pygame
import Guns
pygame.init()

win = pygame.display.set_mode((700, 500))
pygame.display.set_caption('BANK ROBBER PRO')

clock = pygame.time.Clock()

music = pygame.mixer.music.load('images/music.mp3')
pygame.mixer.music.play(-1)

font = pygame.font.SysFont('comicsans', 50)


class player(object):
    walkRight = [pygame.transform.scale(pygame.image.load('images/character4t.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/character5t.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/character6t.png'), (40, 60))]

    walkLeft = [pygame.transform.scale(pygame.image.load('images/character10t.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/character11t.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/character12t.png'), (40, 60))]

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
        self.shoot = False
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


class BackgroundColor(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))



def redrawGameWindow():
    backgroundcolor.draw(win)
    character.draw(win)
    pistol.draw(win, character.x, character.y, character.left)
    pistol.shoot(win, character.x, character.y, character.left, character.shoot)
    pistol.bulletTracker(win)

    pygame.display.update()


backgroundcolor = BackgroundColor(0, 0, 700, 500, (100, 100, 100))
character = player(100, 420, 40, 60)
pistol = Guns.Pistol()
shootLoop = 0
shootCount = 0
run = True
while run:
    clock.tick(27)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    if shootLoop >= 0 and shootCount >= 1:
        shootLoop += 1
    if shootLoop > 20:
        shootLoop = 0
        shootCount = 0


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        shootCount += 1
        character.shoot = True
    else:
        character.shoot = False

    if keys[pygame.K_LEFT] and character.x > character.vel and character.dead == False:
        character.x -= character.vel
        character.left = True
        character.right = False
        character.standing = False
    elif keys[pygame.K_RIGHT] and character.x < 700 - character.width - character.vel and character.dead == False:
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