from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Terminal", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(y=260, x=0)
        self.score = 0
        self.render_score()

    def render_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
