# Title: CodeLagos Progress - My Science App
# Author: Samuel Akintola
# Organization: Code Lagos 4.0
# Date: Monday, 10th December 2018

from tkinter import *
from math import *
import random
import time;

#======================================QUIZ CALCULATOR==============================================

root = Tk()
root.geometry('450x1000+5+5')
root.title (" QUIZ CALCULATOR")

text_Input = StringVar()
operator = ""

Tops = Frame (root, width = 500, height = 200,
              bg = "powder blue",relief = GROOVE)
Tops.pack   (side = TOP)

"""f1 = Frame (root, width = 655, height = 700,
              bg = "powder blue",relief = GROOVE)
f1.pack   (side = LEFT)"""

f1 = Frame (root, width = 50, height = 225,
              bg = "powder blue",relief = GROOVE)
f1.pack   (side = BOTTOM)

"""f3 = Frame (root, width = 100, height = 50,
              bg = "powder blue",relief = GROOVE)
f3.pack   (side = )"""
#======================================TITLE============================================
lblinfo = Label(Tops, font=('arial', 30, 'bold'), text ="QUIZ CALCULATOR",
                fg='gold', bd=10, anchor='w')
lblinfo.grid(row=0,column=0)
#=====================================TIME=========================================
localtime =time.asctime(time.localtime(time.time()))
#=====================================INFO==============================================
lblDateTime=Label(Tops,font=( 'arial', 20, 'bold'), text = localtime,fg = 'purple',
                bg ='red',bd = 10, anchor = 'w')
lblDateTime.grid (row = 1, column = 0)

#=====================================Calculator==============================================
def  btnClick(numbers):
        global  operator
        operator = operator + str(numbers)
        text_Input.set(operator)

def  btnClearDisplay():
        global  operator
        operator = " "
        text_Input.set(" ")

def  btnEqual():
        global  operator
        sumup=str(eval(operator))
        operator = " "
        text_Input.set(sumup)



"""def btnPoint():
        global  operator
        decimal=float(eval(operator))
        operator = " "
        text_Input.set(decimal)"""


txtDisplay = Entry (f1,font=('arial', 20,'bold'),textvariable=text_Input, bd=30, insertwidth=4,
                                   fg='Gold', bg='Steel Blue', justify='right')
txtDisplay.grid (columnspan = 4)

#===================================== 123+ ==============================================

btn1=Button(f1, padx=5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text="1", bg= "Steel Blue", command=lambda: btnClick(1)) . grid(row=2,column=0)


btn2=Button(f1, padx=5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text="2", bg= "Steel Blue", command=lambda: btnClick(2)) . grid(row=2,column=1)

btn3=Button(f1, padx=5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text="3", bg= "Steel Blue", command=lambda: btnClick(3)) . grid(row=2,column=2)

addition=Button(f1,  padx=5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text=" + ", bg= "Steel Blue", command=lambda: btnClick( '+' )) . grid(row=2,column=3)

#===================================== 456- ==============================================

btn4=Button(f1, padx=5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text="4", bg= "Steel Blue", command=lambda: btnClick(4)) . grid(row=3,column=0)

btn5=Button(f1, padx=5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text="5", bg= "Steel Blue", command=lambda: btnClick(5)) . grid(row=3,column=1)

btn6=Button(f1, padx=5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text="6", bg= "Steel Blue", command=lambda: btnClick(6)) . grid(row=3,column=2)

substraction=Button(f1, padx=5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text=" - ", bg= "Steel Blue", command=lambda: btnClick( ' - ' )) . grid(row=3,column=3)

#===================================== 789* ==============================================

btn7=Button(f1, padx=5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text="7", bg= "Steel Blue", command=lambda: btnClick(7)) . grid(row=4,column=0)

btn8=Button(f1, padx=5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text="8", bg= "Steel Blue", command=lambda: btnClick(8)) . grid(row=4,column=1)

btn9=Button(f1, padx=5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text="9", bg= "Steel Blue", command=lambda: btnClick(9)) . grid(row=4,column=2)

multiplication=Button(f1,  padx=5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text=" * ", bg= "Steel Blue", command=lambda: btnClick( '*' )) . grid(row=4,column=3)

#===================================== 0=/. ==============================================

btn0=Button(f1, padx=5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text="0", bg= "Steel Blue", command=lambda: btnClick(0)) . grid(row=5,column=0)

equal=Button(f1,  padx=5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text="=", bg= "Steel Blue", command=btnEqual) . grid(row=5,column=1)

division=Button(f1, padx=2.5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text=" / ", bg= "Steel Blue", command=lambda: btnClick(' / ')) . grid(row=5,column=2)

point=Button(f1,  padx=5, pady=5, bd=2.5, fg='gold',font=('arial', 20,'bold'),
                         text=" . ", bg= "Steel Blue", command=lambda: btnClick('.')) . grid(row=5,column=3)

#===================================== C^( ) ==============================================

btnClear=Button(f1, padx=0.5, pady=0.5, bd=1, fg='gold',font=('arial', 20,'bold'),
                         text=" C ", bg= "Steel Blue", command=btnClearDisplay) . grid(row=6,column=0)

percentage=Button(f1, padx=0.5, pady=0.5, bd=1, fg='gold',font=('arial', 20,'bold'),
                         text=" % ", bg= "Steel Blue", command=lambda: btnClick(' % ')) . grid(row=6,column=1)

opeBracket=Button(f1,  padx=0.5, pady=0.5, bd=1, fg='gold',font=('arial', 20,'bold'),
                         text=" ( ", bg= "Steel Blue", command=lambda: btnClick(' ( ')) . grid(row=6,column=2)

cloBracket=Button(f1,  padx=0.5, pady=0.5, bd=1, fg='gold',font=('arial', 20,'bold'),
                         text=" ) ", bg= "Steel Blue", command=lambda: btnClick( ' ) ' )) . grid(row=6,column=3)

#===================================== END ==============================================
root.mainloop()

