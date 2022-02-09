import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkSlateGray")
turtle.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()