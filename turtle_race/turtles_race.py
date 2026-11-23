import random
from turtle import Turtle
import matplotlib.colors as mcolors
from constants import COLORS, Y_POSITION, X_POSITION


class TurtlesRace:
    def __init__(self):
        self.__arr_colors = []
        self.__turtles = []
        self.__is_race_on = False

    def random_color(self):
        for i in mcolors.BASE_COLORS.keys():
            if i in COLORS:
                self.__arr_colors.append(COLORS[i])
        return self.__arr_colors

    def make_turtle_move(self):
        # This positions each turtle at the start line
        for i in range(0, 6):
            new_turtle = Turtle(shape="turtle")
            new_turtle.color(self.__arr_colors[i])
            new_turtle.penup()
            new_turtle.goto(x=-350, y = Y_POSITION[i])
            self.__turtles.append(new_turtle)

    def start_turtle_race(self, user_input):
        is_race_on = False
        if user_input:
            self.__is_race_on = True
        while self.__is_race_on:
            for tr in self.__turtles:
                # race ends at 330 pixel x position - finish line
                if tr.xcor() > X_POSITION:
                    winning_color = tr.pencolor()
                    if winning_color.lower() == user_input.lower():
                        print(f"You've won! The {winning_color} turtle is the winner!")
                    else:
                        print(f"You loose. The {winning_color} turtle is the winner!")
                    self.__is_race_on = False
                # Each turtle moves rand_distance pixels in the direction it is facing
                rand_distance = random.randint(0, 10)
                tr.forward(rand_distance)