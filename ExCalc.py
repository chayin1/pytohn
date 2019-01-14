if text is None:
    pass
else:
    text += "meaningful"
print(text)

# Title: CodeLagos Progress - My Science App
# Author: Samuel Akintola
# Organization: Code Lagos 4.0
# Date: Monday, 10th December 2018

from tkinter import *
from math import *
#=====================================EXPRESSION CALCULATOR==============================================
top = Tk()
top.title("Sam's Expression Calculator")
Label(top, text="f(x) =").grid(row=0)
f = Entry(top)
f.grid(row=0, column=1)
Label(top, text="x =").grid(row=0, column=2)
e = Entry(top)
e.grid(row=0, column=3)
r = Entry(top)
r.grid(row=0, column=5)

def calc():
    r.delete(0, END)
    x = float(e.get())
    try:
                            y = eval(f.get())
    except:
                            y =  ("ERROR")
    r.insert(INSERT, y)
b = Button(top, text="Equals", command=calc)
b.grid(row=0, column=4)
top.mainloop()


