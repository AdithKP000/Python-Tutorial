"""Draw a star using turtle methods."""

import turtle

def create_shape(length):
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(length)
        turtle.right(144)
    turtle.end_fill()

turtle.speed(3)
turtle.color("yellow")
turtle.bgcolor("black")

create_shape(100)

turtle.done()
