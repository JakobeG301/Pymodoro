import tkinter as tk
from itertools import count
from tkinter import ttk, Button, Canvas
from datetime import datetime

def currTime():

    global timerSec
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")

    print("[Debug] Current time:", currentTime)

    cTimeBanner.config(text=currentTime)
    root.after(1000, currTime)

def buttonText(state):
    if countTime == 1:
        return "Stop"
    if countTime == 0:
        return "Start"
    else:
        print("Err")


#Funkcja do odliczania czasu 25m = 1500sek
def countDown():
    global remTime, timerSec, timerMin, countTime
    if countTime == 0 or remTime == 0:
        print("[Info] Timer stopped")
        return
    if remTime > 0:
        remTime -= 1
        timerSec = int(remTime%60)
        timerMin = int(remTime//60)
        timerValue = ("{:02}:{:02}").format(timerMin,timerSec)
        print(f'[Info] Remaining time:  {timerValue}')
        timerBanner.config(text=timerValue)
        root.after(1000,countDown)




def changeState():
    global countTime
    countTime = not countTime
    if countTime == 1:
        button1.config(text="Stop")
        countDown()
    if countTime == 0:
        button1.config(text="Start")


remTime = 150
countTime = 0
buttonState = "Test"
timerValue = "Start"

#Creating window
root = tk.Tk()
root.title("Pymodoro")
root.config(bg="#A5B68D")
root.geometry("400x500")
root.resizable(False, False)
bg = tk.PhotoImage(file="background.png")



canvas = Canvas(root, width=400, height=500, bg="#A5B68D" )
# canvas.create_image(0, 0, anchor="nw", image=bg)
# canvas.place(x=0, y=0)

# text = canvas.create_image(200,250, text = "Pymodoro")
#timerText = tk.Label(root, width = 100, height = 30)

cTimeBanner = tk.Label(root, font=("Helvetica", 10))
cTimeBanner.place(x= 170, y = 50, width=60, height= 30)

timerBanner = tk.Label(root, text = timerValue, font=("Helvetica",60))
timerBanner.place(x = 100, y=210, width=200, height=80)

button1 = Button(root, text = "Start", command=lambda:changeState())
button1.place(x=175, y=350, width=50,height=40)
# button2 = Button(root, text = "Stop")
# button3 = Button(root, text = "Cancel")
# button4 = Button(root, text = "Leave", command = root.destroy)
currTime()

root.mainloop()
