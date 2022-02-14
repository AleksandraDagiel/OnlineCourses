import turtle
import colorgram
import random

t = turtle.Turtle()
turtle.colormode(255)


def get_colors_from_picture(picture, num_of_colors):
    colors_palette = colorgram.extract(picture, num_of_colors)
    color_list = []
    for color in colors_palette:
        rgb = (colors_palette[color]).rgb
        color_list.append(rgb)
    return color_list


color_palette_list = get_colors_from_picture('dot_painting_color_sample.jpg', 30)
max_num_of_sides = 11
num_of_sides = 3
t.speed('fastest')

# draw shapes from triangle to max_num_of_sides in different random colors
while not max_num_of_sides == num_of_sides:
    t.color(random.choice(color_palette_list))
    for i in range(num_of_sides):
        t.right(360 / num_of_sides)
        t.forward(100)
    num_of_sides += 1


screen = turtle.Screen()
screen.exitonclick()