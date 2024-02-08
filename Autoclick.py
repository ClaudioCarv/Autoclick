import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import pyautogui


KEY = KeyCode(char='y')

click = False
mouse = Controller()

def clicker():
    while True:
        if click:
            mouse.click(Button.left, 1)
        time.sleep(0.001)
    
def evento(key):
    if key == KEY:
        global click
        click = not click

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=evento) as listener:
    listener.join()