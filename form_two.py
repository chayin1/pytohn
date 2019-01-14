from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Registration Form")

label_0 = Label(root, text="Registration form",width=20,font=("bold",20))
label_0.place(x=90,y=20)

label_1 = Label(root, text="Firstname",width=20,font=("bold",10))
label_1.place(x=75,y=70)

entry_1 = Entry(root)
entry_1.place(x=240,y=70)

label_1a = Label(root, text="Middlename",width=20,font=("bold",10))
label_1a.place(x=80,y=110)

entry_1a = Entry(root)
entry_1a.place(x=240,y=110)

label_1b = Label(root, text="Lastname",width=20,font=("bold",10))
label_1b.place(x=75,y=150)

entry_1b = Entry(root)
entry_1b.place(x=240,y=150)

label_2 = Label(root, text="Email",width=20,font=("bold",10))
label_2.place(x=68,y=195)

entry_2 = Entry(root)
entry_2.place(x=240,y=195)

label_3 = Label(root, text="Gender",width=20,font=("bold",10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230) 
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Country",width=20,font=("bold",10))
label_4.place(x=70,y=280)

list1 = ['Australia','Belgium','Canada','Denmark','Ethopia','Finland','Nigeria'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=20)
c.set('Select your Country')
droplist.place(x=240,y=280)

label_4 = Label(root, text="Programming",width=20,font=("bold",10))
label_4.place(x=85,y=330)
var1 = IntVar()
Checkbutton(root, text="java", variable=var1).place(x=235,y=330)
var2 = IntVar ()
Checkbutton(root, text="python", variable=var2).place(x=290,y=330)              

Button(root, text='Submit',width=20,bg='brown',fg='white', command=root.destroy).place(x=180,y=380)

root.mainloop ()              
