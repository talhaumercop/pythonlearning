from turtle import Turtle,Screen,clearscreen
import time
from snake import Snake
from food import Food

screen=Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.listen()

snake=Snake()
food=Food()
food.random_location()

screen.onkey(fun=snake.move_up,key='Up')
screen.onkey(fun=snake.move_down,key='Down')
screen.onkey(fun=snake.move_left,key='Left')
screen.onkey(fun=snake.move_right,key='Right')

game_over=False

while not game_over:
        screen.update()
        time.sleep(0.1)
        snake.move()
        
        if snake.head.distance(food)<15:
                food.random_location()
                snake.head_increase()

screen.exitonclick()