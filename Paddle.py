from turtle import Turtle
PADDLE_WIDTH = 5
PADDLE_LENGTH = 1
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, paddle_coordinate):
        super().__init__()
        self.coordinate = paddle_coordinate
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.penup()
        self.goto(self.coordinate)

    def move_up(self):
        y_coordinate = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y_coordinate)

    def move_down(self):
        y_coordinate = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), y_coordinate)
