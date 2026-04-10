import time
from turtle import Turtle

STARTING_POSITION = (0, 260)
ALIGNMENT = "center"
FONT = ("Terminal", 20, "normal")
GAME_OVER_FONT = ("Impact", 48, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.high_score = 0
        self.score = 0
        self.render_score()

    def render_score(self):
        self.goto(STARTING_POSITION)
        self.clear()
        self.color("white")
        self.write(arg=f"SCORE: {self.score} HIGHSCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.render_score()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.home()
        self.color("red")
        self.write(arg="GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)

    def clear_screen(self):
        self.clear()
        self.home()
