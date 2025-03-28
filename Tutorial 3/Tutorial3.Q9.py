"""9.	Write a GUI-based program that plays a guess-the-number game in which the computer guesses a 
number between 1 and 100 and the user provides the responses. The window should display the computer’s 
guesses with a label. The user enters a hint in response, by selecting one of a set of command buttons labeled 
Too small, Too large, and Correct. When the game is over,
 you should disable these buttons and wait for the user to click New game, as before.(university question)"""


import tkinter as tk
from tkinter import messagebox
import random

def comp_guess():
    global l, h, g, a
    if l <= h:
        g = (l + h) // 2
        lbl_g.config(text=f"Is it {g}?")
    else:
        lbl_g.config(text="Restart game.")

def too_sm():
    global l, a
    l = g + 1
    a += 1
    comp_guess()

def too_lg():
    global h, a
    h = g - 1
    a += 1
    comp_guess()

def corr():
    messagebox.showinfo("Done!", f"Guessed in {a} attempts!")
    dis_btns()

def dis_btns():
    btn_sm.config(state=tk.DISABLED)
    btn_lg.config(state=tk.DISABLED)
    btn_corr.config(state=tk.DISABLED)

def new_g():
    global l, h, a
    l, h = 1, 100
    a = 0
    enb_btns()
    comp_guess()

def enb_btns():
    btn_sm.config(state=tk.NORMAL)
    btn_lg.config(state=tk.NORMAL)
    btn_corr.config(state=tk.NORMAL)

w = tk.Tk()
w.title("Guess the Number")

lbl_g = tk.Label(w, text="Think of a number 1-100.")
lbl_g.grid(row=0, column=0, columnspan=2)
btn_sm = tk.Button(w, text="Too Small", command=too_sm)
btn_sm.grid(row=1, column=0)
btn_lg = tk.Button(w, text="Too Large", command=too_lg)
btn_lg.grid(row=1, column=1)
btn_corr = tk.Button(w, text="Correct!", command=corr)
btn_corr.grid(row=2, column=0, columnspan=2)
tk.Button(w, text="New Game", command=new_g).grid(row=3, column=0, columnspan=2)

l, h, a = 1, 100, 0
comp_guess()

w.mainloop()
