from tkinter import *
window = Tk()
window.title("Simple frame")
window.geometry('300x200')

border_effect = [FLAT,SUNKEN,RAISED,GROOVE,RIDGE]

for r in border_effect :
    frame  = Frame(master=window , relief=r , borderwidth=5 )
    frame.pack(side=LEFT)
    label = Label(master=frame,text=r)
    label.pack()
window.mainloop()