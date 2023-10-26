from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
REVEAL_CARD = 1.8


# --------------------------- GUESSING TIMER ---------------------------- #
def guessing_timer(count, word_dict):
    timer = window.after(1000, guessing_timer, count - 1, word_dict)
    if count < 0.0:
        english_card(word_dict)
        window.after_cancel(timer)


# ---------------------------- NEXT CARD ------------------------------- #
def new_card():
    words = study_words()
    french_card(words)
    guessing_timer(REVEAL_CARD, words)


def study_words():
    try:
        data = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        data = pandas.read_csv("data/french_words.csv")
        to_learn = data.to_dict(orient="records")
        return random.choice(to_learn)
    else:
        to_learn = data.to_dict(orient="records")
        return random.choice(to_learn)


def french_card(french_word):
    canvas.create_image(400, 263, image=card_front)
    french_language_text = canvas.create_text(400, 150, text="Language", font=(FONT_NAME, 40, "italic"))
    french_word_text = canvas.create_text(400, 263, text="word", font=(FONT_NAME, 60, "bold"))
    canvas.itemconfig(french_language_text, text="French")
    canvas.itemconfig(french_word_text, text=french_word["French"])


def english_card(english_word):
    canvas.create_image(400, 263, image=card_back)
    english_language_text = canvas.create_text(400, 150, text="Language", font=(FONT_NAME, 40, "italic"))
    english_word_text = canvas.create_text(400, 263, text="word", font=(FONT_NAME, 60, "bold"))
    canvas.itemconfig(english_language_text, text="English")
    canvas.itemconfig(english_word_text, text=english_word["English"])


# ---------------------------- UI SETUP ------------------------------- #
# Create window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create inside the window
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Create the template card
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="Language",  fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="word",  fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Create and show right button
right_button = PhotoImage(file="images/right.png")
known_button = Button(image=right_button, highlightthickness=0, command=new_card)
known_button.grid(column=1, row=1)

# Create and show wrong button
wrong_button = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_button, highlightthickness=0, command=new_card)
unknown_button.grid(column=0, row=1)

new_card()
window.mainloop()

