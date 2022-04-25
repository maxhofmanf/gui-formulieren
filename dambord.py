from operator import truediv
import tkinter as tk
from tkinter import ttk

window= tk.Tk()
window.geometry("600x600")
color = "black"

m = False
for x in range(10):
    if m == True:
        m= False
    else:
        m = True
    for y in range(10):
        if m == True:
            color = "black"
            m= False
        else:
            color= "white"
            m = True
        block = tk.Label(window, bg = color,padx=20, pady=10)
        block.grid(column= x,row= y)
window.mainloop()