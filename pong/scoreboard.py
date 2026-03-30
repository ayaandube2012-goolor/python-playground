from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Terminal", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 200)
        self.render_score()

    def render_score(self):
        self.clear()
        self.write(f"{self.l_score}:{self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.render_score()

    def r_point(self):
        self.r_score += 1
        self.render_score()