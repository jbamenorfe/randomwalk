"""This program uses python's turtle module to produce a turtle that makes random woalk. By JBAmenorfe on 07.01.2025"""
import turtle
from turtle import Turtle, Screen
import random

# Change color mode of the turtle module to enable the use of rgb colors
turtle.colormode(255)
def random_color():
    random_red = random.randint(0,255)
    random_green = random.randint(0,255)
    random_blue = random.randint(0,255)
    rgb = (random_red, random_green, random_blue)
    return rgb


# colors = ["green yellow", "lime green", "medium spring green", "lime", "aquamarine", "pale green", "cyan", "turquoise",
#           "dodger blue", "blue", "pale green", "magenta", "orange", "orange red", "gold", "deep pink"]
move_direction = [0, 90, 180, 270]

# Create the screen object
screen = Screen()
screen.screensize(canvheight=600, canvwidth=600, bg="wheat")

# Create a turtle object
eklo = Turtle()
eklo.shape("turtle")
eklo.pensize(10)
eklo.speed("fastest")
for steps in range(500):
    random_angle = random.choice(move_direction)
    eklo.color(random_color())
    eklo.forward(25)
    eklo.setheading(random_angle)

screen.exitonclick()
