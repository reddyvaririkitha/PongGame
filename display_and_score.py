from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier",80,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align= ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_score_increment(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_score_increment(self):
        self.r_score += 1
        self.update_scoreboard()
        
class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.pensize(5)
        self.hideturtle()
        self.goto(0, 200)
        self.setheading(270)
        self.draw_border_line()

    def draw_border_line(self):
        while self.ycor() >= -250:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)