from tkinter import *
import random

nbr_secret = random.randint(1, 100)

def Check_Guess():
    guess = int(number.get())
    if guess == nbr_secret:
        result_label.config(text="well done you find the hidden number 👏🏻!!")
    elif guess < nbr_secret:
        result_label.config(text="More !")
    else:
        result_label.config(text="Less !")

# Create the main window
game = Tk()
game.title("GUESS THE HIDDEN NUMBER !?")

# Create and pack widgets
Label(game, text="Guess A Number Between 1 And 100").pack()

number = Entry(game)
number.pack()

check_button = Button(game, text="Check it", command=Check_Guess)
check_button.pack()

result_label = Label(game, text="")
result_label.pack()

# Start the Tkinter event loop
game.mainloop()
