

import turtle

def draw_hexagon(size):
    for _ in range(6):
        turtle.forward(size)
        turtle.right(60)

def draw_radial_pattern(len, count):
    for _ in range(count):
        draw_hexagon(len)
        turtle.right(360 / count)

# Setup turtle
turtle.speed(0.5)
turtle.bgcolor("black")
turtle.color("yellow")


draw_radial_pattern(50, 10)

turtle.done()

