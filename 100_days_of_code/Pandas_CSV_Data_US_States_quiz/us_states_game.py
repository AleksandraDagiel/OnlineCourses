import turtle
import pandas

screen = turtle.Screen()
map_background = turtle.Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
map_background.shape(image)
data = pandas.read_csv("50_states.csv")
states_base = data["state"].to_list()
questions_counter = 0

while questions_counter < 50:
    if questions_counter == 0:
        answer_state = screen.textinput(title="Guess the State.", prompt="What's state's name?").title()
    else:
        answer_state = screen.textinput(title=f"{questions_counter}/50 States Correct",
                                        prompt="What's another state's name?").title()
    if answer_state not in states_base:
        print("State is not correct. Try again.")
    else:
        print("Correct")
        questions_counter += 1
        states_base.remove(answer_state)
        state_coordinates = (data[data.state == answer_state].x.item(), data[data.state == answer_state].y.item())
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(state_coordinates)
        turtle.write(arg=answer_state)


