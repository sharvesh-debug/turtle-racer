STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle,Screen


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.restart()

        self.shape("turtle")
    def move(self):
        self.forward(10)
    def restart(self):
        self.goto(STARTING_POSITION)


