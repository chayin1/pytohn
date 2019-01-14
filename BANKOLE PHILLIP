# Title: A MINI STAFF RECORD MANAGEMENT SYSTEM
# Author: BANKOLE, PHILIP AJIBOLA
# Organization: Code Lagos 5.0
# Date: 11-12-2018

from tkinter import *
from tkinter import messagebox
import os
f=open("Philip_Bankole",'a+')
root = Tk()
root.title(" BANKOLE PHILIP AJIBOLA (B.P.A) MINI STAFF RECORD  MANAGEMENT  SYSTEM")
root.configure(width=1700,height=700,bg='red')
var=-1

def addstaff():
    global var
    num_lines = 0
    with open("Philip_Bankole", 'r') as f10:
        for line in f10:
            num_lines += 1
    var=num_lines-1
    b1=entry1.get()
    b2=entry2.get()
    b3=entry3.get()
    b4=entry4.get()
    b5=entry5.get()
    f.write('{0} {1} {2} {3} {4}\n'.format(str(b1),b2,b3,str(b4),b5))
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)


def deletestaff():
    b1=entry1.get()
    with open(r"Philip_Bankole") as f, open(r"Philip_Bankole1", "w") as working:
        for line in f:
            if str(b1) not in line:
                working.write(line)
    os.remove(r"Philip_Bankole")
    os.rename(r"Philip_Bankole1", r"Philip_Bankole")
    f.close()
    working.close()
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

def firststaff():
    global var
    var=0
    f.seek(var)
    c=f.readline()
    v=list(c.split(" "))
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry1.insert(0,str(v[0]))
    entry2.insert(0,str(v[1]))
    entry3.insert(0,str(v[2]))
    entry4.insert(0,str(v[3]))
    entry5.insert(0,str(v[4]))
    print(first_line)
    
def nextstaff():
    global var
    var = var + 1
    f.seek(var)
    try:
        c=f.readlines()
        xyz = c[var]
        v = list(xyz.split(" "))
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry1.insert(0, str(v[0]))
        entry2.insert(0, str(v[1]))
        entry3.insert(0, str(v[2]))
        entry4.insert(0, str(v[3]))
        entry5.insert(0, str(v[4]))
    except:
        messagebox.showinfo("Title", "SORRY!...STAFF RECORDS LIST EXHAUSTED")
def previousstaff():
        global var
        var=var-1
        f.seek(var)
        try:
            z = f.readlines()
            xyz=z[var]
            v = list(xyz.split(" "))
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)

            entry1.insert(0, str(v[0]))
            entry2.insert(0, str(v[1]))
            entry3.insert(0, str(v[2]))
            entry4.insert(0, str(v[3]))
            entry5.insert(0, str(v[4]))
        except:
            messagebox.showinfo("Title", "SORRY!...STAFF RECORDS LIST EXHAUSTED")

def laststaffrecord():
    global var
    f4=open("Philip_Bankole",'r')
    x=f4.read().splitlines()
    last_line= x[-2]
    num_lines = 0
    with open("Philip_Bankole", 'r') as f8:
        for line in f8:
            num_lines += 1
    var=num_lines-1
    print(last_line)
    try:
        v = list(last_line.split(" "))
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)

        entry1.insert(0, str(v[0]))
        entry2.insert(0, str(v[1]))
        entry3.insert(0, str(v[2]))
        entry4.insert(0, str(v[3]))
        entry5.insert(0, str(v[4]))
    except:
        messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")


def updatestaffrecord():

    b1 = entry1.get()
    b2 = entry2.get()
    b3 = entry3.get()
    b4 = entry4.get()
    b5 = entry5.get()
    with open(r"Philip_Bankole") as f1, open(r"Philip_Bankole1", "w") as working:
        for line in f1:
            if str(b1) not in line:
                working.write(line)
            else:
                working.write('{0} {1} {2} {3} {4}'.format(str(b1), b2, b3, str(b4), b5))
    os.remove(r"Philip_Bankole")
    #CODES LAGOS PROGRAM HAS ENHANCED ME EFFECTIVELY TO COME OUT  WITH THIS DESIGN UNDER THE FACILITATOR MR GODDY, AT CHRIST INT'L MINISTRY CENTRE, ABARANJE IKOTUN, LAGOS
    os.rename(r"Philip_Bankole1", r"Philip_Bankole")


