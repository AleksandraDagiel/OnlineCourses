from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('DodgerBlue2')
for n in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

timmy_the_turtle.right(45)

for n in range(15):
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)
