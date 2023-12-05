from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
REVEAL_CARD = 1.8


# --------------------------- GUESSING TIMER ---------------------------- #
def guessing_timer(count, word_dict):
    if count > 0:
        timer = window.after(1000, guessing_timer, count - 1, word_dict)
    else:
        back_of_card(word_dict)


# --------------------------- BACK OF CARD ----------------------------- #
def back_of_card(english_word):
    english_card = canvas.create_image(400, 263, image=card_back)
    canvas.itemconfig(english_card, image=card_back)
    english_language_text = canvas.create_text(400, 150, text="Language", fill="white", font=(FONT_NAME, 40, "italic"))
    english_word_text = canvas.create_text(400, 263, text="word", fill="white", font=(FONT_NAME, 60, "bold"))
    canvas.itemconfig(english_language_text, text="English")
    canvas.itemconfig(english_word_text, text=english_word["English"])


# ---------------------------- NEXT CARD ------------------------------- #
def next_card():
    # Access CSV  file
    data = pandas.read_csv("data/french_words.csv")

    # Retrieve word from file and load it into program
    to_learn = data.to_dict(orient="records")
    word = random.choice(to_learn)

    french_card = canvas.create_image(400, 263, image=card_front)
    canvas.itemconfig(french_card, image=card_front)
    french_language_text = canvas.create_text(400, 150, text="Language", fill="black", font=(FONT_NAME, 40, "italic"))
    french_word_text = canvas.create_text(400, 263, text="word", fill="black", font=(FONT_NAME, 60, "bold"))
    # Create French word
    canvas.itemconfig(french_language_text, text="French")
    canvas.itemconfig(french_word_text, text=word["French"])

    # Reveal Card after timer is finished
    guessing_timer(REVEAL_CARD, word)


# ---------------------------- UI SETUP ------------------------------- #

# Setup Flashcard
# Create window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create and show front of the card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Create card layout
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
flash_card = canvas.create_image(400, 263, image=card_front)

# Create text for the card
language_text = canvas.create_text(400, 150, text="Language",  fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="word",  fill="black", font=(FONT_NAME, 60, "bold"))

# Place card in correct position
canvas.grid(column=0, row=0, columnspan=2)

# Create and show right button
right_button = PhotoImage(file="images/right.png")
known_button = Button(image=right_button, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)

# Create and show wrong button
wrong_button = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_button, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()
window.mainloop()

