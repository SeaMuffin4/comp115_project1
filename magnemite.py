import turtle
import random

drwscrn = turtle.Screen()
# drwscrn.setup(width=1200, height=600)
drwscrn.screensize(750, 750) 
#background
drwscrn.bgcolor("lightsky blue")

bg = turtle.Turtle()
bg.speed(70)
bg.color('wheat')
bg.fillcolor('wheat')
bg.penup()
bg.goto(0, -40)
bg.pendown()
bg.begin_fill()
for i in range (2):
    bg.forward(750)
    bg.right(90)
    bg.forward(750)
    bg.right(90)
    bg.forward(750)

bg.end_fill()

bg.goto(400, -40)

bg.color('black')
bg.fillcolor('darkslategrey')
bg.begin_fill()
bg.setheading(135)
bg.forward(200)
bg.left(85)
bg.forward(80)
bg.right(100)
bg.forward(280)
bg.left(120)
bg.forward(180)
bg.right(120)
bg.forward(400)
bg.goto(-500,-40)
bg.goto(400, -40)
bg.end_fill()







###

def magnemite():
    al = turtle.Turtle()
    al.speed(40)

    def draw_magnet ():
        #magnet 1 
        al.fillcolor("dimgrey")
        al.begin_fill()
        al.forward(100)
        al.circle(45, 180)
        al.forward(100)
        al.right(90)
        al.forward(30)
        al.right(90)
        al.forward(120)
        al.circle(-75, 180)
        al.forward(120)
        al.right(90)
        al.forward(30)
        al.end_fill()

        al.fillcolor('blue')
        al.begin_fill()
        al.left(90)
        for i in range (4):
            al.forward(30)
            al.left(90)
        al.end_fill()

        al.penup()
        al.right(90)
        al.forward(120)
        al.pendown()

        al.fillcolor('red')
        al.begin_fill()
        for i in range (4):
            al.left(90)
            al.forward(30)
        al.end_fill()

        #print(al.pos())

    al.penup()

    #screw top

    al.goto(-15, 165)
    al.begin_fill()
    al.fillcolor('grey')
    for i in range(2):
        al.forward(30)
        print(al.pos())
        al.left(90)
        al.forward(80)
        al.left(90)

    al.end_fill()

    al.penup()

    al.goto(-15, 165)
    al.pendown()
    al.pensize(4)
    for i in range (11):
        al.setheading(15)
        al.forward(30)
        al.penup()
        al.setheading(0)
        al.back(29)
        al.pendown()


    #top semicircle
    al.penup()
    al.goto(-45,245)
    al.pensize(2)
    al.pendown()
    al.begin_fill()
    al.setheading(0)
    al.forward(90)
    al.left(90)
    al.circle(45,180)
    al.end_fill()

    al.penup()


    # main circle and magnets
    al.pensize(2)
    al.goto(0,0)
    al.pendown()
    al.setheading(0)
    al.fillcolor('darkgrey')
    al.begin_fill()
    al.circle(100)
    al.end_fill()

    al.penup()
    al.forward(-295)
    al.left(90)
    al.forward(55)
    al.right(90)
    al.pendown()
    #print(al.pos())
    draw_magnet()
    al.penup()
    al.goto(295, 145)
    al.pendown()
    al.left(90)
    draw_magnet()
    al.penup()

    al.goto(0,40)
    al.left(90)
    al.pendown()
    al.fillcolor('white')
    al.begin_fill()
    al.circle(60)
    al.end_fill()
    al.penup()

    al.fillcolor('black')
    al.begin_fill()
    al.goto(0,90)
    al.circle(10)
    al.end_fill()
    #end main body

    def front_screw():
        al.color('black')
        al.fillcolor('grey')
        al.begin_fill()
        al.circle(25)
        al.end_fill()
        al.penup()
        al.left(90)
        al.forward(10)
        al.pendown()
        al.setheading(0)
        al.fillcolor('black')
        al.begin_fill()
        for i in range (4):
            al.forward(5)
            al.left(90)
            al.forward(10)
            al.right(90)
            al.forward(10)
            al.left(90)
            al.forward(5)
        al.end_fill()

    #front screws

    al.goto(50, -10)
    al.pendown()
    front_screw()
    al.penup()
    al.goto(-50, -10)
    al.pendown()
    front_screw()


    al.penup()
    al.goto(-1000, - 1000)
magnemite()

drwscrn.exitonclick()