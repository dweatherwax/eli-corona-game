import pygame
import pickle
import os.path
import random

pygame.init()

win = pygame.display.set_mode((600, 600))
win.fill((255, 255, 255))

pygame.display.set_caption('DRAWER PRO')

music = pygame.mixer.music.load('images/music.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

font = pygame.font.SysFont('comicsans', 25)


class Grid(object):
    def __init__(self, width, height, color):
        self.width = width
        self.width1 = 600
        self.height = height
        self.height1 = 500
        self.height2 = 10
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (0, 100, self.width1, self.height2))
        pygame.draw.rect(win, self.color, (0, 150, self.width1, self.height2))
        pygame.draw.rect(win, self.color, (0, 200, self.width1, self.height2))
        pygame.draw.rect(win, self.color, (0, 250, self.width1, self.height2))
        pygame.draw.rect(win, self.color, (0, 300, self.width1, self.height2))
        pygame.draw.rect(win, self.color, (0, 350, self.width1, self.height2))
        pygame.draw.rect(win, self.color, (0, 400, self.width1, self.height2))
        pygame.draw.rect(win, self.color, (0, 450, self.width1, self.height2))
        pygame.draw.rect(win, self.color, (0, 500, self.width1, self.height2))
        pygame.draw.rect(win, self.color, (0, 550, self.width1, self.height2))
        pygame.draw.rect(win, self.color, (0, 100, self.width, self.height1))
        pygame.draw.rect(win, self.color, (50, 100, self.width, self.height1))
        pygame.draw.rect(win, self.color, (100, 100, self.width, self.height1))
        pygame.draw.rect(win, self.color, (150, 100, self.width, self.height1))
        pygame.draw.rect(win, self.color, (200, 100, self.width, self.height1))
        pygame.draw.rect(win, self.color, (250, 100, self.width, self.height1))
        pygame.draw.rect(win, self.color, (300, 100, self.width, self.height1))
        pygame.draw.rect(win, self.color, (350, 100, self.width, self.height1))
        pygame.draw.rect(win, self.color, (400, 100, self.width, self.height1))
        pygame.draw.rect(win, self.color, (450, 100, self.width, self.height1))
        pygame.draw.rect(win, self.color, (500, 100, self.width, self.height1))
        pygame.draw.rect(win, self.color, (550, 100, self.width, self.height1))


