# creating scoreboard class to use in SNAKE GAME

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 25, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 340)
        self.write(f"SCORE: {self.score}", align = ALIGNMENT, font = FONT)
        self.hideturtle()

    def gameover(self):
        self.goto(0, 0)
        self.color('yellow')
        self.write("!! GAME OVER !!", align = ALIGNMENT, font = ("Courier", 30, "bold"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score}", align = "center", font = ("Arial", 25, "normal"))

    def clearscreen(self):
        self.clear()
