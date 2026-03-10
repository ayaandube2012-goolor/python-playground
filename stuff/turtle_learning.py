import turtle
from turtle import Turtle, Screen

bob = Turtle()
bob.shape("turtle")
#for _ in range(4):
#   bob.fd(100)
#    bob.lt(90)

# dashed line
# bob.pu()
# bob.bk(100)
# bob.pd()
# for _ in range(25):
#     bob.fd(10)
#     bob.pu()
#     bob.fd(10)
#     bob.pd()

# polygon overlap
# import random
# bob.screen.colormode(255)
# bob.pu()
# bob.goto(-50, 400)
# bob.pd()
#
# turn_angle = 120
# num_of_sides = 3
# bob.speed(0)
# for _ in range(30):
#     bob.color(random.randint(0, 225), random.randint(0, 225), random.randint(0, 225))
#     for _ in range(num_of_sides):
#         bob.fd(100)
#         bob.rt(turn_angle)
#     num_of_sides += 1
#     turn_angle = 360 / num_of_sides

#random walk
import random
bob.screen.colormode(255)
directions = [0, 90, 180, 270]

bob.pensize(10)
bob.speed(0)
for _ in range(1000):
    bob.color(random.randint(0, 225), random.randint(0, 225), random.randint(0, 225))
    bob.setheading(random.choice(directions))
    bob.fd(20)


screen = Screen()
screen.exitonclick()
