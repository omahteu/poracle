from time import sleep
from pyautogui import click, moveTo, press, write
from codes.db import dados


def mudar_senha():
    sleep(1)
    moveTo(461, 436)
    click()
    write(dados[1], interval=0.10)
    press("tab")
    write("123456Jr@a", interval=0.10)
    press("tab")
    write("123456Jr@a", interval=0.10)
    press("tab")
    press("enter")
