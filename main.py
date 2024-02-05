# Final Project
# CS 111, Reckinger
# Recreation of Super Mario Bros Level One
# Aleena Mehmood
# Theme: Get Mario to save princess peach by collecting at least 1,000 points. 
# References:
# C:\Users\aleen\Downloads\references.docx 

import turtle
import random

global coin
coins = 00
global score
score = 0 
global TotalScore
TotalScore = 0
global character
global notStart
global notSelected
global notNext

def checkpos():
  global score
  global TotalScore
  if (mario.distance(coin.xcor(), coin.ycor()) < 30):
    coin.hideturtle()
    coin.goto(random.randint(-200, 200), random.randint(-130,-100))
    coin.showturtle()

    score += 1
    textScore.clear()
    textScore.write('x '+str(score), False, align='center', font=('Verdana', 20, 'italic'))
    
    TotalScore += 100
    textTotalScore.clear()
    textTotalScore.write(str(TotalScore), False, align='center', font=('Verdana', 20, 'italic'))




def left():
  mario.setheading(180)
  mario.forward(10)
  checkpos()
  

def right():
  mario.setheading(0)
  mario.forward(10)
  checkpos()

def upUnder():
  mario.setheading(90)
  mario.forward(10)
  checkpos()

def downUnder():
  mario.setheading(270)
  mario.forward(10)
  checkpos()
  
  

def jump():
  if mario.condition == 'ready':
    mario.dy = 17
    mario.condition = 'notReady'
  checkpos()


def leftJump():
  mario.setheading(180)
  mario.forward(3)
  if mario.condition == 'ready':
    mario.dy = 17
    mario.condition = 'notReady'
  checkpos()

def rightJump():
  mario.setheading(0)
  mario.forward(3)
  if mario.condition == 'ready':
    mario.dy = 17
    mario.condition = 'notReady'
  checkpos()

def start(x,y):
  global notStart
  notStart = False

#creates an invisable line to check if the character is at the end of the screen.
def screenEnd():
  invisLine = turtle.Turtle()
  invisLine.speed(0)
  invisLine.pensize(4)
  invisLine.color('white')
  invisLine.penup()
  invisLine.goto(SCREEN_LIMIT, -400)
  invisLine.pendown()
  invisLine.goto(SCREEN_LIMIT,400)
  invisLine.penup()
  invisLine.hideturtle() #comment out to show the limit line

# def coordinateCheck():
#   x = mario.xcor()
#   y = mario.ycor()
#   if (mario.distance(invisLine.xcor(), invisLine.ycor()) < 30):
#     nextScreen = True
#     s.clearscreen()
#     return nextScreen 


def go(x,y):
  global notNext
  notNext = False


######################################################
###############  ALL SCREENS  ########################
######################################################

#text shown on top of screen, applies on all game screens
def screentext():
  text = turtle.Turtle()
  text.penup()
  text.hideturtle()
  text.speed(0)
  text.goto(-400,250)
  text.color('white smoke')
  text.write('MARIO', False, align='center', font=('Verdana', 20, 'italic'))

  text.goto(100,250)
  text.color('white smoke')
  text.write('WORLD', False, align='center', font=('Verdana', 20, 'italic'))

  text.goto(100,220)
  text.color('white smoke')
  text.write('1-1', False, align='center', font=('Verdana', 20, 'italic'))

  text.goto(400,250)
  text.color('white smoke')
  text.write('TIME', False, align='center', font=('Verdana', 20, 'italic'))

def load_rules():
  file = open('rules.txt')
  list = []
  for line in file:
      list.append(line)
  return list
  
list_rules = load_rules()

