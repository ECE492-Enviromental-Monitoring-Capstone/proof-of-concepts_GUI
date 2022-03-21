# -------------------------------------------------------------------------------------
# ECE 492 Winter 2022
# Acoustic and Evironment Monitoring System Project
# Desktop Controller App
# -------------------------------------------------------------------------------------
from tkinter import *
#from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
#import bluetooth
#nearby_devices = bluetooth.discover_devices()
import threading
import time
import fakeParameters
import datetime
import os

# Main Window
root = Tk()
root.title("AEMS panel")
#root.iconbitmap('/Users/hoyeungching/Desktop/logo.ico')
root.geometry("800x400")

# ---[Function Definitions]------------------------------------------------------------------------------------
def clickStartRec():
    global presetTime
    presetTime = 360*float(LoggingHourBox.get()) + 60*float(LoggingMinBox.get()) + float(LoggingSecBox.get())
    global loggingStartTime
    loggingStartTime = time.time()
    messagebox.showinfo("Info", "Recording Started!")
    statusBox.delete(0, END)
    statusBox.config(bg="red")
    statusBox.insert(0, "Rec in progress...")
    threading.Thread(target=recording).start()

def clickStopRec():
    response1 = messagebox.askyesno("Warning", "Stop Recording?")
    if response1:
        statusBox.config(bg="green")
        statusBox.delete(0, END)
        statusBox.insert(0, "Recording of {} saved!".format(str(time.time()-loggingStartTime)))
    presetTime = 0

def openDebugTerminal():
    topWindow = Toplevel()
    topWindow.title("Debug Terminal")
    topWindow.geometry("650x400")
    textTerminal = Text(topWindow, width=80, height=20, fg="white", bg="black")
    textTerminal.pack()

def openBluetoothList():
    global topWindow2
    topWindow2 = Toplevel()
    topWindow2.title("Discover Bluebooth Device...")
    global deviceList
    deviceList = Listbox(topWindow2)
    refreshBlueButton = Button(topWindow2, text="Refresh", command = refreshBlueList)
    connectBlueButton = Button(topWindow2, text="Connect", command = connectToBlueDevice)
    for i in fakeParameters.getFakeBlueList():
        deviceList.insert(END, i)
    deviceList.pack()
    refreshBlueButton.pack()
    connectBlueButton.pack()

def refreshBlueList():
    deviceList.delete(0, END)
    for i in fakeParameters.getFakeBlueList():
        deviceList.insert(END, i)

def connectToBlueDevice():
    global currentDeviceName
    currentDeviceName = deviceList.get(ANCHOR)
    messagebox.showinfo("Info", "Connected to " + currentDeviceName)
    topWindow2.destroy()
    connectionStatusBox.config(bg="green")
    connectionStatusBox.delete(0, END)
    connectionStatusBox.insert(0, "Connected to " + currentDeviceName)

def disconToBlueDevice():
    messagebox.showinfo("Info", "Disconnected from " + currentDeviceName)
    connectionStatusBox.config(bg="red")
    connectionStatusBox.delete(0, END)
    connectionStatusBox.insert(0, "Not Connected")

def recording():
    # update logging status
    while (time.time() - loggingStartTime) < presetTime:
        statusBox.delete(0, END)
        statusBox.config(bg="red")
        statusBox.insert(0, "Rec in progress... " + str(int((time.time()-loggingStartTime)*100/presetTime)) + "%" + " finished")
        time.sleep(0.5)
    # logging times up
    statusBox.config(bg="green")
    statusBox.delete(0, END)
    statusBox.insert(0, "Recording of {} saved!".format(str(datetime.timedelta(seconds=(presetTime)))))

def realTimeUpdateMeasurement():
    while True:
        # update temp
        temperatureBox.delete(0, END)
        temperatureBox.insert(0, str(fakeParameters.getFakeTemp()) + " ˚C")

        # update humi
        humidityBox.delete(0, END)
        humidityBox.insert(0, str(fakeParameters.getFakeHumi()) + " %")

        # update lumi
        luminosityBox.delete(0, END)
        luminosityBox.insert(0, str(fakeParameters.getFakeLumi()) + " W")
                
        # frequency
        time.sleep(1)

