from turtle import Turtle,Screen,colormode
from random import random,choices,randint

t=Turtle()
t.shape('turtle')
# Draw a dashed line
# for _ in range(10): # Draw 10 dashes
#     t.pendown()    # Pen down to draw a dash
#     t.forward(10)  # Move forward to create the dash
#     t.penup()      # Pen up to create a gap
#     t.forward(5)   # Move forward to create the gap


# for _ in range(1):
#     t.forward(40)
#     t.right(120)
#     t.forward(40)
#     t.right(120)
#     t.forward(40)
#     t.right(120)
#     t.forward(40)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(40)
    
#     t.right(72)
#     t.forward(40)
#     t.right(72)
#     t.forward(40)
#     t.right(72)
#     t.forward(40)
#     t.right(72)
#     t.forward(40)
#     t.right(72)

#     t.forward(40)
#     t.right(60)
#     t.forward(40)
#     t.right(60)
#     t.forward(40)
#     t.right(60)
#     t.forward(40)
#     t.right(60)
#     t.forward(40)
#     t.right(60)
#     t.forward(40)
#     t.right(60)
# colors=['DeepPink','Cyan','Red','Yellow','Orange','Blue']    
# t.pensize(10)

colormode(255)
def randomColor():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)

    return (r,g,b)

# for i in range(100):
#     t.color(randomColor())    
#     steps = int(random() * 100)
#     angle = int(90)
#     t.right(angle)
#     t.forward(steps)
#     t.speed(5)

t.speed('fastest')
for _ in range(100):
    t.color(randomColor()) 
    t.circle(120, 360)  # draw a semicircle
    current_heading=t.heading()
    t.setheading(current_heading+10)


screen=Screen()
screen.exitonclick()