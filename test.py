print("what is your name") #name request
name = input()
if name == 'tommy' or name == 'aaron':
    print("you are mean")
else:
    print("Hello,", name)

print("lets play a game") #number game
print("pick a number")
num1 = input()
print("pick another number")
num2 = input()
print("now lets multiply them")
SUM = int(num1) * int(num2)
print(SUM)

print("lets play another game") #multiplication game
print("what is 7x8=")
answer = input()

if int(answer) == 56: # if statement for multiplication game
    print("correct")
elif int(answer) < 56:
    print("incorrect")
else:
    print("incorrect")

print("want to play another game?") #asking if yo want to play another game
hopefully = input()

if hopefully == 'yes': #if statement for asking if yo want to play a game
    print("yay")
else:
    print("you are mean")

print("what does 4x5=") #another number game
print("what does 20x20=")
print("please answer both with a single comma between them")
answer2 = input()

if answer2 == '20,400':
    print("correct")
else:
    print("incorrect")

for x in range(0, 100, 1): #a for loop
    print(x)

loop = True

while loop:                               #a while loop that requests a password
    password = ("mudgie is the best")
    typed_password = input("password: ")
    if typed_password.lower() == password:
        print("mudgie is awesome")
        break

ski_mountains = ['Big Sky', 'Cannon', 'Bretton Woods', 'Loon']
print(ski_mountains)
ski_mountains.append('Waterville Valley')
print(ski_mountains)
ski_mountains[1:1] = 'Alta'
print(ski_mountains)
Black = (0, 0, 0)
Cannon = ('Awesome', 'Cool')

for mountian in ski_mountains:
    if mountian == 'Cannon':
        print("Cannon is the best ski mountain")
    else:
        print("Not cannon")

def myname():
    print('Mudgie')

myname()
username = input('Username: ')
try:
    usernamenum = int(username)
    print(usernamenum)
except:
    print('invalid username')



print("level 2")
print("please read our priviacy policy: dslkflkdsjflkdsjfldsjfksdjflsdjflsdjfksdjflsdjfl")
print("now please enter your name")
name2 = input()
print("now enter your age")
age = input()
print("now we can begin the game")

print("please create a password for your account")
print('please include the number one in your password')

password2 = input()
print("please enter your password")


loop2 = True

while loop2:
    print("password:")
    typed_password2 = input()
    if typed_password2 == password2:
        print("welcome,", name2)
        #print("now we can play")
        #print("the first game is called guess the number")
        #print("in this game you will guess a number between 1 and 10 and hope you guess correct!")
        #print("lets play, I'm thinking of a number...")
       # print("Guess:")
       # guess = input()
       # if int(guess) == 9:
         #   print("yay you got it right!")
       # else:
          #  print("aaw, maybe next time : (")
       # print("lets play another game of guess the number")
       # print("I'm thinking of a number")
       # print("Guess: ")
       # guess2 = input()
       # if int(guess2) == 4:
        #    print("yay you got it right")
       # else:
        #    print("aaw, maybe next time : (")
      #  print("now you can choose different games")
      #  print("here's a list of all the options:")
      #  print("Guess The Number")
       # print("Counter")
       # print("Math Facts-Multiplication")
       # print("Math Facts-Division")
      #  print("Math Facts-Addition")
      #  print("Math Facts-Subtraction")
       # print("Math Facts-Mixed")
       # print("Math Facts-Multiplication and Division")
       # print("Math Facts-Addition and Subtraction")
       # print("Math Facts-Greater Than and less Than")
        print("now you can choose different games")
        print("here's a list of all the options:")
        print("Guess The Number")
        print("Counter")
        print("Math Facts-Multiplication")
        print("Math Facts-Division")
        print("Math Facts-Addition")
        print("Math Facts-Subtraction")
        print("Math Facts-Mixed")
        print("Math Facts-Multiplication and Division")
        print("Math Facts-Addition and Subtraction")
        print("Math Facts-Greater Than and less Than")

        while loop2:


            print("Pick a game")
            gamechoice = input()
            if gamechoice == 'Counter':
                print("Welcome to counter")
                print("Please choose a number")
                print("Number: ")
                num1_1 = input()
                print("Number 2: ")
                num1_2 = input()
                print("Number 3: ")
                num1_3 = input()
                print("now lets count")
                for x in range(int(num1_1), int(num1_2), int(num1_3)):
                   print(x)
            elif gamechoice == 'Guess The Number':
                print("Welcome to Guess The Number")
                print("to play this game you guess the number that I am thinking of between 1 and 10")
                print("I'm thinking of a number...")
                print("Guess: ")
                guess3 = input()
                if int(guess3) == 7:
                    print("Yay you got it right")
                else:
                    print("Aaw maybe next time")
            elif gamechoice == 'Math Facts-Multiplication':
                if int(age) >= 8:
                    print("Welcome to Math Facts Multiplication Edition")
                    print("To play you just enter the answer to the facts and hope you are correct")
                    print("lets play!")
                    print("3x4=")
                    mathfactsmanswer1 = input()
                    if int(mathfactsmanswer1) == 12:
                        print("Correct")
                    else:
                        print("Sorry but the correct answer is 12")
                    print("6x8=")
                    mathfactsmanswer2 = input()
                    if int(mathfactsmanswer2) == 48:
                        print("Correct")
                    else:
                        print("Sorry but the correct answer is 48")
                    print("7x8=")
                    mathfactsmanswer3 = input()
                    if int(mathfactsmanswer3) == 56:
                        print("Correct")
                    else:
                        print("Sorry but the correct answer is 56")
                    print("9x12=")
                    mathfactsmanswer4 = input()
                    if int(mathfactsmanswer4) == 108:
                        print("Correct")
                    else:
                        print("Sorry but the correct answer is 108")
                    print("8x5=")
                    mathfactsmanswer5 = input()
                    if int(mathfactsmanswer5) == 40:
                        print("Correct")
                    else:
                        print("Sorry but the correct answer is 40")
                    print("3x0=")
                    mathfactsmanswer6 = input()
                    if int(mathfactsmanswer6) == 0:
                        print("Correct")
                    else:
                        print("Sorry but the correct answer is 40")
                    print("4x9=")
                    mathfactsmanswer7 = input()
                    if int(mathfactsmanswer7) == 36:
                        print("Correct")
                    else:
                        print("sorry but the correct answer is 36")
                    print("6x9=")
                    mathfactsmanswer8 = input()
                    if int(mathfactsmanswer8) == 54:
                        print("Correct")
                    else:
                        print("Sorry but hte correct answer is 54")
                    print("12x12=")
                    mathfactsmanswer9 = input()
                    if int(mathfactsmanswer9) == 144:
                        print("Correct")
                    else:
                        print("Sorry but the correct answer is 144")
                    print("4x8=")
                    mathfactsmanswer10 = input()
                    if int(mathfactsmanswer10) == 32:
                        print("Correct")
                    else:
                        while int(mathfactsmanswer10) != 32:
                            print("4x8=")
                            mathfactsmanswer10ex = input()
                            if int(mathfactsmanswer10ex) != 32:
                                print("Try again")
                            else:
                                print("Correct")
                                break

                    print("Thank you for playing Math Facts Multiplication Edition")
                elif gamechoice == 'Math Facts-Division':
                    if int(age) >= 8:
                        print("Welcome to Math Facts Division Edition")
                        print("To play just enter the answer to the facts and hope you are correct")
                        print("Lets play!")








        





