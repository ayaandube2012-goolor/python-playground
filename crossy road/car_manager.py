import time
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.rolls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.move_distance = STARTING_MOVE_DISTANCE
        self.new_car()

    def new_car(self):
        chance = random.choices(self.rolls, weights=self.weights)[0]
        if chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(280, random.randint(-250, 250))
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.bk(self.move_distance)

    def next_level(self):
        self.weights[0] *= 1.6
        self.move_distance += 10

