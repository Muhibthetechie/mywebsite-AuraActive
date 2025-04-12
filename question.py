from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry('200x200')

def msg():
    messagebox.askquestion('Question Box', 'Do you want to contenue?')
button = Button(root , text="Question", command=msg)
button.place(x=40, y=80)
root.mainloop()