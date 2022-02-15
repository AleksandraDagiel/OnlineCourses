from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle win win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x_position = -230
y_position = [-100, -50, 0, 50, 100, 150]

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=x_position, y=y_position)


screen.exitonclick()
