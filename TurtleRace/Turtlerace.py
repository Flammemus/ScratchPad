from multiprocessing.connection import wait
import turtle
from random import randint, random

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle Race")
wn.screensize(500, 500)

winline = 235

backstage = turtle.Turtle()
amund = turtle.Turtle()
carlAnton = turtle.Turtle()
herjus = turtle.Turtle()
tidemann = turtle.Turtle()
sigurd = turtle.Turtle()

backstage.speed(0)
backstage.penup()
backstage.hideturtle()

amund.speed(0)
amund.color("purple")
amund.shape("turtle")
amund.penup()

carlAnton.speed(0)
carlAnton.color("lime")
carlAnton.shape("turtle")
carlAnton.penup()

herjus.speed(0)
herjus.color("orange")
herjus.shape("turtle")
herjus.penup()

tidemann.speed(0)
tidemann.color("red")
tidemann.shape("turtle")
tidemann.penup()

sigurd.speed(0)
sigurd.color("black")
sigurd.shape("turtle")
sigurd.penup()

def startline():
    backstage.goto(-250, 100)
    backstage.pendown()
    backstage.setheading(-90)
    backstage.forward(200)

def startpos():
    amund.goto(-250, 40)
    carlAnton.goto(-250, 0)
    herjus.goto(-250, -40)
    tidemann.goto(-250, 80)
    sigurd.goto(-250, -80)
    amund.speed(10)
    carlAnton.speed(10)
    herjus.speed(10)
    tidemann.speed(10)
    sigurd.speed(10)

def finishline():
    backstage.penup()
    backstage.goto(250, 100)
    backstage.pendown()
    backstage.setheading(-90)
    backstage.forward(200)

def winningtext():
    backstage.penup()
    if winnerofrace == "Amund vinner!":
        backstage.goto(-130, 180)
        backstage.write(winnerofrace, font=("Arial", 40, "normal"))
    elif winnerofrace == "Carl Anton vinner!":
        backstage.goto(-160, 180)
        backstage.write(winnerofrace, font=("Arial", 40, "normal"))
    elif winnerofrace == "Herjus vinner!":
        backstage.goto(-135, 180)
        backstage.write(winnerofrace, font=("Arial", 40, "normal"))
    elif winnerofrace == "Tidemann vinner!":
        backstage.goto(-150, 180)
        backstage.write(winnerofrace, font=("Arial", 40, "normal"))
    elif winnerofrace == "Sigurd vinner!":
        backstage.goto(-135, 180)
        backstage.write(winnerofrace, font=("Arial", 40, "normal"))

def contesters():
    backstage.penup()
    backstage.goto(-348, 70)
    backstage.write("Tidemann", font=("Arial", 20, "normal"))
    backstage.goto(-325, 30)
    backstage.write("Amund", font=("Arial", 20, "normal"))
    backstage.goto(-356, -10)
    backstage.write("Carl Anton", font=("Arial", 20, "normal"))
    backstage.goto(-320, -50)
    backstage.write("Herjus", font=("Arial", 20, "normal"))
    backstage.goto(-320, -90)
    backstage.write("Sigurd", font=("Arial", 20, "normal"))

startline()
finishline()
startpos()
contesters()

amund.pendown()
carlAnton.pendown()
herjus.pendown()
tidemann.pendown()
sigurd.pendown()

racetofinish = True
while racetofinish:

    amund.forward(randint(1, 10))
    carlAnton.forward(randint(1, 10))
    herjus.forward(randint(1, 10))
    tidemann.forward(randint(1, 10))
    sigurd.forward(randint(1, 10))

    if amund.xcor() or carlAnton.xcor() or herjus.xcor() or tidemann.xcor() or sigurd.xcor() > winline:
        if amund.xcor() > winline:
            racetofinish = False
            winnerofrace = "Amund vinner!"
        elif carlAnton.xcor() > winline:
            racetofinish = False
            winnerofrace = "Carl Anton vinner!"
        elif herjus.xcor() > winline:
            racetofinish = False
            winnerofrace = "Herjus vinner!"
        elif tidemann.xcor() > winline:
            racetofinish = False
            winnerofrace = "Tidemann vinner!"
        elif sigurd.xcor() > winline:
            racetofinish = False
            winnerofrace = "Sigurd vinner!"

winningtext()


turtle.mainloop()