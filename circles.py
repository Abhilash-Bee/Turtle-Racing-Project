from turtle import *

bgcolor("black")
hideturtle()
for i in range(200):
    speed(0)
    color("red")
    circle(i)
    color("yellow")
    circle(i * 0.8)
    forward(3)
    right(3)

exitonclick()
