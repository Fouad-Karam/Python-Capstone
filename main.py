from tkinter import *
import pandas
import random
from tkinter import messagebox

# ******************** Functions *********************
data = pandas.read_csv("data/multiplication.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    try:
        global current_card
        current_card = random.choice(to_learn)
        canvas.itemconfig(card_title, text="Table")
        canvas.itemconfig(card_word, text=current_card["Table"])
        canvas.itemconfig(card_background, image=card_front_img)
    except IndexError:
        messagebox.showwarning(title="Warning", message="You have answered all the questions. Please close the app")


def answer_card():
    canvas.itemconfig(card_title, text="Answer")
    canvas.itemconfig(card_word, text=current_card["Answer"])
    canvas.itemconfig(card_background, image=card_back_img)


def wrong_card():
    canvas.itemconfig(card_title, text="Oops, wrong!")
    canvas.itemconfig(card_word, text="Next Q")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    try:
        to_learn.remove(current_card)
        # print(len(to_learn))
        canvas.itemconfig(card_title, text="Correct! Next Q")
        # canvas.itemconfig(card_word, text="Next Q")
        # canvas.itemconfig(card_background, image=card_back_img)
    except ValueError:
        messagebox.showwarning(title="Oops!",
                               message="You clicked the green check mark already. Pick the next question.")


# ******************** UI *********************

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Capstone")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Multiplication", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Are you Ready?", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=4)

wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0, command=wrong_card)
unknown_button.grid(row=1, column=0)

question_img = PhotoImage(file="images/question.png")
known_button = Button(image=question_img, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

answer_img = PhotoImage(file="images/answer.png")
known_button = Button(image=answer_img, highlightthickness=0, command=answer_card)
known_button.grid(row=1, column=2)

right_img = PhotoImage(file="images/right.png")
known_button = Button(image=right_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=3)

# next_card()

window.mainloop()
