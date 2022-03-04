from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
else:
    data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_background, image=card_front)
    current_card = random.choice(to_learn)
    card_index = to_learn.index(current_card)
    print(current_card)
    canvas.itemconfig(title_canvas, text="French", fill="black")
    canvas.itemconfig(word_canvas, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_canvas, text="English", fill="white")
    canvas.itemconfig(word_canvas, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    to_learn.remove(current_card)
    next_card()
    pandas.DataFrame(to_learn).to_csv("./data/words_to_learn.csv", index=False)


window = Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_back)
title_canvas = canvas.create_text(400, 150, text="", font=("Ariel", 30, "italic"))
word_canvas = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_img = PhotoImage(file="./images/right.png")
button_right = Button(image=right_img, highlightthickness=0, command=is_known)
button_right.grid(column=0, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_img, highlightthickness=0, command=next_card)
button_wrong.grid(column=1, row=1)

next_card()



window.mainloop()