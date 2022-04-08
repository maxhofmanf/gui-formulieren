import random
import tkinter as tk
from tkinter import END, Entry, StringVar, messagebox as mb
window=tk.Tk()
points= tk.IntVar(0)
point = 0
points.set(f'points = {point}')
timer = tk.IntVar(0)
nameText = StringVar()

def begin():
    global time,blaster
    blaster= enter.get()
    blaster= int(blaster)
    time = blaster  
    enter.destroy()
    newbutton()

def newbutton():
    global targetbox, num1, num2,keuzes,targetText
    Btn1.destroy()
    keuzes = [['<w>','<a>','<s>','<d>','<space>'],['<Button>','<Double-Button>','<Triple-Button>']]
    num1 = random.randint(0,1)
    num2=random.randint(0,len(keuzes[num1])- 1)
    name = keuzes[num1][num2]
    targetText(name)
    targetbox = tk.Label(window,textvariable= nameText,bg = 'white')
    targetbox.place(x=random.randrange(20,600), y = random.randrange(20,470))
    if num1 == 0:
        window.bind(keuzes[num1][num2],targetHit)
    else:
        targetbox.bind(keuzes[num1][num2],targetHit)
    targetText(name)

def targetText(name):
    global nameText
    if name == '<w>':
        nameText.set('press w')
    elif name =='<a>':
        nameText.set('press a')
    elif name =='<s>':
        nameText.set('press s')
    elif name =='<d>':
        nameText.set('press d')
    elif name =='<space>':
        nameText.set('press space')
    elif name =='<Button>':
        nameText.set('click')
    elif name =='<Double-Button>':
        nameText.set('double click')
    elif name =='<Triple-Button>':
        nameText.set('triple click')


def clock():
    global timer, time
    
    time -= 1
    timer.set(f'{time} seconds left')
    if time != 0:
        window.after(1000,clock)
    else:
        clockdone()

def clockdone():
    global points, time
    answer = mb.askyesno('want to play again?',f'final score = {point} \nWould you like to play again ')
    targetbox.destroy()
    if answer:
        points=0

        startbtn()

    else:
        window.destroy()
def targetHit(e):
    global point,points
    targetbox.destroy()
    
    
    if num1 == 0:
        window.unbind(keuzes[num1][num2])
        point += 1
    else:
        point += 2
    points.set(f'points = {point}')
    newbutton()


def start():
    window.after(1000,clock)
    begin()


window.geometry('700x500')
def startbtn():
    global Btn1, point ,enter

    point = 0
    Btn1 = tk.Button(text = 'Press here to start', command = start)
    Btn1.place(x = 300, y = 0)
    enter = tk.Entry()
    enter.insert(END,'20')
    enter.place (x = 290, y = 30)
    


box2=tk.Label(textvariable=points,width = 9, height =0)
box2.place(x=500,y=2)

box3= tk.Label(textvariable= timer,width = 10, height = 0)
box3.place(x=200,y=2)
startbtn()
window.mainloop()