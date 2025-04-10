from tkinter import *
window = Tk()
window.title('Number pad')
window.geometry('300x200')

nums = [[9,8,7],[6,5,4],[3,2,1],['#',0,'*']]

for i in range(4):
    window.columnconfigure(i, weight = 1 , minsize = 125)
    window.columnconfigure(i, weight = 1 , minsize = 100)

    for j in range(0 , 3 ):
        frame = Frame(
            master=window,
            relief = SUNKEN,
            borderwidth = 1
        )
        frame.grid(row=i,column=j)
        label = Label(master=frame , text=nums [i][j], bg="#f3db6f")
        label.pack(padx=3 , pady=3)
window.mainloop()