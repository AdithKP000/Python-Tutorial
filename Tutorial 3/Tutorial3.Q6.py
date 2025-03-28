"""6.	Write a GUI program to convert an input string to uppercase and displays the result."""

import tkinter as tk

def convert_to_upper():
    text = input_entry.get()
    result_label.config(text=text.upper())

root = tk.Tk()
root.title("Uppercase Converter")


tk.Label(root, text="Enter Text:").grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(root, width=30)
input_entry.grid(row=0, column=1, padx=10, pady=10)
convert_btn = tk.Button(root, text="Convert", command=convert_to_upper)
convert_btn.grid(row=1, column=0, columnspan=2, pady=10)
result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
result_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
