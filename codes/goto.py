from pyautogui import click, mouseDown, moveTo
from time import sleep


def encaminhar():
    moveTo(1013, 465)
    mouseDown(button='left')
    sleep(2)
    moveTo(1277, 465)
    click(button='right')
    moveTo(1012, 520)
    sleep(0.5)
    click()
    sleep(5)
