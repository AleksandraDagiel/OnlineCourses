from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=250)
window.config(padx=50, pady=50)


def calculate():
    miles = entry.get()
    kilometers = str(round(int(miles) * 1.6, 2))
    result_window.config(text=kilometers)


Label(text="Miles", font=("Arial", 15, "normal"), width=20).grid(column=3, row=1)
Label(text="Km", font=("Arial", 15, "normal"), width=20).grid(column=3, row=2)
Label(text="is equal to", font=("Arial", 15, "normal"), width=20).grid(column=1, row=2)

button = Button(text="Calculate", command=calculate, font=("Arial", 15, "normal"), width=20)
button.grid(column=2, row=3)

entry = Entry(width=20, font=("Arial", 15, "normal"))
entry.insert(END, string="0")
entry.grid(column=2, row=1)

result_window = Label(text="0", font=("Arial", 15, "normal"), width=20)
result_window.grid(column=2, row=2)


window.mainloop()
