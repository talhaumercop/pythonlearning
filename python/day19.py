from turtle import Turtle,Screen,clearscreen

t=Turtle()

def keyeventsW():
    t.forward(10)
def keyeventsS():
    t.backward(10)
def keyeventsA():
    t.right(25)
def keyeventsD():
    t.left(25)
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen=Screen()
screen.listen()
screen.onkey(key='w',fun=keyeventsW)
screen.onkey(key='s',fun=keyeventsS)
screen.onkey(key='a',fun=keyeventsA)
screen.onkey(key='d',fun=keyeventsD)
screen.onkey(key='c',fun=clear)

screen.bgcolor("orange")
screen.exitonclick()