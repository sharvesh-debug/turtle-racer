import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
c1=CarManager()
level=Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()


screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True


while game_is_on:

    time.sleep(0.1)
    screen.update()
    c1.createCar()
    c1.move()
    for car in c1.cars:
        if car.distance(player)<20:
            level.over()
            game_is_on=False
    if player.ycor()>280:
        level.calc()

        c1.increment()
        print(c1.STARTING_MOVE_DISTANCE)
        player.restart()
screen.exitonclick()


