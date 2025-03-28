"""8.	Write a GUI-based program that plays a guess-the-number game in which the user guesses a 
number between 1 and 100 and the computer provides the responses. The window should display the user’s
 guesses with a label by saying, “Too large, try again,” or “Too small, try again.” When the user finally
   guesses the correct number,
 the program congratulates him and tells him the total number of guesses"""


import tkinter as tk
from tkinter import messagebox
import random

def check_guess():
    global guess_count
    try:
        user_guess = int(entry_guess.get())
        guess_count += 1
        if user_guess < target_number:
            label_result.config(text="Too small, try again.")
        elif user_guess > target_number:
            label_result.config(text="Too large, try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it right in {guess_count} attempts!")
            reset_game()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

def reset_game():
    global target_number, guess_count
    target_number = random.randint(1, 100)
    guess_count = 0
    label_result.config(text="")
    entry_guess.delete(0, tk.END)

# Create main window
window = tk.Tk()
window.title("Guess the Number Game")

label_guess = tk.Label(window, text="Guess a number (1-100):")
label_guess.grid(row=0, column=0)
entry_guess = tk.Entry(window)
entry_guess.grid(row=0, column=1)

button_guess = tk.Button(window, text="Submit Guess", command=check_guess)
button_guess.grid(row=1, column=0, columnspan=2)

label_result = tk.Label(window, text="", font=("Arial", 10))
label_result.grid(row=2, column=0, columnspan=2)

button_reset = tk.Button(window, text="Reset Game", command=reset_game)
button_reset.grid(row=3, column=0, columnspan=2)

# Initialize game variables
target_number = random.randint(1, 100)
guess_count = 0

# Run the application
window.mainloop()