from turtle import Turtle,Screen,clearscreen

MOVE_DISTANCE=20
HEAD=3

class Snake:
    def __init__(self):
        self.positionList=[(0,0),(20,0),(40,0)]
        self.snake_pieces=[]
        

        for i in range(3):
            self.snake=Turtle()
            self.snake.shape('square')
            self.snake.color('white')
            self.snake.penup()
            self.snake.goto(self.positionList[i])
            self.snake_pieces.append(self.snake)

        self.head=self.snake_pieces[0]

    def move(self):
        for piece in range(len(self.snake_pieces)-1,0,-1):
           
           x_new_pos=self.snake_pieces[piece-1].xcor()
           y_new_pos=self.snake_pieces[piece-1].ycor()
           self.snake_pieces[piece].goto(x_new_pos,y_new_pos)
        

        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        self.head.setheading(90)
    def move_right(self):
        self.head.setheading(0)
    def move_left(self):
        self.head.setheading(180)
    def move_down(self):
        self.head.setheading(270)
    def head_increase(self):
        self.snake=Turtle()
        self.snake.shape('square')
        self.snake.color('white')
        self.snake.penup()
        self.snake.goto(self.positionList[i])
        self.snake_pieces.append(self.snake)