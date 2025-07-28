import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('paint.jpg', 6)

number=6
all_color=[]
for i in range(number):
    first_color=colors[i]
    rgb = first_color.rgb # e.g. (255, 151, 210)
    r=rgb.r
    g=rgb.g
    b=rgb.b
    color_tuple=(r,g,b)
    all_color.append(color_tuple)
print(all_color)

from turtle import Turtle,Screen,colormode
import random
# from random import random,choices,randint
colormode(255)
all_color=[(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57)]
t=Turtle()
t.shape('turtle')
val=random.choices(all_color)

t.setheading(225)
t.penup();
t.forward(300)
t.setheading(0)

number=100

for number_dots in range(1,number+1):
    val=random.choices(all_color)
    t.penup();
    t.dot(30, val[0]);
    t.penup()
    t.forward(50)
    if number_dots%10==0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)



screen=Screen()
screen.exitonclick()