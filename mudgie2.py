import pygame
import random
pygame.init()

win = pygame.display.set_mode((1500, 480))

pygame.display.set_caption('Covid 19')

background = pygame.transform.scale(pygame.image.load('images/bg.jpg'), (1500, 500))
background2 = pygame.transform.scale(pygame.image.load('images/simpsons-background.png'), (4902, 480))

clock = pygame.time.Clock()

music = pygame.mixer.music.load('images/music.mp3')
pygame.mixer.music.play(-1)

font = pygame.font.SysFont('comicsans', 25)

keys = pygame.key.get_pressed()


class player(object):
    walkRight = [pygame.transform.scale(pygame.image.load('images/character4t.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/character5t.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/character6t.png'), (40, 60))]

    walkLeft = [pygame.transform.scale(pygame.image.load('images/character10t.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/character11t.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/character12t.png'), (40, 60))]

    walkUp = [pygame.transform.scale(pygame.image.load('images/character1t.png'), (40, 60)),
              pygame.transform.scale(pygame.image.load('images/character2t.png'), (40, 60)),
              pygame.transform.scale(pygame.image.load('images/character3t.png'), (40, 60))]

    walkDown = [pygame.transform.scale(pygame.image.load('images/character7.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/character8.png'), (40, 60)),
                pygame.transform.scale(pygame.image.load('images/character9.png'), (40, 60))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = True
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.jumpCount = 10
        self.health = 100
        self.healthiness = 100
        self.bodytemp = 98.6
        self.symptoms = 0
        self.happiness = 50
        self.money = 50
        self.sicknessChance = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 9:
            self.walkCount = 0

        print(self.walkCount)
        if self.standing and self.vel >= 0:
                if self.up:
                    win.blit(self.walkUp[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.down:
                    win.blit(self.walkDown[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(self.walkRight[1], (self.x, self.y))
                else:
                    win.blit(self.walkLeft[1], (self.x, self.y))
        if not self.standing and self.vel > 0:
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (225, 0, 0), self.hitbox, 2)


class Guy(object):
    walkRight = [pygame.transform.scale(pygame.image.load('images/person4t.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/person5t.png'), (40, 60)),
                 pygame.transform.scale(pygame.image.load('images/person6t.png'), (40, 60))]

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
        if talk.drawStop == 1:
            if talk.optionACounter >= 50 or talk.optionCCounter >= 50 or talk.optionCACounter >= 50 or talk.optionB == True:
                self.drawable = True
                self.vel = 3
        else:
            self.drawable = False
            self.vel = 0


class Talk(object):
    def __init__(self, color):
        self.color = color
        self.drawOptions = -1
        self.drawStop = 0
        self.optionSelected = False

        self.optionB = False

        self.optionA = False
        self.optionACounter = 0

        self.optionC = False
        self.optionCCounter = 0

        self.optionCA = False
        self.optionCACounter = 0

        self.text = font.render('OPTIONS: ', 1, self.color)
        self.text1 = font.render('A. TALK', 1, self.color)
        self.text2 = font.render('B. WALK AWAY', 1, self.color)
        self.text3 = font.render('C. COUGH ON', 1, self.color)
        self.text4 = font.render('BLAH   BLAH', 1, self.color)
        self.text5 = font.render('COUGH  COUGH', 1, self.color)
        self.text6 = font.render("YOU AREN'T SICK CAN'T COUGH", 1, self.color)

    def setDisplayText(self):
        if not self.optionSelected and self.drawStop == 0:
            self.drawOptions = 0

    def selectOptionA(self):
        self.optionA = True
        self.drawOptions = 1
        self.drawStop = 1
        self.optionSelected = True

    def selectOptionB(self):
        self.optionB = True
        self.drawOptions = 1
        self.drawStop = 1
        self.optionSelected = True

    def selectOptionC(self):
        self.optionC = True
        self.drawOptions = 1
        self.drawStop = 1
        self.optionSelected = True

    def selectOptionCA(self):
        self.optionCA = True
        self.drawOptions = 1
        self.drawStop = 1
        self.optionSelected = True

    def clearOptionSelected(self):
        self.optionSelected = False

    def draw(self, win, x, y):

        if self.drawOptions == 0:
            win.blit(self.text, (x, y - 75))
            win.blit(self.text1, (x + 5, y - 55))
            win.blit(self.text2, (x + 5, y - 40))
            win.blit(self.text3, (x + 5, y - 25))

        if self.optionA and self.optionACounter < 50:
            win.blit(self.text4, (x, y - 20))
            self.optionACounter += 1
        elif self.optionACounter == 1000:
            self.optionA = False
            self.optionACounter = 0

        if self.optionC and self.optionCCounter < 50:
            win.blit(self.text5, (x, y - 20))
            self.optionCCounter += 1
        elif self.optionCCounter == 1000:
            self.optionC = False
            self.optionCCounter = 0

        if self.optionCA and self.optionCACounter < 50:
            win.blit(self.text6, (x, y - 20))
            self.optionCACounter += 1
        elif self.optionCACounter == 1000:
            self.optionCA = False
            self.optionCACounter = 0



def drawText():
    healthtext = font.render('HP: ' + str(character.health), 1, (0, 0, 0))
    healthinesstext = font.render('HEALTHINESS: ' + str(character.healthiness) + '%', 1, (0, 0, 0))
    bodytemptext1 = font.render('BODY TEMP: ', 1, (0, 0, 0))
    bodytemtext2 = font.render(str(character.bodytemp), 1, bodytempcolor)
    symptomstext = font.render('SYMPTOMS: ' + str(character.symptoms) + '/4', 1, (0, 0, 0))
    happinesstext1 = font.render('HAPPINESS: ', 1, (0, 0, 0))
    happinesstext2 = font.render(str(character.happiness) + '/100', 1, happinesscolor)
    moneytext = font.render('DOLLARS: ' + '$' + str(character.money), 1, (0, 0, 0))
    hospitaltext = font.render('HOSPITAL', 1, (0, 0, 0))
    housetext = font.render('HOUSE', 1, (0, 0, 0))
    officetext = font.render('OFFICE', 1, (0, 0, 0))
    win.blit(officetext, (200, 200))
    win.blit(housetext, (800, 200))
    win.blit(hospitaltext, (1350, 200))
    win.blit(moneytext, (10, 120))
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
    win.blit(background2, (-2800, 0))
    character.draw(win)
    person.draw(win)
    talk.draw(win, person.x, person.y)

    pygame.display.update()


character = player(300, 410, 40, 60)
person = Guy(10, 410, 40, 60)
talk = Talk((255, 255, 255))
happinesscolor = ()
bodytempcolor = (0, 200, 0)
run = True

while run:
    clock.tick(27)


    if character.hitbox[1] < person.hitbox[1] + person.hitbox[3] and character.hitbox[1] + character.hitbox[3] > person.hitbox[1]:
        if character.hitbox[0] + character.hitbox[2] > person.hitbox[0] and character.hitbox[0] < person.hitbox[0] + person.hitbox[2]:
            character.vel = 0
            person.hit()
            talk.setDisplayText()

            if keys[pygame.K_a]:
                character.happiness += 25
                talk.selectOptionA()
            if keys[pygame.K_b]:
                character.happiness -= 25
                talk.selectOptionB()
            if keys[pygame.K_c]:
                if character.symptoms > 0:
                    talk.selectOptionC()
                else:
                    talk.selectOptionCA()

            if talk.drawStop == 1:
                character.vel = 5
        else:
            talk.clearOptionSelected()
            character.vel = 5


    if character.x > 200 and character.x < 220 and character.y == 350:
        character.vel = 0
    else:
        character.vel = 5

    if talk.optionA == True:
        character.sicknessChance = random.randrange(300)
    if character.sicknessChance == 57:
        character.symptoms = 1


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

    if character.happiness >= 100:
        character.happiness = 100
    if character.happiness <= 0:
        character.happiness = 0

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

    if keys[pygame.K_UP] and character.x > 200 and character.x < 220 and character.y > 350:
        character.y -= character.vel
        character.left = False
        character.right = False
        character.down = False
        character.up = True
        character.standing = False

    if keys[pygame.K_LEFT] and character.x > character.vel:
        character.x -= character.vel
        character.left = True
        character.right = False
        character.standing = False
    elif keys[pygame.K_RIGHT] and character.x < 1500 - character.width - character.vel:
        character.x += character.vel
        character.right = True
        character.left = False
        character.standing = False
    elif keys[pygame.K_UP] or keys[pygame.K_DOWN]:
        character.standing = True
    else:
        character.standing = True
        character.walkCount = 0

    if not (character.isJump):
        if keys[pygame.K_SPACE]:
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


