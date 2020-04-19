import pygame
pygame.init()

win = pygame.display.set_mode((850, 480))

pygame.display.set_caption('Covid 19')

background = pygame.image.load('images/bg.jpg')

clock = pygame.time.Clock()

music = pygame.mixer.music.load('images/music.mp3')
pygame.mixer.music.play(-1)

font = pygame.font.SysFont('comicsans', 25)


class player(object):
    walkRight = [pygame.transform.scale(pygame.image.load('images/character4.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/character5.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/character6.png'), (40, 60))]

    walkLeft = [pygame.transform.scale(pygame.image.load('images/character10.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/character11.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/character12.png'), (40, 60))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.health = 100
        self.healthiness = 100
        self.bodytemp = 98.6
        self.symptoms = 0
        self.happiness = 50
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if not (self.standing):
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(self.walkRight[1], (self.x, self.y))
            else:
                win.blit(self.walkLeft[1], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (225, 0, 0), self.hitbox, 2)


class Guy(object):
    walkRight = [pygame.transform.scale(pygame.image.load('images/person4.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/person5.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/person6.png'), (40, 60))]

    walkLeft = [pygame.transform.scale(pygame.image.load('images/person10.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/person11.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/person12.png'), (40, 60))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.left = False
        self.right = True
        self.walkCount = 0
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.sickness = 0
        self.guyCount = 0
        self.drawable = True

    def draw(self, win):
        if self.drawable == True:
            self.move()
            self.right = True
            self.guyCount += 1

            if self.guyCount == 3:
                self.walkCount += 1
                self.guyCount = 0
            #else:
            #    if self.right:
            #        win.blit(self.walkRight[1], (self.x, self.y))
            if self.right:
                win.blit(self.walkRight[self.walkCount % 3], (self.x, self.y))
            else:
                win.blit(self.walkLeft[self.walkCount % 3], (self.x, self.y))

            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        else:
            if character.x > self.x:
                win.blit(self.walkRight[1], (self.x, self.y))
            else:
                win.blit(self.walkLeft[1], (self.x, self.y))

    def move(self):
        self.x += self.vel

    def hit(self):
        self.drawable = False
        self.vel = 0
        #win.blit(self.walkRight[1], (self.x, self.y))



def drawText():
    healthtext = font.render('HP: ' + str(character.health), 1, (0, 0, 0))
    healthinesstext = font.render('HEALTHINESS: ' + str(character.healthiness) + '%', 1, (0, 0, 0))
    bodytemptext1 = font.render('BODY TEMP: ', 1, (0, 0, 0))
    bodytemtext2 = font.render(str(character.bodytemp), 1, bodytempcolor)
    symptomstext = font.render('SYMPTOMS: ' + str(character.symptoms) + '/4', 1, (0, 0, 0))
    happinesstext1 = font.render('HAPPINESS: ', 1, (0, 0, 0))
    happinesstext2 = font.render(str(character.happiness) + '/100', 1, happinesscolor)
    win.blit(happinesstext1, (10, 98))
    win.blit(happinesstext2, (120, 98))
    win.blit(bodytemptext1, (10, 76))
    win.blit(bodytemtext2, (120, 76))
    win.blit(symptomstext, (10, 54))
    win.blit(healthinesstext, (10, 32))
    win.blit(healthtext, (10, 10))

    pygame.display.update()


def redrawGameWindow():
    win.blit(background, (0,0))
    character.draw(win)
    person.draw(win)

    pygame.display.update()


character = player(300, 410, 40, 60)
person = Guy(10, 410, 40, 60)
happinesscolor = ()
bodytempcolor = (0, 200, 0)
run = True
while run:
    clock.tick(27)


    if character.hitbox[1] < person.hitbox[1] + person.hitbox[3] and character.hitbox[1] + character.hitbox[3] > person.hitbox[1]:
            if character.hitbox[0] + character.hitbox[2] > person.hitbox[0] and character.hitbox[0] < person.hitbox[0] + person.hitbox[2]:
                person.hit()

    if person.x > character.x:
        person.right = True
    else:
        person.right = False


    if character.happiness >= 25 and character.happiness <= 75:
        happinesscolor = (225, 225, 0)
    if character.happiness <= 24:
        happinesscolor = (255, 0, 0)
    if character.happiness >= 76:
        happinesscolor = (0, 200, 0)

    if character.bodytemp >= 98.6 and character.bodytemp <= 100:
        bodytempcolor = (0, 200, 0)
    else:
        bodytempcolor = (0, 200, 0)
    if character.bodytemp >=100.1:
       bodytempcolor = (255, 0, 0)
    else:
       bodytempcolor = (0, 200, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    print(keys[pygame.K_LEFT])

    if keys[pygame.K_LEFT] and character.x > character.vel:
        character.x -= character.vel
        character.left = True
        character.right = False
        character.standing = False
    elif keys[pygame.K_RIGHT] and character.x < 850 - character.width - character.vel:
        character.x += character.vel
        character.right = True
        character.left = False
        character.standing = False
    else:
        character.standing = True
        character.walkCount = 0

    if not (character.isJump):
        if keys[pygame.K_UP]:
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
    drawText()


pygame.quit()


