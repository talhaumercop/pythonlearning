from turtle import Turtle

class Ball:
    def __init__(self):
        self.ball=Turtle()
        self.ball.color('green')
        self.ball.shape('circle')
        self.ball.penup()
        self.x=10
        self.y=10
    def move(self):
        new_x=self.ball.xcor()+self.x
        new_y=self.ball.ycor()+self.y
        self.ball.goto(new_x,new_y)

    def bounce_Y(self):
        self.y*=-1
    def bounce_X(self):
        self.x*=-1