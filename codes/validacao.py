from codes.senha import mudar_senha
from codes.cloud import login_cloud
from codes.db import dados
from pyautogui import locateOnScreen, moveTo
from time import sleep


def confirmacao():
    moveTo(105, 487)
    sleep(1)
    ver = locateOnScreen('./img/btn.png')
    if ver is None:
        mudar_senha()
        sleep(5)
    else:
        login_cloud(dados[0], '123456Jr@a')
