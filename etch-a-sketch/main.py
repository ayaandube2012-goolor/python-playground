from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forward():
    tim.fd(10)

def backward():
    tim.bk(10)

def turn_right():
    tim.rt(5)

def turn_left():
    tim.lt(5)

def clear():
    tim.speed(0)
    tim.home()
    tim.setheading(0)
    tim.clear()
    tim.speed('normal')



screen.listen()
screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