def searchstaffrecord():
    i=0
    b11 = entry1.get()
    with open(r"Philip_Bankole") as working:
        for line in working:
            i=i+1
            if str(b11) in line:
                break
        try:
            v = list(line.split(" "))
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry1.insert(0, str(v[0]))
            entry2.insert(0, str(v[1]))
            entry3.insert(0, str(v[2]))
            entry4.insert(0, str(v[3]))
            entry5.insert(0, str(v[4]))
        except:
            messagebox.showinfo("Title", "error end of file")
    working.close()


def clearstaffrecord():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
   
#
label0= Label(root,text="BPA, MINI STAFF RECORD MANAGEMENT SYSTEM",bg="white",fg="blue",font=("ALGERIAN",40))
label1=Label(root,text="ENTER STAFF NAME",bd="12", bg="black",relief="ridge",fg="white",font=("Book Antiqua", 13),width=40)
entry1=Entry(root , font=("Times", 12))
label2=Label(root, text="ENTER STAFF PF NUMBER",bd="12",relief="ridge",height="1",bg="black",fg="white", font=("Book Antiqua", 13),width=40)
entry2= Entry(root, font=("Times", 12))
label3=Label(root, text="ENTER STAFF RANK",bd="12",relief="ridge",bg="black",fg="white", font=("Book Antiqua", 13),width=40)
entry3= Entry(root, font=("Times", 12))
label4=Label(root, text="STAFF CATEGORY(ACADEMIC/NON ACADEMIC)",bd="12",relief="ridge",bg="black",fg="white", font=("Book Antiqua", 11),width=45)
entry4= Entry(root, font=("Times", 12))
label5=Label(root, text="ENTER STAFF OFFICE NUMBER", bd="12", bg="black",relief="ridge",fg="white", font=("Book Antiqua", 13),width=40)
entry5= Entry(root, font=("Times", 12))
button1= Button(root, text="ADD STAFF RECORD", bg="white", fg="blue", width=28, font=("Times", 13),command=addstaff)
button2= Button(root, text="DELETE STAFF RECORD", bg="white", fg="blue", width =28, font=("Times", 13),command=deletestaff)
button3= Button(root, text="VIEW FIRST STAFF RECORD" , bg="white", fg="blue", width =27, font=("Times", 13),command=firststaff)
button4= Button(root, text="VIEW NEXT STAFF RECORD" , bg="white", fg="blue", width =28, font=("Times", 13), command=nextstaff)
button5= Button(root, text="VIEW PREVIOUS STAFF RECORD", bg="white", fg="blue", width =28, font=("Times", 13),command=previousstaff)
button6= Button(root, text="VIEW LAST STAFF RECORD", bg="white", fg="blue", width =28, font=("Times", 13),command=laststaffrecord)
button7= Button(root, text="UPDATE STAFF RECORD", bg="white", fg="blue", width =28, font=("Times", 13),command=updatestaffrecord)
button8= Button(root, text="SEARCH FOR STAFF", bg="white", fg="blue", width =28, font=("Times", 13),command=searchstaffrecord)
button9= Button(root, text="CLEAR SCREEN", bg="white", fg="black", width=28, font=("ALGERIAN", 11),command=clearstaffrecord)
label0.grid(columnspan=6, padx=10, pady=10)
label1.grid(row=1,column=0, sticky=W, padx=10, pady=10)
label2.grid(row=2,column=0, sticky=W, padx=10, pady=10)
label3.grid(row=3,column=0, sticky=W, padx=10, pady=10)
label4.grid(row=4,column=0, sticky=W, padx=10, pady=10)
label5.grid(row=5,column=0, sticky=W, padx=10, pady=10)
entry1.grid(row=1,column=1, padx=40, pady=10)
entry2.grid(row=2,column=1, padx=10, pady=10)
entry3.grid(row=3,column=1, padx=10, pady=10)
entry4.grid(row=4,column=1, padx=10, pady=10)
entry5.grid(row=5,column=1, padx=10, pady=10)
button1.grid(row=1,column=4, padx=40, pady=10)
button2.grid(row=1,column=5, padx=40, pady=10)
button3.grid(row=2,column=4, padx=40, pady=10)
button4.grid(row=2,column=5, padx=40, pady=10)
button5.grid(row=3,column=4, padx=40, pady=10)
button6.grid(row=3,column=5, padx=40, pady=10)
button7.grid(row=4,column=4, padx=40, pady=10)
button8.grid(row=4,column=5, padx=40, pady=10)
button9.grid(row=5,column=5, padx=40, pady=10)
root.mainloop()
