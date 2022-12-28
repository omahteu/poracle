from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pyautogui import locateOnScreen, moveTo, click, center
from ssh import chave

'//*[@id="baseplate"]/div[1]/div[1]/div/dialog/div[3]/button[1]'
'//*[@id="oui-viewstack-root"]/div[2]/div[2]/div/div/div/div[3]/div/button[2]'

dados = []
url = 'https://learn.oracle.com/ols/course/solution-development-using-oci-go-and-typescript-sdk/35644/84140#'
option = Options()
option.headless = True
driver = webdriver.Chrome()
driver.get(url)
sleep(1)
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="local-nav"]/div/div/div[1]/button').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="signInOut2"]').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="sso_username"]').click()
sleep(1)
ActionChains(driver).send_keys("bliesemata.hd.hm.7.82@gmail.com").perform()
sleep(0.2)
ActionChains(driver).send_keys("\ue004").perform()
sleep(0.2)
ActionChains(driver).send_keys("123456Jr@").perform()
sleep(0.2)
ActionChains(driver).send_keys("\ue004").perform()
sleep(1)
ActionChains(driver).send_keys("\ue007").perform()
sleep(5)
driver.find_element(By.XPATH, '//*[@id="tabLab"]').click()
sleep(1)
local = driver.find_element(By.XPATH, '//*[@id="lab"]/div/header[1]')
local.click()
sleep(1)
base = driver.find_elements(By.XPATH, '//*[@id="iladditionalInformationEnv1_1"]')
for c in base:
    texto = c.text
    texto_lista = texto.split()
    try:
        dados.append(texto_lista[20])
        dados.append(texto_lista[57])
        dados.append(texto_lista[59])
        dados.append(str(texto_lista[60]).split(":")[1])
    except IndexError:
        pass
sleep(1)
driver.get(f'{str(dados[0])}')
sleep(5)
driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div[3]/div[3]/div/button').click()
sleep(1)
nome = driver.find_element(By.XPATH, '//*[@id="username"]')
ActionChains(driver).scroll_to_element(nome)
sleep(1)
nome.click()
sleep(1)
ActionChains(driver).send_keys(f'{str(dados[1])}').perform()
sleep(1)
ActionChains(driver).send_keys("\ue004").perform()
sleep(1)
ActionChains(driver).send_keys(f'{str(dados[2])}').perform()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="submit-native"]').click()
sleep(2)
ver = driver.find_elements(By.XPATH, '//*[@id="submit-native"]')
sleep(1)
if len(ver) > 0:
    driver.find_element(By.XPATH, '//*[@id="username"]').click()
    sleep(1)
    ActionChains(driver).send_keys(f'{str(dados[1])}').perform()
    sleep(1)
    ActionChains(driver).send_keys("\ue004").perform()
    sleep(1)
    ActionChains(driver).send_keys('123456Jr@a').perform()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="submit-native"]').click()
sleep(10)
driver.find_element(By.XPATH, '/html/body/section/div[1]/div[3]/main/div[1]/div['
                              '2]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div/div['
                              '2]/div[1]/a/span[1]').click()
sleep(10)

for e in range(0, 11):
    sleep(0.1)
    ActionChains(driver).send_keys("\ue004").perform()

sleep(0.1)
ActionChains(driver).send_keys('\ue007').perform()
sleep(0.1)
ActionChains(driver).send_keys(f"{str(dados[1][0:8])}").perform()
sleep(0.5)
ActionChains(driver).send_keys("\ue015").perform()
sleep(0.3)
ActionChains(driver).send_keys('\ue007').perform()
sleep(3)

for f in range(0, 9):
    sleep(0.1)
    ActionChains(driver).send_keys("\ue004").perform()

sleep(0.1)
ActionChains(driver).send_keys('\ue007').perform()
sleep(5)

# INSTÂNCIA 1
for g in range(0, 3):
    sleep(0.1)
    ActionChains(driver).send_keys("\ue004").perform()

sleep(0.5)
ActionChains(driver).send_keys('\ue007').perform()

for h in range(0, 4):
    sleep(0.1)
    ActionChains(driver).send_keys("\ue004").perform()

sleep(0.5)
ActionChains(driver).send_keys('\ue007').perform()
sleep(3)

for j in range(0, 4):
    sleep(0.1)
    ActionChains(driver).send_keys("\ue004").perform()

sleep(1)
hg = locateOnScreen("./img/marca.png")
hgs = center(hg)
moveTo(hgs)
click(button='left')
sleep(0.5)

for k in range(0, 14):
    sleep(0.1)
    ActionChains(driver).send_keys("\ue004").perform()

sleep(0.5)
ActionChains(driver).send_keys('\ue007').perform()

sleep(0.1)
ActionChains(driver).send_keys("\ue004").perform()
sleep(0.1)
ActionChains(driver).send_keys('\ue007').perform()
sleep(0.1)
ActionChains(driver).send_keys("\ue004").perform()
sleep(0.1)
ActionChains(driver).send_keys("\ue004").perform()
sleep(0.1)
ActionChains(driver).send_keys("\ue012").perform()
sleep(0.1)
ActionChains(driver).send_keys('\ue007').perform()

for c in range(0, 47):
    sleep(0.5)
    ActionChains(driver).send_keys("\ue004").perform()

click(button='left')
sleep(1)
# for m in range(0, 12):
#     sleep(0.1)
#     ActionChains(driver).send_keys("\ue004").perform()
#
# sleep(0.5)
# ActionChains(driver).send_keys('\ue007').perform()
# sleep(1)
#
# for a in range(0, 5):
#     sleep(0.1)
#     ActionChains(driver).send_keys("\ue004").perform()
#
# ActionChains(driver).send_keys('\ue014').perform()
#
# for b in range(0, 11):
#     sleep(0.1)
#     ActionChains(driver).send_keys("\ue004").perform()
#
# ActionChains(driver).send_keys('\ue014').perform()
# ActionChains(driver).send_keys('\ue014').perform()
# ActionChains(driver).send_keys("\ue004").perform()
# ActionChains(driver).send_keys(f"{str(chave)}").perform()
#
# for d in range(0, 11):
#     sleep(0.1)
#     ActionChains(driver).send_keys("\ue004").perform()
#
# sleep(0.5)
# # ActionChains(driver).send_keys('\ue007').perform()
# sleep(5)






# # INSTÂNCIA 2
# ActionChains(driver).send_keys("\ue004").perform()
# sleep(0.5)
# ActionChains(driver).send_keys("\ue004").perform()
# sleep(0.5)
# ActionChains(driver).send_keys("\ue004").perform()
# sleep(0.5)
# ActionChains(driver).send_keys('\ue014').perform()
# sleep(0.5)
# ActionChains(driver).send_keys('\ue007').perform()
#
#
#
# # INSTÂNCIA 3
# ActionChains(driver).send_keys("\ue004").perform()
# sleep(0.5)
# ActionChains(driver).send_keys("\ue004").perform()
# sleep(0.5)
# ActionChains(driver).send_keys("\ue004").perform()
# sleep(0.5)
# ActionChains(driver).send_keys('\ue012').perform()
# sleep(0.5)
# ActionChains(driver).send_keys('\ue007').perform()

sleep(90)
driver.quit()
