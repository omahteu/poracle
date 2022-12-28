from time import sleep
import pyautogui

sleep(2)
lm = pyautogui.locateOnScreen("./img/ver.png")
print(lm)
