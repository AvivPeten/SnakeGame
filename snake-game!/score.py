from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.update_score()


    def update_score(self):
        self.write(f"SCORE:  {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)