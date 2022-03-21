# -------------------------------------------------------------------------------------
# ECE 492 Winter 2022
# Acoustic and Evironment Monitoring System Project
# Desktop Controller App
# -------------------------------------------------------------------------------------
from tkinter import *
#from PIL import ImageTk, Image
from tkinter import messagebox
#import bluetooth
#nearby_devices = bluetooth.discover_devices()
import threading
import time
import fakeParameters

# Initialization
root = Tk()
root.title("AEMS panel")
#root.iconbitmap('/Users/hoyeungching/Desktop/logo.ico')
root.geometry("500x500")

# Function Definitions
def clickStartRec():
    statusBox.delete(0, END)
    statusBox.config(bg="red")
    statusBox.insert(0, "Recording inprogress...")
    messagebox.showinfo("Info", "Recording Started!")

def clickStopRec():
    response1 = messagebox.askyesno("Warning", "Stop Recording?")
    if response1:
        statusBox.config(bg="green")
        statusBox.delete(0, END)
        statusBox.insert(0, "Recording saved!")

def openDebugTerminal():
    topWindow = Toplevel()
    topWindow.title("Debug Terminal")

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

def realTimeUpdateMeasurement():
    while True:
        # update temp
        temperatureBox.delete(0, END)
        temperatureBox.insert(0, str(fakeParameters.getFakeTemp()) + " C")

        # update humi
        humidityBox.delete(0, END)
        humidityBox.insert(0, str(fakeParameters.getFakeHumi()) + " %")

        # update lumi
        luminosityBox.delete(0, END)
        luminosityBox.insert(0, str(fakeParameters.getFakeLumi()) + " W")

        # frequency
        time.sleep(1)

# Setup widegts
# ---------------------------------------------------------------------------------------------
# Device connection
openBlueButton = Button(root, text = "Bluetooth", command=openBluetoothList)
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
statusBox = Entry(root, width=40,fg="white", bg="blue", borderwidth = "5")
statusBox.insert(0, "Welcome to AEMS!")
startRecButton = Button(root, text="Start Rec", padx=40, pady=20, command=clickStartRec, fg="green")
stopRecButton = Button(root, text="Stop Rec", padx=40, pady=20, command=clickStopRec, fg="red")

# Show debug terminal
openTerminalButton = Button(root, text="Open Debug Terminal", command=openDebugTerminal)

# ---------------------------------------------------------------------------------------------

# Set widgets positions
startRecButton.grid(row=1, column=0)
stopRecButton.grid(row=1, column=1)
statusBox.grid(row=0, column=0, columnspan=2)
temperatureBox.grid(row=3, column=0)
humidityBox.grid(row=3, column=1)
temperatureLabel.grid(row=2, column=0)
humidityLabel.grid(row=2, column=1)
openTerminalButton.grid(row=4, column=0)
openBlueButton.grid(row=5, column=0)
connectionStatusBox.grid(row=6, column=0)
disconBlueButton.grid(row=6, column=1)
luminosityLabel.grid(row=7, column=0)
luminosityBox.grid(row=7, column=1)

threading.Thread(target=realTimeUpdateMeasurement).start()

root.mainloop()