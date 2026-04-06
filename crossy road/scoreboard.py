from turtle import Turtle

LEVEL_FONT = ("Terminal", 25, "normal")
GAMEOVER_FONT = ("Terminal", 80, "bold")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.levels = 1
        self.write(f"LEVEL: {self.levels}", align=ALIGNMENT, font=LEVEL_FONT)

    def update_level(self):
        self.levels += 1
        self.clear()
        self.write(f"LEVEL: {self.levels}", align=ALIGNMENT, font=LEVEL_FONT)

    def game_over(self):
        self.home()
        self.color("red")
        self.write(f"GAME OVER", align=ALIGNMENT, font=GAMEOVER_FONT)