#repeated screen for start menu and game screen one.
def screen1():
  mountain = turtle.Turtle()
  turtle.addshape('mountainbig.gif')
  mountain.shape('mountainbig.gif')
  mountain.speed(0)
  mountain.penup()
  mountain.goto(-350,-200)

  mountainMini = turtle.Turtle()
  turtle.addshape('mountainsmall.gif')
  mountainMini.shape('mountainsmall.gif')
  mountainMini.speed(0)
  mountainMini.penup()
  mountainMini.goto(435,-250)

  bush = turtle.Turtle()
  turtle.addshape('bush.gif')
  bush.shape('bush.gif')
  bush.speed(0)
  bush.penup()
  bush.goto(320,-250)

  coinscore = turtle.Turtle()
  turtle.addshape('coinscore.gif')
  coinscore.shape('coinscore.gif')
  coinscore.speed(0)
  coinscore.penup()
  coinscore.goto(-260,260)

  floor = turtle.Turtle()
  turtle.addshape('floorfull.gif')
  floor.shape('floorfull.gif')
  floor.speed(0)
  floor.penup()
  floor.goto(0,-290)


def screen2():
  bush = turtle.Turtle()
  turtle.addshape('bush.gif')
  bush.shape('bush.gif')
  bush.speed(0)
  bush.penup()
  bush.goto(300,-250)

  mountainMini = turtle.Turtle()
  turtle.addshape('mountainsmall.gif')
  mountainMini.shape('mountainsmall.gif')
  mountainMini.speed(0)
  mountainMini.penup()
  mountainMini.goto(-200,-250)

  cloud = turtle.Turtle()
  turtle.addshape('cloud.gif')
  cloud.shape('cloud.gif')
  cloud.speed(0)
  cloud.penup()
  cloud.goto(250,150)

  cloudMini = turtle.Turtle()
  turtle.addshape('cloudsmall.gif')
  cloudMini.shape('cloudsmall.gif')
  cloudMini.speed(0)
  cloudMini.penup()
  cloudMini.goto(-350,100)

  coinscore = turtle.Turtle()
  turtle.addshape('coinscore.gif')
  coinscore.shape('coinscore.gif')
  coinscore.speed(0)
  coinscore.penup()
  coinscore.goto(-260,260)

  tubeUP = turtle.Turtle()
  turtle.addshape('tubeUP.gif')
  tubeUP.shape('tubeUP.gif')
  tubeUP.speed(0)
  tubeUP.penup()
  tubeUP.goto(420,-230)

  floor = turtle.Turtle()
  turtle.addshape('floorfull.gif')
  floor.shape('floorfull.gif')
  floor.speed(0)
  floor.penup()
  floor.goto(0,-290)


def screen3():
  s.clearscreen()
  s.bgcolor("cornflower blue")
  s.tracer(0)
  screentext3 = screentext()

  bush = turtle.Turtle()
  turtle.addshape('bush.gif')
  bush.shape('bush.gif')
  bush.speed(0)
  bush.penup()
  bush.goto(-150,-250)

  mountain = turtle.Turtle()
  turtle.addshape('mountainbig.gif')
  mountain.shape('mountainbig.gif')
  mountain.speed(0)
  mountain.penup()
  mountain.goto(-350,-200)

  cloudMini = turtle.Turtle()
  turtle.addshape('cloudsmall.gif')
  cloudMini.shape('cloudsmall.gif')
  cloudMini.speed(0)
  cloudMini.penup()
  cloudMini.goto(350,100)

  coinscore = turtle.Turtle()
  turtle.addshape('coinscore.gif')
  coinscore.shape('coinscore.gif')
  coinscore.speed(0)
  coinscore.penup()
  coinscore.goto(-260,260)

  floor = turtle.Turtle()
  turtle.addshape('floorfull.gif')
  floor.shape('floorfull.gif')
  floor.speed(0)
  floor.penup()
  floor.goto(0,-290)

  tubeUP = turtle.Turtle()
  turtle.addshape('tubeUP.gif')
  tubeUP.shape('tubeUP.gif')
  tubeUP.speed(0)
  tubeUP.penup()
  tubeUP.goto(430,-290)

  textScore = turtle.Turtle()
  textScore.penup()
  textScore.hideturtle()
  textScore.speed(0)
  textScore.goto(-200,250)
  textScore.color('white smoke')
  textScore.write('x '+str(score), False, align='center', font=('Verdana', 20, 'italic'))

  textTotalScore = turtle.Turtle()
  textTotalScore.penup()
  textTotalScore.hideturtle()
  textTotalScore.speed(0)
  textTotalScore.goto(-400,220)
  textTotalScore.color('white smoke')
  textTotalScore.write(str(TotalScore), False, align='center', font=('Verdana', 20, 'italic'))

  mario = turtle.Turtle()
  turtle.addshape('mario.gif')
  mario.shape('mario.gif')
  mario.speed(0)
  mario.penup()
  mario.width = 84
  mario.height = 55
  mario.dx = 0
  mario.dy = 0
  mario.condition = 'ready' #changing condition to ensure user cannot make mario continously jump. while inside of jump function, user cannot press space again.
  mario.goto(-350, GROUND + mario.height / 2)

  coin = turtle.Turtle()
  turtle.addshape('coin.gif')
  coin.shape('coin.gif')
  coin.speed(0)
  coin.penup()
  coin.goto(0,-100)

