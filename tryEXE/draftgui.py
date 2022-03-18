from tkinter import *
#from PIL import ImageTk, Image

root = Tk()
root.title("AEMS panel")
#root.iconbitmap('/Users/hoyeungching/Desktop/logo.ico')

def clickStartRec():
    messageBox.delete(0, END)
    messageBox.insert(0, "Recording inprogress")

def clickStopRec():
    messageBox.delete(0, END)
    messageBox.insert(0, "Recording savedp")

#e = Entry(root, width=50, fg="white", bg="blue", borderwidth = "5")
#e.pack()
#e.insert(0, "Enter the command")

messageBox = Entry(root, width=40,fg="white", bg="blue", borderwidth = "5")

startRecButton = Button(root, text="Start Rec", padx=40, pady=20, command=clickStartRec, fg="red")
stopRecButton = Button(root, text="Stop Rec", padx=40, pady=20, command=clickStopRec, fg="green")

startRecButton.grid(row=1, column=0)
stopRecButton.grid(row=1, column=1)
messageBox.grid(row=0, column=0, columnspan=2)

root.mainloop()