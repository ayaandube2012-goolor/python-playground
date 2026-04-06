import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="w", fun=player.move)
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.new_car()
    car_manager.move()

    if player.ycor() > FINISH_LINE_Y:
        player.next_level()
        car_manager.next_level()
        scoreboard.update_level()

    for car in car_manager.all_cars:
        if 25 < player.distance(car) < 35 and player.ycor() > car.ycor() - 25:
            scoreboard.game_over()
            screen.update()
            game_is_on = False

screen.mainloop()
