c

def move_forward():
    tim.fd(10)

screen.listen()
screen.onkey(move_forward, "Up")
screen.exitonclick()
