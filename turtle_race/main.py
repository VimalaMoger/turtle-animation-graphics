import random
from turtle import Turtle, Screen
import matplotlib.colors as mcolors
from constants import COLORS

def random_color():
    arr_colors = []
    for i in mcolors.BASE_COLORS.keys():
        if i in COLORS:
            arr_colors.append(COLORS[i])
    return arr_colors

def make_turtle_move(arr_colors):
    turtles = []
    y_position = [-70, -40, -10, 20, 50, 80]
    # We need 6 turtles starting from the same line
    for i in range(0, 6):
        new_turtle = Turtle(shape = "turtle")
        new_turtle.color(arr_colors[i])
        new_turtle.penup()
        new_turtle.goto(x = -350, y = y_position[i])
        turtles.append(new_turtle)
    start_turtle_race(user_bet, turtles)

def start_turtle_race(user_input, turtles):
    is_race_on = False
    if user_input:
        is_race_on = True
    while is_race_on:
        for tr in turtles:
            # Race ends at 330 pixel xcor
            if tr.xcor() > 330:
                winning_color = tr.pencolor()
                if winning_color == user_input.lower().title():
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You loose! The {winning_color} turtle is the winner!")
                is_race_on = False
            # Each turtle moves rand_distance pixels in the direction it is facing
            rand_distance = random.randint(0, 10)
            #turtle.dot(5, random.choice(colors))
            tr.forward(rand_distance)

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width = 800, height = 600)
    screen.bgcolor("black")
    colors = random_color()
    colors.append('exit')
    while True:
        user_bet = str(screen.textinput(f"{colors}", "Which turtle will win the race? Enter a color: "))
        if user_bet.lower() == 'exit':
            break
        elif  user_bet.lower().title() in colors:
            make_turtle_move(colors)
            screen.exitonclick()
            break
        else:
            print("Please enter a valid color.")






