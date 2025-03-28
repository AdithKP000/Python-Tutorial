""" 2.	Write a program to draw a pentagon using turtle."""

import turtle

def create_shape(length):
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(length)
        turtle.left(72)
    turtle.end_fill()

turtle.speed(1)
turtle.color("yellow")
turtle.bgcolor("black")

create_shape(100)

turtle.done()
