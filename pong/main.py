from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=l_paddle.down, key="s")
screen.onkey(fun=l_paddle.up, key="w")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.y_bounce()

    if ((ball.xcor() > 320 and ball.x_move > 0 and ball.distance(r_paddle) < 50)
        or (ball.xcor() < -320 and ball.x_move < 0 and ball.distance(l_paddle) < 50)):

        ball.x_bounce()
        ball.move_speed *= 0.9

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
        ball.move_speed = 0.1

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
        ball.move_speed = 0.1

screen.mainloop()
