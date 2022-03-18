from tkinter import *
#from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("AEMS panel")
#root.iconbitmap('/Users/hoyeungching/Desktop/logo.ico')
root.geometry("400x400")

def clickStartRec():
    statusBox.delete(0, END)
    statusBox.insert(0, "Recording inprogress...")
    messagebox.showinfo("Info", "Recording Started!")

def clickStopRec():
    response1 = messagebox.askyesno("Warning", "Stop Recording?")
    if response1:
        statusBox.delete(0, END)
        statusBox.insert(0, "Recording saved!")

#e = Entry(root, width=50, fg="white", bg="blue", borderwidth = "5")
#e.pack()
#e.insert(0, "Enter the command")

temperatureLabel = Label(root, text = "Current Temp")
humidityLabel = Label(root, text = "Current Humi")

statusBox = Entry(root, width=40,fg="white", bg="blue", borderwidth = "5")
temperatureBox = Entry(root, width=10, borderwidth = "5")
humidityBox = Entry(root, width=10, borderwidth = "5")

temperatureBox.insert(0, "0 C")
humidityBox.insert(0, "0 %")

startRecButton = Button(root, text="Start Rec", padx=40, pady=20, command=clickStartRec, fg="red")
stopRecButton = Button(root, text="Stop Rec", padx=40, pady=20, command=clickStopRec, fg="green")

startRecButton.grid(row=1, column=0)
stopRecButton.grid(row=1, column=1)
statusBox.grid(row=0, column=0, columnspan=2)
temperatureBox.grid(row=3, column=0)
humidityBox.grid(row=3, column=1)
temperatureLabel.grid(row=2, column=0)
humidityLabel.grid(row=2, column=1)

root.mainloop()