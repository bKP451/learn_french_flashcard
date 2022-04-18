import tkinter
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
pair_chosen = dict()
# after_timer = None
set_of_words = pandas.read_csv('./data/french_words.csv')
to_learn = set_of_words.to_dict(orient='records')
count = 0

# print(to_learn)
# convert DataFrame into a dictionary
# set_of_words_list = set_of_words.to_dict(orient='records')
# print(set_of_words_list)


def show_translated_word():
    """It displays the translated word in English."""
    flash_canvas.itemconfig(front_image, image=card_back_image)
    flash_canvas.itemconfig(title, text="English", fill='white')
    print(type(pair_chosen))
    print(type(flash_canvas))
    flash_canvas.itemconfig(rand_word, text=f"{pair_chosen['English']}", fill='white')


def select_word():
    """It displays card showing the French word."""
    global pair_chosen, after_timer
    window.after_cancel(after_timer)
    flash_canvas.itemconfig(front_image, image=card_front_image)
    pair_chosen = random.choice(to_learn)
    random_french_word = pair_chosen['French']
    flash_canvas.itemconfig(title, text="French", fill='black')
    flash_canvas.itemconfig(rand_word, text=f"{random_french_word}", fill='black')
    after_timer = window.after(3000, show_translated_word)


# -------- LAYOUT -------- #


window = tkinter.Tk()
window.title("Learn French using Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flash_canvas = tkinter.Canvas(height=526, width=800, highlightthickness=0)
card_front_image = tkinter.PhotoImage(file='./images/card_front.png')
front_image = flash_canvas.create_image(400, 263, image=card_front_image)
card_back_image = tkinter.PhotoImage(file='./images/card_back.png')

title = flash_canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
rand_word = flash_canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
flash_canvas.config(bg=BACKGROUND_COLOR)
flash_canvas.grid(row=0, columnspan=2)

#  Buttons at the bottom  of the window
right_image = tkinter.PhotoImage(file='./images/right.png')
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=select_word)
right_button.grid(row=1,  column=0)
wrong_image = tkinter.PhotoImage(file='./images/wrong.png')
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=select_word)
wrong_button.grid(row=1, column=1)


after_timer = window.after(3000, show_translated_word)
# before show_translated_word()  is  invoked, select_word() is invoked
select_word()
window.mainloop()



