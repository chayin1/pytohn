'''
Author: Itua Austin Junior
'''
#Title: Project

from tkinter import *

root = Tk()
root.geometry('1000x1000')
root.title('Voters Registration Form')

label_0 = Label(root, text = 'Voters Registration Form', fg = 'green', width = 20, font = ('bold', 20))
label_0.place(x = 90, y = 53)

label_1 = Label(root, text = 'Full Name', width = 10, font = ('bold', 10))
label_1.place(x = 80, y = 130)

entry_1 = Entry(root)
entry_1.place(x = 240, y = 130)

label_2 = Label(root, text = 'Date of Birth', width = 10, font =('bold', 10))
label_2.place(x = 70, y = 180)

entry_2 = Entry(root)
entry_2.place(x = 240, y = 180)

label_3 = Label(root, text = 'Email(optional)', width = 10, font = ('bold', 10))
label_3.place(x = 80, y = 200)

entry_3 = Entry(root)
entry_3.place(x = 250, y = 200)

label_4 = Label(root, text = 'Gender', width = 10, font = ('bold', 10))
label_4.place(x = 70, y = 230)
var = IntVar()
Radiobutton(root, text = 'Male', padx = 5, variable = var, value = 1).place(x = 235, y = 230)
Radiobutton(root, text = 'Female', padx = 20, variable = var, value = 2).place(x = 290, y = 230)

label_5 = Label(root, text = 'Local Government', width = 40, fg = 'blue', font = ('bold', 10))
label_5.place(x = 8, y = 280)

list1 = ['Alimisho', 'Kosofe', 'Mushin', 'Oshodi', 'Ikorodu', 'Surulere', 'Agege', 'Alimosho', 'Ikeja'];
c = StringVar()
droplist = OptionMenu(root, c, *list1)
droplist.config(width = 30)
c.set('select your Local Government')
droplist.place(x = 300, y = 280)

label_5 = Label(root, text = 'Political Party', width = 40, fg = 'blue', font = ('bold', 10))
label_5.place(x = 10, y = 325)

list1 = ['AD', 'APC', 'APGA', 'DPA', 'DPP', 'FDP', 'LP', 'NCP', 'PDP','PPA'];
c = StringVar()
droplist = OptionMenu(root, c, *list1)
droplist.config(width = 25)
c.set('select your political party')
droplist.place(x = 325, y = 325)

Button(root, text = 'Submit', bg = 'white', width = 40,  command = root.destroy).place(x = 180, y = 380)

root.mainloop()
