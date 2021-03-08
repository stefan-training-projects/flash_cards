from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#-----------------------UI SETUP------------------#
window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#images
card_back_image = PhotoImage(file = "images/card_back.png")
card_front_image = PhotoImage(file = "images/card_front.png")
right_image = PhotoImage(file ="images/right.png")
wrong_image = PhotoImage(file= "images/wrong.png")

#canvas setup
canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400,263, image=card_back_image)
canvas.create_image(400,263, image=card_front_image)
canvas.create_text(400, 150, text="Title", font = ('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text="Word", font = ('Ariel', 60, 'italic'))
canvas.grid(row=0,column=0,columnspan=2)

#buttons
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_image, bg=BACKGROUND_COLOR)
right_button.grid(row=1, column = 1)

window.mainloop()
