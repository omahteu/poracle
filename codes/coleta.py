from time import sleep
from pyautogui import center, click, locateOnScreen, mouseDown, moveTo
from pyperclip import paste
from codes.db import dados


def acolhimento():
    sleep(1)
    click(x=1104, y=201)
    sleep(0.5)
    click(x=1328, y=253)
    sleep(2)
    moveTo(1038, 586)
    mouseDown(button='left')
    moveTo(1191, 586)
    sleep(1)
    click(button='right')
    lname = locateOnScreen("./img/copiar.png")
    lnamex = center(lname)
    moveTo(lnamex)
    sleep(1)
    click()
    name = paste()
    sleep(1)
    dados.append(name)
    sleep(1)

    moveTo(1031, 603)
    mouseDown(button='left')
    moveTo(1193, 601)
    sleep(1)
    click(button='right')
    lsenha = locateOnScreen("./img/copiar.png")
    lsenhax = center(lsenha)
    moveTo(lsenhax)
    click()
    senha = paste()
    sleep(1)
    dados.append(senha)
    sleep(1)

    moveTo(1052, 630)
    mouseDown(button='left')
    moveTo(1183, 630)
    sleep(1)
    click(button='right')
    lserv = locateOnScreen("./img/copiar.png")
    lservx = center(lserv)
    moveTo(lservx)
    click()
    servi = paste()
    sleep(1)
    dados.append(servi)
    sleep(1)