from turtle import Turtle,Screen,clearscreen
import random

color=['yellow','green','purple','blue','red','orange','pink']
screen=Screen()
screen.setup(width=500,height=400)
input_user=screen.textinput("guess", "who is going to win the race:")
is_game_on=False

val=-130
turtles=[]

def turtle(colorfill):
    t=Turtle()
    t.shape('turtle')
    t.color(colorfill)
    t.penup()
    t.goto(-230,val)
    turtles.append(t)


for i in range(0,7):
    colors=color[i]
    turtle(colors)
    val+=50

if input_user:
    is_game_on=True

while is_game_on:
    for turtle in turtles:
        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)
        if turtle.xcor()>230:
            win_turtle=turtle.pencolor()
            if win_turtle == input_user:
                print(f'yes you have won {win_turtle} turtle have won')
                is_game_on=False
            else:
                print(f'you loose {win_turtle} turtle have won!')
                is_game_on=False

screen.exitonclick()