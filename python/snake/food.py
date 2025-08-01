from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.penup()
        self.speed('fastest')
        self.shapesize(0.5,0.5)
        
    def random_location(self):
        xco=random.randint(-280,280)
        yco=random.randint(-280,280)
        self.goto(xco,yco)