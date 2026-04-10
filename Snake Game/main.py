from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

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
        snake.extend()
        food.replenish()
        scoreboard.update_score()

    if snake.head.xcor() > 275 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -275:
        scoreboard.game_over()
        screen.update()
        time.sleep(3)
        scoreboard.clear_screen()
        scoreboard.render_score()
        snake.game_over()

    for seg in snake.segments[1:]:
        if (snake.head.heading() == DOWN and seg.heading() == UP
                or snake.head.heading() == UP and seg.heading() == DOWN
                or snake.head.heading() == LEFT and seg.heading() == RIGHT
                or snake.head.heading() == RIGHT and seg.heading() == LEFT):

            pass

        elif snake.head.distance(seg) < 5:
            scoreboard.game_over()
            screen.update()
            time.sleep(3)
            scoreboard.clear_screen()
            scoreboard.render_score()
            snake.game_over()

screen.mainloop()
