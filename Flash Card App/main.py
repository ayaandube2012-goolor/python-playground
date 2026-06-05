from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
word = {}

def flip_card(word_to_translate):
    english_word = word_to_translate["English"]
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(word_label, text=english_word)
    canvas.itemconfig(language_label, text="english")


def display_word():
    global word, flip_card_delay
    window.after_cancel(flip_card_delay)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(language_label, text="german")
    word = random.choice(german_words)
    german_word = word["German"]
    canvas.itemconfig(word_label, text=german_word)
    flip_card_delay = window.after(3000, flip_card, word)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_card_delay = window.after(3000, flip_card, word)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
language_label = canvas.create_text(390, 150, text="german", font=("Arial", 40, "italic"))
word_label = canvas.create_text(390, 263, text="Click button to start", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(bg=BACKGROUND_COLOR, cursor="hand2")
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button.config(image=wrong_button_image, command=display_word)
wrong_button.grid(row=1, column=0)

correct_button = Button(bg=BACKGROUND_COLOR, cursor="hand2")
right_button_image = PhotoImage(file="images/right.png")
correct_button.config(image=right_button_image, command=display_word)
correct_button.grid(row=1, column=1)

df = pd.read_csv("data/german-english data.csv")
german_words = df.to_dict(orient="records")


window.mainloop()
