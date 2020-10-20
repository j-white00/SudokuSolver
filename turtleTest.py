import turtle
import random
myPen = turtle.Turtle()
bgPen = turtle.Turtle()

def drawBG(pen):
    pen.color('grey')
    pen.speed(0)
    pen.width(5)
    for i in range(50):
        pen.penup()
        randX = random.randrange(-450, 450)
        randY = random.randrange(-450, 450)
        pen.setpos(randX, randY)
        pen.begin_fill()
        pen.pendown()
        pen.circle(random.randrange(10, 150))
        pen.end_fill()

def drawBox(pen):
    pen.speed()
    pen.penup()
    pen.color('black', 'grey')
    pen.width(6)
    pen.setposition(-225,225)
    pen.pendown()
    pen.fillcolor('white')
    pen.begin_fill()
    for i in range(4):
        pen.forward(450)
        pen.right(90)
    pen.end_fill()
    pen.width(2)
    pen.right(90)
    pen.forward(50)
    pen.left(90)
    for i in range(4):
        if(i == 1):
            pen.width(4)
        pen.forward(450)
        pen.width(2)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
        if(i==2):
            pen.width(4)
        pen.forward(450)
        pen.width(2)
        pen.left(90)
        pen.forward(50)
        pen.left(90)
    pen.forward(50)
    pen.left(90)
    for i in range(4):
        if(i == 1):
            pen.width(4)
        pen.forward(450)
        pen.width(2)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
        if(i==2):
            pen.width(4)
        pen.forward(450)
        pen.width(2)
        pen.left(90)
        pen.forward(50)
        pen.left(90)


drawBG(bgPen)

drawBox(myPen)



