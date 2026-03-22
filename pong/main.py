from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.title("Pong")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.update()

screen.listen()
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=l_paddle.down, key="s")
screen.onkey(fun=l_paddle.up, key="w")

game_is_on = True
while game_is_on:
    screen.update()

screen.mainloop()