def screen4():
  screentext4 = screentext()

  coinscore = turtle.Turtle()
  turtle.addshape('coinscore.gif')
  coinscore.shape('coinscore.gif')
  coinscore.speed(0)
  coinscore.penup()
  coinscore.goto(-260,260)


  coral = turtle.Turtle()
  turtle.addshape('coral.gif')
  coral.shape('coral.gif')
  coral.speed(0)
  coral.penup()
  coral.goto(-100,-250)

  fish = turtle.Turtle()
  turtle.addshape('fish.gif')
  fish.shape('fish.gif')
  fish.speed(0)
  fish.penup()
  fish.goto(250,0)

  underfloor = turtle.Turtle()
  turtle.addshape('underFloor.gif')
  underfloor.shape('underFloor.gif')
  underfloor.speed(0)
  underfloor.penup()
  underfloor.goto(0,-290)


  tubeSIDE = turtle.Turtle()
  turtle.addshape('tubeSIDE.gif')
  tubeSIDE.shape('tubeSIDE.gif')
  tubeSIDE.speed(0)
  tubeSIDE.penup()
  tubeSIDE.goto(-450,170)
  tubeSIDE.hideturtle()



def bufferScreen():
  s = turtle.Screen()
  s.bgcolor("blue")
  bush.hideturtle()
  cloud.hideturtle()
  cloudMini.hideturtle()
  mountainMini.hideturtle()
  tubeUP.hideturtle()
  floor.hideturtle()
  screen4()
  mario.goto(-350, GROUND + mario.height / 2)
  s.ontimer(bufferScreen1, 10000)

def bufferScreen1():
  s = turtle.Screen()
  s.bgcolor("cornflower blue")

  mario.goto(-350, GROUND + mario.height / 2)
  coin.goto(0,-200)
  

  cloud = turtle.Turtle()
  turtle.addshape('cloud.gif')
  cloud.shape('cloud.gif')
  cloud.speed(0)
  cloud.penup()
  cloud.goto(250,0)


  castle = turtle.Turtle()
  turtle.addshape('castle.gif')
  castle.shape('castle.gif')
  castle.speed(0)
  castle.penup()
  castle.goto(0,-75)

  bowser = turtle.Turtle()
  turtle.addshape('bowser.gif')
  bowser.shape('bowser.gif')
  bowser.speed(0)
  bowser.penup()
  bowser.goto(300,-165)

  floor = turtle.Turtle()
  turtle.addshape('floorfull.gif')
  floor.shape('floorfull.gif')
  floor.speed(0)
  floor.penup()
  floor.goto(0,-287)

  s.ontimer(endscreen, 4000)

