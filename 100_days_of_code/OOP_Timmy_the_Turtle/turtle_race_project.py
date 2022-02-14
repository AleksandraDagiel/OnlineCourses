import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("arrow")
# tim.up()


def clean_screen():
    tim.penup()
    tim.clean()
    tim.home()
    tim.pendown()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


screen.listen()
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clean_screen)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_right)
screen.exitonclick()
