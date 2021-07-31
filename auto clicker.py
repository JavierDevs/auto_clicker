from appJar.appjar import PauseLogger
import pyautogui
import appJar
import keyboard as key
from time import sleep

def buttonPress(button):
    if(button == "Start"):
        amount = int(app.getEntry("amount"))
        button = app.radioButton("click")
        if(button == "Right Click"):
            button = "right"
        else:
            button = "left"
        for _ in range(amount):
            pyautogui.click(button=button,interval=0,)
    if(button == "End"):
        while True:
            sleep(1)

app = appJar.gui("autoclicker")
app.setSize("600x500")
app.setSticky("new")
app.addLabel("Enter amount of clicks", row=0)
app.addEntry("amount", row=1)
app.addButton("Start", buttonPress, row=3)
app.setSticky("e")
app.radioButton("click", "Right Click", row=2)
app.setSticky("w")
app.radioButton("click", "Left Click", row=2)
app.setSticky("new")
app.addButton("End", buttonPress, row=5)
app.go()
