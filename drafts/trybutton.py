from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="hahahaha")
    myLabel.pack()

myButton = Button(root, text="click here", command=myClick, fg="blue")
myButton.pack()

root.mainloop()