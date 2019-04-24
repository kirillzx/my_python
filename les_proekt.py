from tkinter import *
import math

def fun():
    global a
    try:
        a=(4/3)*round(math.pi,3)*(int(ent1.get()))**3
        text1.config(text=str(a))
    except ValueError:
        print('Ошибка!!! \nВведите число')
def writer():
    try:
        if v.get()=='Текст':
            with open('proekt.txt','w') as file:
                file.write(str(a))
        else:
            with open('proekt.html','w') as file:
                file.write(str(a))
    except Exception as e:
        print(e)
    
root=Tk()

root.title('Программа для вычисления объема сферы')
lbl1 = Label(root,text='Введите радиус:')
lbl1.grid(row=0,column=0)

lbl2=Label(root,text='Результат вычислений:')
lbl2.grid(row=1,column=0)

ent1=Entry(root)
ent1.grid(row=0,column=1)

text1=Label(root,width='15',height='1')
text1.grid(row=1,column=1)

btn1=Button(root,text='Вычислить',command=fun)
btn1.grid()
btn2=Button(root,text='Сохранить', cursor='heart', activebackground='green',command=writer)
btn2.grid(row=3,column=0)

v=StringVar()
v.set('Текст')

op=OptionMenu(root,v,'Текст','HTML')
op.grid(row=3,column=1)

root.mainloop()
