from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Bet on a turtle (choose a colour): ")
colours = ["red", "orange", "yellow", "green", "pink", "blue", "purple"]
all_turtles = []

y = -90
for colour in colours:
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.color(colour)
    racer.goto(x=-230, y=y)
    all_turtles.append(racer)
    y += 30

if user_bet:
    is_race_on = True

winner = None
while is_race_on:
    for racer in all_turtles:
        racer.fd(random.randint(0, 10))
        if racer.xcor() >= 240:
            is_race_on = False
            winner = racer
print(f"{winner.fillcolor()} won !")
if user_bet.lower() == winner.fillcolor():
    print("you won the bet, here is your money: $$$")
else:
    print("you lost the bet.")
    

screen.exitonclick()
