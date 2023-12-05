from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

current_card = {}


def french_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.create_image(400, 263, image=card_front)
    french_language_text = canvas.create_text(400, 150, text="Language", font=(FONT_NAME, 40, "italic"))
    french_word_text = canvas.create_text(400, 263, text="word", font=(FONT_NAME, 60, "bold"))
    canvas.itemconfig(french_language_text, text="French")
    canvas.itemconfig(french_word_text, text=current_card["French"])
    flip_timer = window.after(3000, func=english_card)


def english_card():
    canvas.create_image(400, 263, image=card_back)
    english_language_text = canvas.create_text(400, 150, text="Language", font=(FONT_NAME, 40, "italic"))
    english_word_text = canvas.create_text(400, 263, text="word", font=(FONT_NAME, 60, "bold"))
    canvas.itemconfig(english_language_text, text="English")
    canvas.itemconfig(english_word_text, text=current_card["English"])

# ---------------------------- UI SETUP ------------------------------- #

# Setup Flashcard
# Create window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=english_card)

# Create inside the window
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Create the template card
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="Language",  fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="word",  fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Could make word global and access in each function
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")

# Create and show right button
right_button = PhotoImage(file="images/right.png")
known_button = Button(image=right_button, highlightthickness=0, command=french_card)
known_button.grid(column=1, row=1)

# Create and show wrong button
wrong_button = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_button, highlightthickness=0, command=french_card)
unknown_button.grid(column=0, row=1)

french_card()
window.mainloop()

