from tkinter import *
from random import *

root = Tk()
root.title('Guess the word')
root.geometry('300x200')
frame = Frame(root)
frame.pack()

words = {'Programmer': 'программист',
         'University': 'университет',
         'Job': 'работа',
         'Car': 'машина',
         'Python': 'питон'}

def randChoice():
    global tr
    word, tr = choice(list(words.items()))
    lbl2.config(text = word)

def enterFunc():
    if tr == ent.get():
        lbl4.config(text = 'Guess',bg = 'green')
    else:
        lbl4.config(text = 'Error', bg = 'red')
def ex():
    exit()
    
lbl1 = Label(frame,text = 'Random word:',font='13')
lbl1.grid()

lbl2 = Label(frame,font=('13'),bg ='Green')
lbl2.grid()

lbl3 = Label(frame, text = 'enter the translation:',font='13')
lbl3.grid()

ent = Entry(frame,width = 30)
ent.grid()

lbl4 = Label(frame, text = '',font='13')
lbl4.grid()

but1 = Button(frame, text = 'Done',width = 14, height = 1, bg = 'black', fg = 'white',command = enterFunc)
but1.grid()

but2 = Button(frame, text = 'Exit',width = 14, height = 1, bg = 'black', fg = 'white', command=ex)
but2.grid()

randChoice()

root.mainloop()
