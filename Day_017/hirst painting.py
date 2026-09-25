import turtle as turtle_module
import  random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [
    (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123),
    (170, 154, 41), (138, 31, 52), (134, 164, 182), (18, 86, 60),
    (69, 12, 32), (180, 71, 44), (211, 128, 97), (112, 158, 140),
    (23, 56, 99), (121, 78, 118), (160, 62, 82), (165, 187, 160)
]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dot = 100

for dot_count in range(1, num_of_dot + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:

        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()