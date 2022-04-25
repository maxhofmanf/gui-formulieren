from msilib.schema import CheckBox
import tkinter as tk
from tkinter import *
window = tk.Tk()
counter = tk.IntVar(0)
count=0
stat = True
aanofuit = IntVar()

def double(e):
    global count
    if stat == True:
        count*=3
        counter.set(count)
    else:
        count/=3
        counter.set(count)

def enter(e):
    window['bg']='yellow'
def marked():
    global count
    if aanofuit.get() == 1:
        if stat == True:
            Click1()
        elif stat == False:
            Click2()
        window.after(5000,marked)
s


def up(e):
    Click1()
def Click1():
    global count, stat
    stat = True
    count += 1
    counter.set(count)
    background2()

def down(e):
    Click2()
def Click2():
    global count,stat
    stat = False
    count -=1
    counter.set(count)
    background2()

box1 = tk.Label(window,textvariable= counter,width = 9,height = 2)

def background1(e):
    background2()
def background2():
    if counter.get() > 0 :
        window['bg']= 'green'
        
    elif counter.get() < 0:
        window['bg']='red'
        
    else:
        window['bg']='gray'



checkbox = tk.Checkbutton(window,text='autoclicker',variable= aanofuit,onvalue=1,offvalue=0,command=marked).pack()

btn1= tk.Button(text='+' ,bg="white", fg="black", padx = 30 , pady = 10, command= Click1)
btn2= tk.Button(text='-' ,bg="white", fg="black", padx = 30 , pady = 10, command= Click2)
btn1.pack()
box1.pack()
btn2.pack()
box1.bind('<Enter>',enter)
box1.bind('<Leave>',background1)
box1.bind('<Double-Button-1>',double)
window.bind('<Up>', up) and window.bind('<+>', up) 
window.bind('<Down>',down) and window.bind('-',down)
window.bind('<space>',double)
window.mainloop()