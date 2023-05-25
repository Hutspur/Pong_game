from turtle import Screen
from Paddle import Paddle
from ball import Ball
import time

P1_COR = (380, 0)
P2_COR = (-380, 0)

screen = Screen()
screen.title("Pong Legend")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

player1 = Paddle(P1_COR)
player2 = Paddle(P2_COR)
ball = Ball()


screen.listen()
screen.onkey(fun=player2.move_up, key="w")
screen.onkey(fun=player2.move_down, key="s")
screen.onkey(fun=player1.move_up, key="Up")
screen.onkey(fun=player1.move_down, key="Down")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect collision
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.y_bounce()
    # Detect collision with paddle
    if ball.distance(player1) < 50 and ball.xcor() > 360 or ball.distance(player2) < 50 and ball.xcor() < -360:
        ball.x_bounce()


screen.exitonclick()


git confg --globaluser.email