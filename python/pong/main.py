from turtle import Screen
from Bar import Bar
from ball import Ball
import time

screen=Screen()
screen.bgcolor('black')
screen.title('Pong Game')
screen.setup(height=600,width=800)

bar_l=Bar((-350,0))
bar_r=Bar((350,0))

ball=Ball()



screen.listen()
screen.onkey(bar_r.eventListen_UP,'Up')
screen.onkey(bar_r.eventListen_DOWN,'Down')
screen.onkey(bar_l.eventListen_UP,'w')
screen.onkey(bar_l.eventListen_DOWN,'s')


game_over=False
while not game_over:
    time.sleep(0.1)
    ball.move()

    if ball.ball.ycor()>= 280 or ball.ball.ycor()<= -280:
        ball.bounce_Y() 
        
    if ball.ball.distance(bar_r.bar)<50 or ball.ball.xcor()>340:
        ball.bounce_X()
    elif ball.ball.distance(bar_l.bar)<50 or ball.ball.xcor()<-340:
        ball.bounce_X()
screen.exitonclick()
