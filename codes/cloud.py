from time import sleep
from pyautogui import click, moveTo, scroll, write


def login_cloud(usuario, senha):
    sleep(1)
    moveTo(924, 684)
    click()
    scroll(-500)
    moveTo(452, 425)
    click()
    write(usuario, interval=0.10)
    moveTo(462, 504)
    click()
    write(senha, interval=0.10)
    moveTo(452, 556)
    click()
    sleep(1)
