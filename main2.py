from time import sleep
from pyautogui import click, locateOnScreen, mouseDown, moveTo
from gps import dominios
from ssh import chave
from codes.oracle import login_oracle
from codes.cloud import login_cloud
from codes.coleta import acolhimento
from codes.popups import fechar_popups
from codes.senha import mudar_senha
from codes.servidor import instancia
from codes.pontes import ponte
from codes.configs import configuracao

dados = []
url = 'https://learn.oracle.com/ols/course/solution-development-using-oci-go-and-typescript-sdk/35644/84140#'

sleep(5)


login_oracle("tammymoo.ms.0.91.99.5@gmail.com", "123456Jr@")

acolhimento()

moveTo(1013, 465)
mouseDown(button='left')
sleep(2)
moveTo(1277, 465)
click(button='right')
moveTo(1012, 520)
sleep(0.5)
click()
sleep(5)

login_cloud(dados[1], dados[2])
moveTo(105, 487)
sleep(5)
ver = locateOnScreen('./img/btn.png')
if ver is None:
    mudar_senha()
    sleep(5)

else:
    login_cloud(dados[1], '123456Jr@a')

fechar_popups()

instancia()


local = dominios["3"]

ponte()
configuracao(chave, local[0], local[1])
