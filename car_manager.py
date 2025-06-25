

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

from turtle import Turtle,Screen
import random

class CarManager(Turtle):
    def __init__(self):
       super().__init__()
       self.STARTING_MOVE_DISTANCE = 5
       self.MOVE_INCREMENT = 10
       self.cars = []
    def createCar(self):
        s=random.randint(1,6)
        if s==6:
            car = Turtle("square")
            car.penup()
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.goto(280, random.randint(-250, 250))
            self.cars.append(car)

            self.hideturtle()
    def move(self):
        for car in self.cars:
            car.backward(self.STARTING_MOVE_DISTANCE)
    def increment(self):

        self.STARTING_MOVE_DISTANCE+=self.MOVE_INCREMENT























