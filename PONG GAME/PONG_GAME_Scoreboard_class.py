from turtle import Turtle

class Scoreboard (Turtle):
    def __init__ (self):
        super(). __init__ ()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.goto(-100, 250)
        self.write(self.left_score, align = 'center', font = ("Courier", 70, "bold"))
        self.goto(100, 250)
        self.write(self.right_score, align = 'center', font = ("Courier", 70, "bold"))

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.left_score, align = 'center', font = ("Courier", 70, "bold"))
        self.goto(100, 250)
        self.write(self.right_score, align = 'center', font = ("Courier", 70, "bold"))

    def increase_l_score(self):
        self.left_score += 1
        self.update_scoreboard()

    def increase_r_score(self):
        self.right_score += 1
        self.update_scoreboard()
        
        
