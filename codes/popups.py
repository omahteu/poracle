from time import sleep
from pyautogui import center, click, locateOnScreen, moveTo


def fechar_popups():
    sleep(1)
    popup1 = locateOnScreen("./img/pop1.png")
    if popup1 is None:
        popup2 = locateOnScreen("./img/skip2.png")
        print(popup2)
        if popup2 is None:
            popup3 = locateOnScreen("./img/fechar.png")
            if popup3 is None:
                pass
            else:
                fechando = center(popup3)
                moveTo(fechando)
                click()
        else:
            fechando2 = center(popup2)
            moveTo(fechando2)
            click()
    else:
        fecha1 = center(popup1)
        moveTo(fecha1)
        sleep(1)
        moveTo(272, 760)
        click()
