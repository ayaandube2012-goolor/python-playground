from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.replenish()

    def replenish(self):
        self.goto(y=random.randint(-270, 280), x=random.randint(-280, 270))

    def destroy(self):
        self.hideturtle()
