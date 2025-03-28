""" 4.	Write a GUI based program that allows the user to convert temperature values between degrees Fahrenheit and degrees Celsius.  The interface should have labeled entry fields for these two values. 
These components should arrange in a grid where the labels occupy the first row and the corresponding field occupy the second row. At start up the Fahrenheit field should contain 32 and the Celsius field
contain 0.0.The third row in the window contain two command buttons ,
labeled >>>> and <<<<.When the user presses the first button, the program should use the data in the Fahrenheit field to compute the Celsius value, which should then be output to the Celsius field.
The second button should perform the inverse function"""
import tkinter as tk

def f_to_c():
    f = float(f_entry.get())
    c = (f - 32) * 5 / 9
    c_entry.delete(0, tk.END)
    c_entry.insert(0, f"{c:.2f}")

def c_to_f():
    c = float(c_entry.get())
    f = (c * 9 / 5) + 32
    f_entry.delete(0, tk.END)
    f_entry.insert(0, f"{f:.2f}")

root = tk.Tk()
root.title("Temperature Converter")

f_label = tk.Label(root, text="Fahrenheit:")
c_label = tk.Label(root, text="Celsius:")
f_label.grid(row=0, column=0)
c_label.grid(row=0, column=1)

f_entry = tk.Entry(root)
c_entry = tk.Entry(root)
f_entry.grid(row=1, column=0)
c_entry.grid(row=1, column=1)

f_entry.insert(0, "32")
c_entry.insert(0, "0.0")

btn_fc = tk.Button(root, text=">>>>", command=f_to_c)
btn_cf = tk.Button(root, text="<<<<", command=c_to_f)
btn_fc.grid(row=2, column=0)
btn_cf.grid(row=2, column=1)

root.mainloop()
