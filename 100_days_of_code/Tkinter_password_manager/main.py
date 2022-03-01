from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_label = Label(text="Email")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)


generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add")
add_button.grid(column=1, row=4, columnspan=2)

website_entry = Entry()
website_entry.grid(column=1, row=3, columnspan=2)
email_entry = Entry()
password_entry = Entry()





window.mainloop()