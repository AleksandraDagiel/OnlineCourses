import turtle
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
turtle.colormode(255)
timmy_the_turtle.shape('arrow')
timmy_the_turtle.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_rgb_color = (r, g, b)
    return random_rgb_color


def draw_spirograph(size_of_graph):
    for _ in range(int(360 / size_of_graph)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_graph)


timmy_the_turtle.color('DodgerBlue2')

# Draws a dotted line
for n in range(15):
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)

timmy_the_turtle.reset()
max_num_of_sides = 11
num_of_sides = 3
timmy_the_turtle.speed('fastest')

# draw shapes from triangle to max_num_of_sides in different random colors
while not max_num_of_sides == num_of_sides:
    timmy_the_turtle.color(random_color())
    for i in range(num_of_sides):
        timmy_the_turtle.right(360 / num_of_sides)
        timmy_the_turtle.forward(100)
    num_of_sides += 1

timmy_the_turtle.reset()
random_direction = [0, 90, 180, 270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed('fastest')

# Draws thick line in random direction and color
for n in range(100):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.setheading(random.choice(random_direction))
    timmy_the_turtle.forward(30)

timmy_the_turtle.reset()
timmy_the_turtle.pensize()
timmy_the_turtle.speed('fastest')
draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()