# ---[Setup widegts]----------------------------------------------------------------------------------
# Device connection
openBlueButton = Button(root, text = "Discover", command=openBluetoothList)
connectionStatusBox = Entry(root, width=20, borderwidth="5", fg="white", bg="red")
connectionStatusBox.insert(0, "Not Connected")
disconBlueButton = Button(root, text="Disconnect", command = disconToBlueDevice)

# Dynamic data
dataFrame = LabelFrame(root, text="Current Data", padx=20, pady=60)

# temperature
temperatureLabel = Label(root, text = "Current Temp")
temperatureBox = Entry(root, width=10, borderwidth = "5")
temperatureBox.insert(0, str(fakeParameters.getFakeTemp()) + " C")

# humidity
humidityLabel = Label(root, text = "Current Humi")
humidityBox = Entry(root, width=10, borderwidth = "5")
humidityBox.insert(0, str(fakeParameters.getFakeHumi()) + " %")

# luminosity
luminosityLabel = Label(root, text = "Current Lumin")
luminosityBox = Entry(root, width=10, borderwidth="5")
luminosityBox.insert(0, str(fakeParameters.getFakeLumi()) + " W")

# USmic Rec
statusBox = Entry(root, width=25,fg="white", bg="blue", borderwidth = "5")
statusBox.insert(0, "Welcome to AEMS!")
startRecButton = Button(root, text="Start Rec", padx=30, pady=15, command=clickStartRec, fg="green")
stopRecButton = Button(root, text="Stop Rec", padx=30, pady=15, command=clickStopRec, fg="red")
LoggingTimeLabel = Label(root, text = "Set Recording Time")
loggingSecLabel = Label(root, text = "sec")
LoggingSecBox = Entry(root, width=20, borderwidth="5")
loggingMinLabel = Label(root, text="min")
LoggingMinBox = Entry(root, width=20, borderwidth="5")
loggingHourLabel = Label(root, text="hrs")
LoggingHourBox = Entry(root, width=20, borderwidth="5")

# Show debug terminal
openTerminalButton = Button(root, text="Open Debug Terminal", command=openDebugTerminal)

# picture
pictureTextBox = Text(root, width = 90, height = 10)
labelImage = PhotoImage(file="./label.png")
pictureTextBox.image_create(END, image=labelImage)

# ---[Positioning widgets]---------------------------------------------------------------------------------------
pictureTextBox.grid(row=0, column=1, columnspan=5)
# connection part
connectionStatusBox.grid(row=1, column=1)
openBlueButton.grid(row=1, column=2)
disconBlueButton.grid(row=1, column=3)
openTerminalButton.grid(row = 1, column = 4)

# rec part
statusBox.grid(row=3, column=4, columnspan=1)
LoggingTimeLabel.grid(row=4, column = 4)
LoggingHourBox.grid(row=5, column = 4, columnspan=2)
loggingHourLabel.grid(row=5, column = 6)
LoggingMinBox.grid(row=6, column = 4, columnspan=2)
loggingMinLabel.grid(row=6, column=6)
LoggingSecBox.grid(row=7, column=4, columnspan=2)
loggingSecLabel.grid(row=7, column=6)
startRecButton.grid(row = 8, column = 4)
stopRecButton.grid(row = 8, column = 5)

# measurement part
temperatureLabel.grid(row=3, column=1)
temperatureBox.grid(row=3, column=2)
humidityLabel.grid(row=4, column=1)
humidityBox.grid(row=4, column=2)
luminosityLabel.grid(row=5, column=1)
luminosityBox.grid(row=5, column=2)

# ---[Threading]--------------------------------------------------------------------------------------
threading.Thread(target=realTimeUpdateMeasurement).start()

root.mainloop()