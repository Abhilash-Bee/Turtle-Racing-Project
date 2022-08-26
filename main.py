from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
screen.setup(width=700, height=600)
user_choice = screen.textinput("Make a bet", "Which turtle is going to win the race, chose the color:: ")

color = ["red", "green", "blue", "yellow", "purple", "orange"]

turtle_object = []
for i in range(6):
    turtle_object.append(Turtle())
    turtle_object[i].shape("turtle")
    turtle_object[i].color(color[i])

x, y = -330, -100
for turtle in turtle_object:
    turtle.penup()
    turtle.goto(x, y)
    y += 40


def start_race(value: bool):
    while value:
        forward_movement = randint(0, 10)
        get_turtle = choice(turtle_object)
        get_turtle.forward(forward_movement)
        width = get_turtle.xcor()
        if width >= 350:
            return get_turtle.color()[0]


if user_choice:
    actual_win = start_race(True)
    if actual_win == user_choice:
        print(f"You won the bet, {actual_win} turtle wins the race")
    else:
        print(f"You lose the bet, {actual_win} turtle wins the race")

screen.exitonclick()
