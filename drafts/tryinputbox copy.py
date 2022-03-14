from tkinter import *

root = Tk()

e = Entry(root, width=50, fg="white", bg="blue", borderwidth = "5")
e.pack()
e.insert(0, "enter our name:")

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButton = Button(root, text="enter your name:", command=myClick)
myButton.pack()

root.mainloop()