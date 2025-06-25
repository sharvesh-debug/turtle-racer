FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(-250,250)
        self.hideturtle()
        self.write(arg=f"level: {self.score}",align="left",font=FONT)
    def calc(self):
        self.clear()
        self.score+=1
        self.write(arg=f"level: {self.score}", align="left", font=FONT)
    def over(self):
        self.goto(0,0)
        self.write(arg="Game Over", align="center", font=FONT)


