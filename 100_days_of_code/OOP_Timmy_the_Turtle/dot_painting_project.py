import turtle
import colorgram
import random

t = turtle.Turtle()
turtle.colormode(255)


# def get_colors_from_picture(picture, num_of_colors):
#     colors_palette = colorgram.extract(picture, num_of_colors)
#     color_list = []
#     for color in colors_palette:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         color_list.append((r, g, b))
#     return color_list
#
#
# rgb_list = get_colors_from_picture('dot_painting_color_sample.jpg', 30)

color_palette = [
    (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157),
    (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55),
    (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113),
    (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)
]

t.speed(8)
t.penup()
t.setposition(-250, -250)
t.hideturtle()

for _ in range(10):
    position = t.position()
    for _ in range(10):
        t.dot(20, (random.choice(color_palette)))
        t.forward(50)
    t.goto(x=position[0], y=position[1]+50)


screen = turtle.Screen()
screen.exitonclick()
