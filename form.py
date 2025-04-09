from tkinter import *
from datetime import date

root = Tk()
root.title('Gettng started with widgets')
root.geometry('400x300')

lbl = Label(text = "Hey there", fg = "white", bg = "#f2ee00" ,height=  1 , width = 300  )
name_lbl = Label(text = "Full name", bg = "#0ef5ee" )
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message  = "Welcome to the aplication \n  Todays date is:"
    greet = "Hello"+name+"\n"

    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END, date.today())

text_box = Text(height = 3)
btn = Button(text = "begin" , command = display , height = 1 , bg = "#f8640a" , fg = "white")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()