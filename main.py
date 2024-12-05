"""
********************************************************************************
* Project Name:  Turtle Crossing Game
* Description:   This is a fun and simple Turtle Crossing game created using Python's turtle module.
* Author:        ziqkimi308
* Created:       2024-12-05
* Updated:       2024-12-05
* Version:       1.0
********************************************************************************
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Calling classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Controller
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for i in car_manager.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()

