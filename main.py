from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# Access CSV  file
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = random.choice(to_learn)


# --------------------------- REVEAL CARD ----------------------------- #
def reveal_card(words):
    card_back = PhotoImage(file="images/card_back.png")
    english_card = canvas.create_image(400, 263, image=card_back)
    canvas.itemconfig(english_card, image=card_back)
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=words["English"])


# ----------------------- CHANGE FRENCH WORD -------------------------- #
def next_card(words):
    canvas.itemconfig(french_card, image=card_front)
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, text=words["French"])


# ---------------------------- UI SETUP ------------------------------- #
# Create window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create and show front of the card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="images/card_front.png")
french_card = canvas.create_image(400, 263, image=card_front)

language_text = canvas.create_text(400, 150, text="Language",  fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="word",  fill="black", font=(FONT_NAME, 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Create and show right button
right_button = PhotoImage(file="images/right.png")
known_button = Button(image=right_button, highlightthickness=0, command=lambda: next_card(current_card))
known_button.grid(column=1, row=1)

# Create and show wrong button
wrong_button = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_button, highlightthickness=0, command=lambda: next_card(current_card))
unknown_button.grid(column=0, row=1)

next_card(current_card)
# window.after(3000)
# reveal_card(current_card)

window.mainloop()