def endscreen():
  s.clearscreen()
  s.bgcolor("sea green")
  s.tracer(0)

  marioVbowser = turtle.Turtle()
  turtle.addshape('marioVbowser.gif')
  marioVbowser.shape('marioVbowser.gif')
  marioVbowser.speed(0)
  marioVbowser.penup()
  marioVbowser.goto(200,0)

  text = turtle.Turtle()
  text.penup()
  text.hideturtle()
  text.speed(0)
  text.color('lavender')
  text.goto(-300,0)
  text.write('FINAL SCORE:', False, align='center', font=('Verdana', 25, 'bold'))

  text.goto(-295,-50)
  text.write(str(TotalScore), False, align='center', font=('Verdana', 25, 'bold'))

  text.goto(-200,200)
  text.write("Mario has reached the castle!", False, align='center', font=('Verdana', 20, 'bold'))

  s.ontimer(winorlose, 3000)

def winorlose():
  s.clearscreen()
  s.tracer(0)
  if TotalScore >= 1000:
    s.bgcolor("hot pink")
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.speed(0)
    text.color('light cyan')
    text.goto(0,150)
    text.write('Congrats! You saved Princess Peach!', False, align='center', font=('Verdana', 25, 'bold'))

    marioandpeach = turtle.Turtle()
    turtle.addshape('marioandpeach.gif')
    marioandpeach.shape('marioandpeach.gif')
    marioandpeach.speed(0)
    marioandpeach.penup()
    marioandpeach.goto(0,-100)
  else: 
    s.bgcolor("red")
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.speed(0)
    text.color('light cyan')
    text.goto(0,150)
    text.write('Oh no! Princess Peach has been captured!', False, align='center', font=('Verdana', 25, 'bold'))

    peachandbowser = turtle.Turtle()
    turtle.addshape('peachandbowser.gif')
    peachandbowser.shape('peachandbowser.gif')
    peachandbowser.speed(0)
    peachandbowser.penup()
    peachandbowser.goto(0,-100)

  



######################################################
###############  START SCREEN  #######################
######################################################
s = turtle.Screen()
s.bgcolor("dodger blue") 
screenStart = screen1()
screenStart = screentext()

textScore = turtle.Turtle()
textScore.penup()
textScore.hideturtle()
textScore.speed(0)
textScore.goto(-200,250)
textScore.color('white smoke')
textScore.write('x 00', False, align='center', font=('Verdana', 20, 'italic'))

textTotalScore = turtle.Turtle()
textTotalScore.penup()
textTotalScore.hideturtle()
textTotalScore.speed(0)
textTotalScore.goto(-400,220)
textTotalScore.color('white smoke')
textTotalScore.write('000000', False, align='center', font=('Verdana', 20, 'italic'))

#turtles only shown on start screen
button = turtle.Turtle()
turtle.addshape('start.gif')
button.shape('start.gif')
button.speed(0)
button.penup()
button.goto(0,-170)

logo = turtle.Turtle()
turtle.addshape('logo.gif')
logo.shape('logo.gif')
logo.speed(0)
logo.penup()
logo.goto(0,35)

s.update()

notStart = True
while notStart:
  button.onclick(start)

s.clearscreen()

######################################################
###############  SCREEN ONE  ########################
######################################################
s = turtle.Screen()
s.bgcolor("dodger blue")
#s.tracer(0)
screen1 = screen1()
screentext1 = screentext()

textScore = turtle.Turtle()
textScore.penup()
textScore.hideturtle()
textScore.speed(0)
textScore.goto(-200,250)
textScore.color('white smoke')
textScore.write('x 00', False, align='center', font=('Verdana', 20, 'italic'))

textTotalScore = turtle.Turtle()
textTotalScore.penup()
textTotalScore.hideturtle()
textTotalScore.speed(0)
textTotalScore.goto(-400,220)
textTotalScore.color('white smoke')
textTotalScore.write('000000', False, align='center', font=('Verdana', 20, 'italic'))

peach = turtle.Turtle()
turtle.addshape('peach.gif')
peach.shape('peach.gif')
peach.speed(0)
peach.penup()
peach.goto(0,-170)

text = turtle.Turtle()
text.penup()
text.hideturtle()
text.speed(0)
x = 0
y = 50
for line in list_rules:
  text.color('deep pink')
  text.goto(x,y)
  text.write(line, False, align='center', font=('Verdana', 20, 'bold'))
  y -= 50


