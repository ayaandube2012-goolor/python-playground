from data import *
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

tim.speed(0)
tim.teleport(-250, -250)
tim.penup()
for row in range(10):
    for dot in range(10):
        tim.color(random.choice(color_palette))
        tim.dot(20)
        tim.fd(50)
    tim.teleport(-250, tim.ycor() + 50)
tim.hideturtle()

screen.exitonclick()
