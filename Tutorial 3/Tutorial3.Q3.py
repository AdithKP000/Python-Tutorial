"""3.	Write a program to draw a circle using turtle."""


import turtle

def create_shape(length):
    turtle.begin_fill()
    turtle.circle(length)
    turtle.end_fill()

# Setup turtle
turtle.speed(1)
turtle.color("yellow")
turtle.bgcolor("black")

create_shape(100)

turtle.done()