next = turtle.Turtle()
turtle.addshape('next.gif')
next.shape('next.gif')
next.speed(0)
next.penup()
next.goto(375,-200)

notNext = True
while notNext:
  next.onclick(go)

s.clearscreen()


#y coordinate of the top of the brick floor, sets the ground level that mario walks on
GROUND = -255

######################################################
###############  SCREEN TWO  ########################
######################################################
s = turtle.Screen()
s.bgcolor("dodger blue")
s.tracer(0)
screentext2 = screentext()

textScore = turtle.Turtle()
textScore.penup()
textScore.hideturtle()
textScore.speed(0)
textScore.goto(-200,250)
textScore.color('white smoke')
textScore.write('x 00', False, align='center', font=('Verdana', 20, 'italic'))

textTotalScore = turtle.Turtle()
textTotalScore.penup()
textTotalScore.hideturtle()
textTotalScore.speed(0)
textTotalScore.goto(-400,220)
textTotalScore.color('white smoke')
textTotalScore.write('000000', False, align='center', font=('Verdana', 20, 'italic'))

bush = turtle.Turtle()
turtle.addshape('bush.gif')
bush.shape('bush.gif')
bush.speed(0)
bush.penup()
bush.goto(300,-250)

mountainMini = turtle.Turtle()
turtle.addshape('mountainsmall.gif')
mountainMini.shape('mountainsmall.gif')
mountainMini.speed(0)
mountainMini.penup()
mountainMini.goto(-200,-250)

cloud = turtle.Turtle()
turtle.addshape('cloud.gif')
cloud.shape('cloud.gif')
cloud.speed(0)
cloud.penup()
cloud.goto(250,150)

cloudMini = turtle.Turtle()
turtle.addshape('cloudsmall.gif')
cloudMini.shape('cloudsmall.gif')
cloudMini.speed(0)
cloudMini.penup()
cloudMini.goto(-350,100)

coinscore = turtle.Turtle()
turtle.addshape('coinscore.gif')
coinscore.shape('coinscore.gif')
coinscore.speed(0)
coinscore.penup()
coinscore.goto(-260,260)

tubeUP = turtle.Turtle()
turtle.addshape('tubeUP.gif')
tubeUP.shape('tubeUP.gif')
tubeUP.speed(0)
tubeUP.penup()
tubeUP.goto(420,-230)

floor = turtle.Turtle()
turtle.addshape('floorfull.gif')
floor.shape('floorfull.gif')
floor.speed(0)
floor.penup()
floor.goto(0,-290)


mario = turtle.Turtle()
turtle.addshape('mario.gif')
mario.shape('mario.gif')
mario.speed(0)
mario.penup()
mario.width = 84
mario.height = 55
mario.dx = 0
mario.dy = 0
mario.condition = 'ready' #changing condition to ensure user cannot make mario continously jump. while inside of jump function, user cannot press space again.
mario.goto(-350, GROUND + mario.height / 2)

coin = turtle.Turtle()
turtle.addshape('coin.gif')
coin.shape('coin.gif')
coin.speed(0)
coin.penup()
coin.goto(0,-100)


######################################################
###############  MOVE MARIO  ########################
######################################################

#x coordinate of the end of the screen, used to check if character is at end of screen to pan to next screen.
SCREEN_LIMIT = 485


#brings mario back down to ensure he does not go into space.
GRAVITY = -0.8

s.listen()
s.onkey(left, "Left")
s.onkey(right, "Right")
s.onkey(jump, "space")
s.onkey(leftJump, "Down")
s.onkey(rightJump, "Up")

s.ontimer(bufferScreen, 10000)

jump = True
while jump:
  mario.dy += GRAVITY

  y = mario.ycor()
  y = y + mario.dy
  mario.sety(y)


  if mario.ycor() < GROUND + mario.height / 2:
    mario.sety(GROUND + mario.height / 2)
    mario.dy = 0
    mario.condition = 'ready'

  screenEnd()

  checkpos()

  

  s.update()









turtle.mainloop() 