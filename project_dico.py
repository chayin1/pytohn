#MeDictionary

#import the gui 
from tkinter import *

#describe window
window=Tk()
window.title("Concise Medi-Dictionary")
window.configure(background="black", width=15)



#Header logo
pic1=PhotoImage(file="C:/Users/HP/Contacts/Desktop/Medico/Untitled-1.gif")
Label(window, image=pic1, bg="white").grid(row=0, column=0, sticky=W)

#Notification for user to enter text
Label(window, text="Enter Word", width=8, bg="black", fg="white", font="helvetica 10 bold").grid(row=2, column=0, sticky=W)

#Textbox
textentry=Entry(window, width=15, bg="white")
textentry.grid(row=3, column=0, sticky=W)



#define button click funtion
def click():
    text_inp=textentry.get() #to get the text entered by the user
    defbox.delete(0.0, END)
    try:
        definition = disp_def[text_inp]
    except:
        definition="definition not available at the moment"
    defbox.insert(END,definition)
    
#Submit Button
Button(window, text="Check Meaning", font="helvetica 8", width=12, command=click).grid(row=4, column=0, sticky=W)

Label(window, width=30, bg="black").grid(row=5, column=0, sticky=W)

#Notification for user to view meaning
Label(window, text="DEFINITION", bg="black", fg="white", font="helvetica 12 bold").grid(row=6, column=0, sticky=W)

#Definition Box
defbox=Text(window, width=40, height=10, bg="white", wrap=WORD)
defbox.grid(row=7, column=0, columnspan=2)

#the dictionary
disp_def={
    'medicine':'field in human endeavour that deals with the study of human health',
    'drug':'substance taken to relieve a declining health condition or restore one to health',
    'doctor':'professional in the field of medicine who treats sick indiviuals'
}

#Exit button
Button(window, text="Close Window", width="13", command=window.destroy).grid(row=8, column=0, sticky=E)

window.mainloop()
