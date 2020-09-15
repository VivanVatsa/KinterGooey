# import tkinter
from tkinter import *

# you create all the required business logic and widgets inside this two main entity functions
# form init of tk() before the end of mainloop()
window = Tk()


def km_2_miles():
    # print("Success!")
    print(e1_value.get())
    miles = e1_value.get()*1.6
    t1.insert(END,miles)
b1 = Button(window, text="Execute", command=km_2_miles)
# b1.pack()
b1.grid(row=0, column=0)

e1_value= StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()
