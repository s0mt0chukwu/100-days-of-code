import random
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

# for _ in range(200):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))
#

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
#
#
# def draw_shape(num_sides):
#     angle = 360/ num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
#
# for shape_sides in range(3, 11):
#     timmy_the_turtle.color(random_color())
#     draw_shape(shape_sides)

import colorgram

# rgb_colors = []
# c0lors = colorgram.extract("image.jpg", 30)
# for color in c0lors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
screen.exitonclick()