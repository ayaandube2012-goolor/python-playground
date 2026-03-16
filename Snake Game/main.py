from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakes")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 20:
        food.replenish()
        scoreboard.update_score()
        scoreboard.render_score()

screen.mainloop()
