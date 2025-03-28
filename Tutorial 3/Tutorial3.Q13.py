"""13.	Write GUI program to compute and displays the square root of an input number."""

import tkinter as tk
from tkinter import messagebox
import math

def compute_sqrt():
    try:
        num = float(entry_number.get())
        if num < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        sqrt_result = math.sqrt(num)
        entry_sqrt.delete(0, tk.END)
        entry_sqrt.insert(0, f"{sqrt_result:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid non-negative number.")

# Create main window
window = tk.Tk()
window.title("Square Root Calculator")

label_number = tk.Label(window, text="Enter Number:")
label_number.grid(row=0, column=0)
entry_number = tk.Entry(window)
entry_number.grid(row=0, column=1)

label_sqrt = tk.Label(window, text="Square Root:")
label_sqrt.grid(row=1, column=0)
entry_sqrt = tk.Entry(window)
entry_sqrt.grid(row=1, column=1)

button_compute = tk.Button(window, text="Compute Square Root", command=compute_sqrt)
button_compute.grid(row=2, column=0, columnspan=2)

window.mainloop()
