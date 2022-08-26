from turtle import Turtle, Screen

mothi = Turtle()
screen = Screen()


def forward():
    mothi.forward(10)


def backward():
    mothi.backward(10)


def turn_left():
    mothi.left(10)


def turn_right():
    mothi.right(10)


def clear_screen():
    screen.reset()


screen.listen()
screen.onkey(key="W", fun=forward)
screen.onkey(key="S", fun=backward)
screen.onkey(key="A", fun=turn_left)
screen.onkey(key="D", fun=turn_right)
screen.onkey(key="C", fun=clear_screen)

screen.exitonclick()
