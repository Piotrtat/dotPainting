import colorgram
import turtle as turtle_module
import random

colors = colorgram.extract('image.jpg', 30)
color_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)

turtle_module.colormode(255)
diesel = turtle_module.Turtle()

diesel.penup()

diesel.setheading(225)
diesel.forward(300)
diesel.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    diesel.dot(20, random.choice(color_list))
    diesel.forward(50)

    if dot_count % 10 == 0:
        diesel.setheading(90)
        diesel.forward(50)
        diesel.setheading(180)
        diesel.forward(500)
        diesel.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()