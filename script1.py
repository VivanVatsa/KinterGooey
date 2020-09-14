# import tkinter
from tkinter import *

# you create all the required business logic and widgets inside this two main entity functions
# form init of tk() before the end of mainloop()
window = Tk()

b1 = Button(window, text="Execute")
# b1.pack()
b1.grid(row=0, column=0)

e1 = Entry(window)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)


window.mainloop()