class Draw(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = colorselect.color

        self.mouseClickOne = 0
        self.mouseClickTwo = 0
        self.mouseClickThree = 0

    def draw(self, win, gridArray):
        self.color = colorselect.color

        xStart = button.x1
        yStart = button.y1

        for i in range(0, 10):
            xStart = button.x1
            for j in range(0, 10):
                pygame.draw.rect(win, gridArray[j][i], (xStart, yStart, self.width, self.height))
                xStart += 50
            yStart += 50


class Buttons(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.xMap = []
        for i in range(0,10):
            self.xMap.append(-1)
        for i in range(10,50):
            self.xMap.append(0)
        for i in range(50,60):
            self.xMap.append(-1)
        for i in range(60,100):
            self.xMap.append(1)
        for i in range(100,110):
            self.xMap.append(-1)
        for i in range(110,150):
            self.xMap.append(2)
        for i in range(150,160):
            self.xMap.append(-1)
        for i in range(160, 200):
            self.xMap.append(3)
        for i in range(200, 210):
            self.xMap.append(-1)
        for i in range(210, 250):
            self.xMap.append(4)
        for i in range(250, 260):
            self.xMap.append(-1)
        for i in range(260, 300):
            self.xMap.append(5)
        for i in range(300,310):
            self.xMap.append(-1)
        for i in range(310, 350):
            self.xMap.append(6)
        for i in range(350,360):
            self.xMap.append(-1)
        for i in range(360,400):
            self.xMap.append(7)
        for i in range(400, 410):
            self.xMap.append(-1)
        for i in range(410, 450):
            self.xMap.append(8)
        for i in range(450,460):
            self.xMap.append(-1)
        for i in range(460,500):
            self.xMap.append(9)

        self.yMap = []
        for i in range(0, 110):
            self.yMap.append(-1)
        for i in range(110, 150):
            self.yMap.append(0)
        for i in range(150, 160):
            self.yMap.append(-1)
        for i in range(160, 200):
            self.yMap.append(1)
        for i in range(200, 210):
            self.yMap.append(-1)
        for i in range(210, 250):
            self.yMap.append(2)
        for i in range(250, 260):
            self.yMap.append(-1)
        for i in range(260, 300):
            self.yMap.append(3)
        for i in range(300, 310):
            self.yMap.append(-1)
        for i in range(310, 350):
            self.yMap.append(4)
        for i in range(350, 360):
            self.yMap.append(-1)
        for i in range(360, 400):
            self.yMap.append(5)
        for i in range(400, 410):
            self.yMap.append(-1)
        for i in range(410, 450):
            self.yMap.append(6)
        for i in range(450, 460):
            self.yMap.append(-1)
        for i in range(460, 500):
            self.yMap.append(7)
        for i in range(500, 510):
            self.yMap.append(-1)
        for i in range(510, 550):
            self.yMap.append(8)
        for i in range(550, 560):
            self.yMap.append(-1)
        for i in range(560, 600):
            self.yMap.append(9)

        self.x1 = 10
        self.y1 = 110

class ColorSelect(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = (255, 0, 0)

        self.y1 = 110
        self.y2 = 160
        self.y3 = 210
        self.y4 = 260
        self.y5 = 310
        self.y6 = 360
        self.y7 = 410
        self.y8 = 460
        self.y9 = 510
        self.y10 = 560
        self.x = 560

        self.redColor = (255,0,0)
        self.orangeColor = (255, 100, 10)
        self.yellowColor = (255, 255, 0)
        self.greenColor = (0, 255, 0)
        self.blueColor = (0, 0, 255)
        self.purpleColor = (150, 0, 255)
        self.pinkColor = (255, 100, 180)
        self.brownColor = (100, 40, 0)
        self.blackColor = (50, 50, 50)
        self.whiteColor = (255, 255, 255)

        self.activeColor = self.redColor

    def draw(self, win, outline = None):
        pygame.draw.rect(win, (0, 0, 0), (510, 110, self.width, 500))
        pygame.draw.rect(win, (255, 0, 0), (560, 110, self.width, 40))
        pygame.draw.rect(win, (255, 100, 10), (560, 160, self.width, 40))
        pygame.draw.rect(win, (255, 255, 0), (560, 210, self.width, 40))
        pygame.draw.rect(win, (0, 255, 0), (560, 260, self.width, 40))
        pygame.draw.rect(win, (0, 0, 255), (560, 310, self.width, 40))
        pygame.draw.rect(win, (150, 0, 255), (560, 360, self.width, 40))
        pygame.draw.rect(win, (255, 100, 180), (560, 410, self.width, 40))
        pygame.draw.rect(win, (100, 40, 0), (560, 460, self.width, 40))
        pygame.draw.rect(win, (50, 50, 50), (560, 510, self.width, 40))


    def isOver111(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y1 and pos[1] < self.y1 + self.height:
                return True

        return False

    def isOver112(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y2 and pos[1] < self.y2 + self.height:
                return True

        return False

    def isOver113(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y3 and pos[1] < self.y3 + self.height:
                return True

        return False

    def isOver114(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y4 and pos[1] < self.y4 + self.height:
                return True

        return False

    def isOver115(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y5 and pos[1] < self.y5 + self.height:
                return True

        return False

    def isOver116(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y6 and pos[1] < self.y6 + self.height:
                return True

        return False

    def isOver117(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y7 and pos[1] < self.y7 + self.height:
                return True

        return False

    def isOver118(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y8 and pos[1] < self.y8 + self.height:
                return True

        return False

    def isOver119(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y9 and pos[1] < self.y9 + self.height:
                return True

        return False

    def isOver1110(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y10 and pos[1] < self.y10 + self.height:
                return True

        return False


class RestartButton(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.clickedTheButton = False
        self.timer = 0
        self.text = font.render('R', 1, (0, 0, 0))
        self.text1 = font.render('E', 1, (0, 0, 0))
        self.text2 = font.render('S', 1, (0, 0, 0))
        self.text3 = font.render('E', 1, (0, 0, 0))
        self.text4 = font.render('T', 1, (0, 0, 0))


    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        win.blit(self.text, (self.x + 28, self.y + 5))
        win.blit(self.text1, (self.x + 28, self.y + 20))
        win.blit(self.text2, (self.x + 28, self.y + 35))
        win.blit(self.text3, (self.x + 28, self.y + 50))
        win.blit(self.text4, (self.x + 28, self.y + 65))

    def reset(self):
        if self.clickedTheButton:
            for i in range(0, 10):
                for j in range(0, 10):
                    gridArray[i][j] = colorselect.whiteColor

    def isOverrestart(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


class SaveLoad(object):
    def __init__(self, width, height):
        self.x = 90

        self.width = width
        self.height = height

        self.y1 = 10
        self.y2 = 55

        self.color1 = (255, 100, 180)
        self.color2 = (255, 255, 0)

        self.text = font.render('S', 1, (0, 0, 0))
        self.text1 = font.render('A', 1, (0, 0, 0))
        self.text2 = font.render('V', 1, (0, 0, 0))
        self.text3 = font.render('E', 1, (0, 0, 0))

        self.text4 = font.render('L', 1, (0, 0, 0))
        self.text5 = font.render('O', 1, (0, 0, 0))
        self.text6 = font.render('A', 1, (0, 0, 0))
        self.text7 = font.render('D', 1, (0, 0, 0))


    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y1 - 2, self.width + 4, self.height + 4), 0)
            pygame.draw.rect(win, outline, (self.x - 2, self.y2 - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color1, (self.x, self.y1, self.width, self.height), 0)
        pygame.draw.rect(win, self.color2, (self.x, self.y2, self.width, self.height), 0)

        win.blit(self.text, (self.x + 10, self.y1 + 10))
        win.blit(self.text1, (self.x + 20, self.y1 + 10))
        win.blit(self.text2, (self.x + 30, self.y1 + 10))
        win.blit(self.text3, (self.x + 40, self.y1 + 10))

        win.blit(self.text4, (self.x + 5, self.y2 + 10))
        win.blit(self.text5, (self.x + 15, self.y2 + 10))
        win.blit(self.text6, (self.x + 30, self.y2 + 10))
        win.blit(self.text7, (self.x + 43, self.y2 + 10))


    def haveSavedGame(self):
        return os.path.exists("savedgame.obj")

    def loadSavedGame(self):
        return pickle.load(open("savedgame.obj", "rb"))

    def saveGame(self, gridArray):
        pickle.dump(gridArray, open("savedgame.obj", "wb"))

    def isOversave(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y1 and pos[1] < self.y1 + self.height:
                return True

        return False

    def isOverload(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y2 and pos[1] < self.y2 + self.height:
                return True

        return False


class Game(object):
    def __init__(self):
        self.Play = False

        self.color1 = (0, 0, 0)
        self.color2 = (0, 255, 0)
        self.color3 = (255, 0, 0)

        self.gameButtonx = 520
        self.gameButtony = 10
        self.gameButtonwidth = 70
        self.gameButtonheight = 80

        self.gameButtontext1 = font.render('P', 1, self.color1)
        self.gameButtontext2 = font.render('L', 1, self.color1)
        self.gameButtontext3 = font.render('A', 1, self.color1)
        self.gameButtontext4 = font.render('Y', 1, self.color1)

        self.gameButtontext5 = font.render('Q', 1, self.color1)
        self.gameButtontext6 = font.render('U', 1, self.color1)
        self.gameButtontext7 = font.render('I', 1, self.color1)
        self.gameButtontext8 = font.render('T', 1, self.color1)

        self.doneButtontext1 = font.render('D', 1, self.color1)
        self.doneButtontext2 = font.render('O', 1, self.color1)
        self.doneButtontext3 = font.render('N', 1, self.color1)
        self.doneButtontext4 = font.render('E', 1, self.color1)

        self.doneButtonx = 170
        self.doneButtony = 10
        self.doneButtonwidth = 70
        self.doneButtonheight = 80

        self.guess = ''
        self.trueGuess = ''
        self.guessCount = 0
        self.guessCounter = 0
        self.blank = pickle.load(open("blank.obj", "rb"))
        self.guessCounterFirst = 0

        self.done = False
        self.arraySelect = -1
        self.doneArray = None

        self.heartArray = pickle.load(open("heart.obj", "rb"))
        self.heartArrayCount = 0

        self.appleArray = pickle.load(open("apple.obj", "rb"))
        self.appleArrayCount = 0

        self.forkArray = pickle.load(open("fork.obj", "rb"))
        self.forkArrayCount = 0

        self.eightbyfivedoorArray = pickle.load(open("8x5 door.obj", "rb"))
        self.eightbyfivedoorArrayCount = 0

        self.fourbyfoursquareArray = pickle.load(open("4x4 square.obj", "rb"))
        self.fourbyfoursquareArrayCount = 0

    def drawGameButton(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.gameButtonx - 2,
                                            self.gameButtony - 2,
                                            self.gameButtonwidth + 4,
                                            self.gameButtonheight + 4), 0)

        pygame.draw.rect(win, self.color3, (self.gameButtonx,
                                            self.gameButtony,
                                            self.gameButtonwidth,
                                            self.gameButtonheight), 0)
        if self.Play == False:
            win.blit(self.gameButtontext1, (self.gameButtonx + 30, self.gameButtony + 10))
            win.blit(self.gameButtontext2, (self.gameButtonx + 30, self.gameButtony + 25))
            win.blit(self.gameButtontext3, (self.gameButtonx + 30, self.gameButtony + 40))
            win.blit(self.gameButtontext4, (self.gameButtonx + 30, self.gameButtony + 55))
        else:
            win.blit(self.gameButtontext5, (self.gameButtonx + 30, self.gameButtony + 10))
            win.blit(self.gameButtontext6, (self.gameButtonx + 30, self.gameButtony + 25))
            win.blit(self.gameButtontext7, (self.gameButtonx + 33, self.gameButtony + 40))
            win.blit(self.gameButtontext8, (self.gameButtonx + 30, self.gameButtony + 55))

    def drawDoneButton(self, win, outline=None):
        if self.Play:
            if outline:
                    pygame.draw.rect(win, outline, (self.doneButtonx - 2,
                                                    self.doneButtony - 2,
                                                    self.doneButtonwidth + 4,
                                                    self.doneButtonheight + 4), 0)

            pygame.draw.rect(win, self.color2, (self.doneButtonx,
                                                self.doneButtony,
                                                self.doneButtonwidth,
                                                self.doneButtonheight), 0)

            win.blit(self.doneButtontext1, (self.doneButtonx + 30, self.doneButtony + 10))
            win.blit(self.doneButtontext2, (self.doneButtonx + 30, self.doneButtony + 25))
            win.blit(self.doneButtontext3, (self.doneButtonx + 30, self.doneButtony + 40))
            win.blit(self.doneButtontext4, (self.doneButtonx + 30, self.doneButtony + 55))

    def Guesser(self, win):
        if self.guessCounter == 0:
            self.guessCounterFirst = random.randrange(200)
        #print(self.guessCounter)
        guessText = font.render('GUESS: ' + self.guess, 1, (0, 0, 0))

        if self.guessCounter < self.guessCounterFirst:
            self.guessCounter += 1
        if self.guessCounter == self.guessCounterFirst and self.guess != 'Nothing':
            self.guessCounter = 0
            self.guessCount = random.randrange(7)

        print(self.guessCount)

        if self.guessCount == 1:
            self.guess = 'GREAT WALL OF CHINA'
        elif self.guessCount == 2:
            self.guess = 'STAMPEDE'
        elif self.guessCount == 3:
            self.guess = 'NO IDEA'
        elif self.guessCount == 4:
            self.guess = 'CRAZY MONKEY'
        elif self.guessCount == 5:
            self.guess = 'UPSIDE DOWN ELEPHANT'
        elif self.guessCount == 6:
            self.guess = 'ROTTEN HAMBERGER'
        elif gridArray == self.blank:
            self.guess = 'Nothing'
        else:
            self.guess = 'NO IDEA'

        if self.Play and self.arraySelect > 0:
            win.blit(guessText, (250, 70))

    def Done(self):
        if self.Play == True:
            doneText = font.render('DRAW A: ' + self.trueGuess, 1, (0, 0, 0))
            win.blit(doneText, (250, 10))
        #if not self.done:
            #print(self.arraySelect)
        if self.doneArray == None:
            self.arraySelect = random.randrange(6)
        if self.arraySelect > 0 and self.arraySelect < 101:
            self.doneArray = True


        if self.arraySelect == 1:
            self.trueGuess = 'HEART'
            if gridArray == self.heartArray:
                print('yay')
                self.heartArrayCount = 1
                self.doneArray = None
                self.guess = self.trueGuess
            #if gridArray != self.heartArray and self.heartArrayCount == 0:
                #print('Aw')

        if self.arraySelect == 2:
            self.trueGuess = 'APPLE'
            if gridArray == self.appleArray:
                print('yay')
                self.appleArrayCount = 1
                self.doneArray = None
                self.guess = self.trueGuess
            if gridArray != self.appleArray and self.appleArrayCount == 0:
                print('Aw')

        if self.arraySelect == 3:
            self.trueGuess = 'FORK'
            if gridArray == self.forkArray:
                print('yay')
                self.forkArrayCount = 1
                self.doneArray = None
                self.guess = self.trueGuess
            if gridArray != self.forkArray and self.forkArrayCount == 0:
                print('Aw')

        if self.arraySelect == 4:
            self.trueGuess = '8x5 DOOR'
            if gridArray == self.eightbyfivedoorArray:
                print('yay')
                self.eightbyfivedoorArrayCount = 1
                self.doneArray = None
                self.guess = self.trueGuess
            if gridArray != self.eightbyfivedoorArray and self.eightbyfivedoorArrayCount == 0:
                print('Aw')

        if self.arraySelect == 5:
            self.trueGuess = '4x4 SQUARE'
            if gridArray == self.fourbyfoursquareArray:
                print('yay')
                self.fourbyfoursquareArrayCount = 1
                self.doneArray = None
                self.guess = self.trueGuess
            if gridArray != self.fourbyfoursquareArray and self.fourbyfoursquareArrayCount == 0:
                print('Aw')


    def isOverGameButton(self, pos):
        if pos[0] > self.gameButtonx and pos[0] < self.gameButtonx+ self.gameButtonwidth:
            if pos[1] > self.gameButtony and pos[1] < self.gameButtony + self.gameButtonheight:
                return True

        return False

    def isOverDoneButton(self, pos):
        if pos[0] > self.doneButtonx and pos[0] < self.doneButtonx+ self.doneButtonwidth:
            if pos[1] > self.doneButtony and pos[1] < self.doneButtony + self.doneButtonheight:
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
    backgroundColor.draw(win)
    grid.draw(win)
    colorselect.draw(win)
    draw.draw(win, gridArray)
    restartbutton.draw(win, (0, 0, 0))
    saveload.draw(win, (0, 0, 0))
    game.drawGameButton(win, (0, 0, 0))
    game.drawDoneButton(win, (0, 0, 0))
    game.Done()
    game.Guesser(win)
    restartbutton.reset()

    pygame.display.update()


gridArray = [[(255, 255, 255) for i in range(10)] for j in range(10)]
grid = Grid(10, 600, (0, 0, 0))
colorselect = ColorSelect(40, 40)
draw = Draw(40, 40)
button = Buttons(40, 40)
saveload = SaveLoad(60, 35)
restartbutton = RestartButton(10, 10, 70, 80, (0, 255, 0))
game = Game()
backgroundColor = BackgroundColor(0, 0, 700, 700, (255, 255, 255))
run = True
while run:
    clock.tick(27)


    if restartbutton.clickedTheButton:
        restartbutton.timer += 1
    if restartbutton.timer == 10:
        restartbutton.clickedTheButton = False
        restartbutton.timer = 0

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                if saveload.haveSavedGame():
                    gridArray = saveload.loadSavedGame()
            if event.key == pygame.K_s:
                saveload.saveGame(gridArray)

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()


    #111111111111111111111111111111111111111
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(event.type)
        xpos = -1
        ypos = -1
        print(pos)
        if pos[0] < 500:
            xpos = button.xMap[pos[0]]
        if pos[1] < 600:
            ypos = button.yMap[pos[1]]

        if ypos >= 0 and xpos >= 0:
            print(xpos, ypos)
            gridArray[xpos][ypos] = colorselect.activeColor



    if event.type == pygame.MOUSEBUTTONDOWN:
        if colorselect.isOver111(pos):
            colorselect.activeColor = colorselect.redColor

    if event.type == pygame.MOUSEBUTTONDOWN:
        if colorselect.isOver112(pos):
            colorselect.activeColor = colorselect.orangeColor

    if event.type == pygame.MOUSEBUTTONDOWN:
        if colorselect.isOver113(pos):
            colorselect.activeColor = colorselect.yellowColor

    if event.type == pygame.MOUSEBUTTONDOWN:
        if colorselect.isOver114(pos):
            colorselect.activeColor = colorselect.greenColor

    if event.type == pygame.MOUSEBUTTONDOWN:
        if colorselect.isOver115(pos):
            colorselect.activeColor = colorselect.blueColor

    if event.type == pygame.MOUSEBUTTONDOWN:
        if colorselect.isOver116(pos):
            colorselect.activeColor = colorselect.purpleColor

    if event.type == pygame.MOUSEBUTTONDOWN:
        if colorselect.isOver117(pos):
            colorselect.activeColor = colorselect.pinkColor

    if event.type == pygame.MOUSEBUTTONDOWN:
        if colorselect.isOver118(pos):
            colorselect.activeColor = colorselect.brownColor

    if event.type == pygame.MOUSEBUTTONDOWN:
        if colorselect.isOver119(pos):
            colorselect.activeColor = colorselect.blackColor

    if event.type == pygame.MOUSEBUTTONDOWN:
        if colorselect.isOver1110(pos):
            colorselect.activeColor = colorselect.whiteColor

    if event.type == pygame.MOUSEBUTTONDOWN:
        if restartbutton.isOverrestart(pos):
            restartbutton.clickedTheButton = True

    if event.type == pygame.MOUSEBUTTONDOWN:
        if saveload.isOversave(pos):
            saveload.saveGame(gridArray)

    if event.type == pygame.MOUSEBUTTONDOWN:
        if saveload.isOverload(pos):
            if saveload.haveSavedGame():
                gridArray = saveload.loadSavedGame()

    if event.type == pygame.MOUSEBUTTONDOWN:
        if game.isOverGameButton(pos):
            if game.Play == False:
                game.Play = True
                restartbutton.clickedTheButton = True

    if event.type == pygame.MOUSEBUTTONDOWN:
        if game.isOverDoneButton(pos):
            game.done = True
            restartbutton.clickedTheButton = True


    redrawGameWindow()

pygame.quit()