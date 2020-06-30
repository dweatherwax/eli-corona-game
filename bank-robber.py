import pygame
import Guns
import People
import Foodway
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


class Bullets(object):
    def __init__(self, x, y, radius, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.facing = facing
        self.vel = 30 * facing

    def move(self):
        self.x += self.vel


class StartScreen(object):
    def __init__(self, x, y, width , height):
        self.People = [pygame.transform.scale(pygame.image.load('images/character5t.png'), (100, 120)),
                       pygame.transform.scale(pygame.image.load('images/character11t.png'), (100, 120))]
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.Text = font.render('BANK ROBBER PRO', 1, (0, 0, 0))

        self.playbuttonx = 275
        self.playbuttony = 200
        self.playbuttonwidth = 150
        self.playbuttonheight = 70
        self.playbuttontext = font.render('PLAY', 1, (0, 0, 0))

        self.Play = False

    def draw(self, win, outline=None):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height))
        win.blit(self.Text, (175, 75))

        win.blit(self.People[0], (10, 170))
        win.blit(self.People[1], (590, 170))

        if outline:
            pygame.draw.rect(win, (0, 0, 0), (self.playbuttonx - 2,
                                              self.playbuttony - 2,
                                              self.playbuttonwidth + 4,
                                              self.playbuttonheight + 4), 0)

        pygame.draw.rect(win, (178, 208, 217), (self.playbuttonx,
                                                self.playbuttony,
                                                self.playbuttonwidth,
                                                self.playbuttonheight), 0)

        win.blit(self.playbuttontext, (self.playbuttonx + 31, self.playbuttony + 20))

    def isOverPlayButton(self, pos):
        if pos[0] > self.playbuttonx and pos[0] < self.playbuttonx + self.playbuttonwidth:
            if pos[1] > self.playbuttony and pos[1] < self.playbuttony + self.playbuttonheight:
                return True

        return False


class LevelSelect(object):
    def __init__(self):
        self.backgroundx = 0
        self.backgroundy = 0
        self.backgroundwidth = 700
        self.backgroundheight = 500

        self.Foodwayx = 10
        self.Foodwayy = 10
        self.Foodwaywidth = 200
        self.Foodwayheight = 200

        self.FoodwaySelected = False

    def draw(self, win, outline=None):
        pygame.draw.rect(win, (255, 255, 255), (self.backgroundx,
                                                self.backgroundy,
                                                self.backgroundwidth,
                                                self.backgroundheight))

        if outline:
            pygame.draw.rect(win, (0, 0, 0), (self.Foodwayx - 2,
                                              self.Foodwayy - 2,
                                              self.Foodwaywidth + 4,
                                              self.Foodwayheight + 4), 0)

        pygame.draw.rect(win, (0, 200, 0), (self.Foodwayx, self.Foodwayy, self.Foodwaywidth, self.Foodwayheight), 0)

    def isOverFoodWayButton(self, pos):
        if pos[0] > self.Foodwayx and pos[0] < self.Foodwayx + self.Foodwaywidth:
            if pos[1] > self.Foodwayy and pos[1] < self.Foodwayy + self.Foodwayheight:
                return True

        return False





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
    keys = pygame.key.get_pressed()

    if levelselect.FoodwaySelected == True:
        backgroundcolor.draw(win)
        foodway.draw(win, aya, oliver, manager)
        foodway.changer(character)
        foodway.stuffGrabber(win, keys, character, manager)

        character.draw(win)
        pistol.draw(win, character.x, character.y, character.left)
        pistol.shoot(win, character.x, character.y, character.left, character.shoot)
        pistol.bulletTracker(win)
        for bullet in bullets:
            bullet.move()

    if startscreen.Play == False:
        startscreen.draw(win, (0, 0, 0))
         
    if startscreen.Play == True and levelselect.FoodwaySelected == False:
        levelselect.draw(win, (0, 0, 0))

    pygame.display.update()


startscreen = StartScreen(0, 0, 700, 500)
levelselect = LevelSelect()
foodway = Foodway.Foodway()
backgroundcolor = BackgroundColor(0, 0, 700, 500, (100, 100, 100))
character = player(100, 420, 40, 60)
pistol = Guns.Pistol()
bullets = []
aya = People.Aya(110, 420, 40, 60)
oliver = People.Oliver(300, 420, 40, 60)
manager = People.Manager(600, 420, 40, 60)
shootLoop = 0
shootCount = 0
run = True

while run:
    clock.tick(27)



    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    if levelselect.FoodwaySelected == True:
        if shootLoop >= 0 and shootCount >= 1:
            shootLoop += 1
        if shootLoop > 20:
            shootLoop = 0
            shootCount = 0

        for bullet in bullets:
            if bullet.y - bullet.radius < manager.hitbox[1] + manager.hitbox[3] and bullet.y + bullet.radius > manager.hitbox[1]:
                if bullet.x + bullet.radius > manager.hitbox[0] and bullet.x - bullet.radius < manager.hitbox[0] + manager.hitbox[2]:
                    manager.hit()

        keys = pygame.key.get_pressed()


        if keys[pygame.K_SPACE] and shootLoop == 0:
            shootCount += 1
            character.shoot = True

            if character.left:
                facing = -1
            else:
                facing = 1

            bullets.append(Bullets(round(character.x + character.width // 2),
                                      round(character.y + character.height // 2),
                                      2,
                                      facing))

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

    if startscreen.Play == False:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if startscreen.isOverPlayButton(pos):
                startscreen.Play = True

    if startscreen.Play == True:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if levelselect.isOverFoodWayButton(pos):
               levelselect.FoodwaySelected = True
               foodway.parkinglot = True



    redrawGameWindow()


pygame.quit()