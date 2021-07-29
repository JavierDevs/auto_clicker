import pyautogui as auto
import keyboard
from time import sleep

while True:
        auto.click(button='left')     

        if keyboard.is_pressed('escape'):
            while True:
                sleep(1)
