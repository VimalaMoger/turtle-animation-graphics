from turtle import Turtle, Screen
from turtles_race import TurtlesRace
from constants import WINDOW_HEIGHT, WINDOW_WIDTH

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
    screen.bgcolor("black")

    turtles_race = TurtlesRace()
    colors = turtles_race.random_color()

    while True:
        user_bet = str(screen.textinput(f"{colors}", "Which turtle will win the race? Enter a color: or 'q' to end"))
        # Type 'q', press Enter
        if user_bet.lower() == 'q':
            break
        elif  user_bet.lower().title() in colors:
            turtles_race.make_turtle_move()
            turtles_race.start_turtle_race(user_bet)
            screen.exitonclick()
            break
        else:
            print("Please enter a valid color.")






