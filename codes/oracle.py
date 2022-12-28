from time import sleep
from pyautogui import click, moveTo, press, write


def login_oracle(usuario, senha):
    sleep(5)
    write('https://learn.oracle.com/ols/course/solution-development-using-oci-go-and-typescript-sdk/35644/84140#',
          interval=0.05)
    press('enter')
    sleep(5)
    moveTo(1159, 152)
    sleep(1)
    click(x=1142, y=199)
    sleep(5)
    write(usuario)
    sleep(1)
    press("tab")
    sleep(1)
    write(senha)
    press("tab")
    sleep(1)
    press("enter")
    sleep(10)
