from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")

with open("./data/french_words.csv") as data:
    words_dict = pandas.read_csv(data)

random_word = random.choice(words_dict["French"])
print(random_word)


# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_img = PhotoImage(file="./images/right.png")
button_right = Button(image=right_img, highlightthickness=0)
button_right.grid(column=0, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_img, highlightthickness=0)
button_wrong.grid(column=1, row=1)

# Labels
language_label = Label(text="Title", font=("Ariel", 30, "italic"))
language_label.grid(column=0, row=0, columnspan=2)
language_label.place(x=400, y=150, anchor="center")

word_label = Label(text=random_word, font=("Ariel", 60, "bold"))
word_label.grid(column=0, row=0, columnspan=2)
word_label.place(x=400, y=263, anchor="center")





window.mainloop()