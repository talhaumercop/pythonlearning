import turtle
import pandas as pd

screen=turtle.Screen()
screen.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')



pen = turtle.Turtle()

# Hide the turtle pointer
pen.hideturtle()
# Don't draw lines while moving
pen.penup()



game_over=False
game_points=50
game_used_points=0
states=pd.read_csv('50_states.csv')

screen.title('guess states')


while not game_over:
    value = screen.textinput(title=f'{game_used_points}/{game_points}guess states', prompt='whats another state name')

    for i in states["state"]:
        if i == value:
            state_value = states[states["state"] == value]
            x=state_value['x'].item()
            y=state_value['y'].item()
            print(x)
            pen.goto(x,y)
            # Write text on the screen
            pen.write(f"{state_value['state'].item()}", align="center", font=("Arial", 16, "normal"))
            game_used_points += 1





screen.exitonclick()