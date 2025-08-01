from turtle import Turtle

class Bar:
    def __init__(self,position):
        self.bar=Turtle('square')
        self.bar.speed('fastest')
        self.bar.penup()
        self.bar.goto(position)
        self.bar.color('white')
        self.bar.shapesize(4,1)

    def eventListen_UP(self):
        self.bar.goto(x=self.bar.xcor(),y=self.bar.ycor()+20)
    def eventListen_DOWN(self):
        self.bar.goto(x=self.bar.xcor(),y=self.bar.ycor()-20)