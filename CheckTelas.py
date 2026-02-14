import pyautogui
import time

def checagemDeTelas():

    try:
        localizacao = pyautogui.locateOnScreen("Jogar.png", confidence=0.65, region=(560, 89, 253, 77))
        pyautogui.moveTo(localizacao)
        time.sleep(1)
        pyautogui.click()
        time.sleep(5)
    except pyautogui.ImageNotFoundException:
        localizacao = None

    try:
        localizacao = pyautogui.locateOnScreen("Loja.png", confidence=0.65, region=(1015, 190, 53, 50))
        pyautogui.moveTo(localizacao)
        pyautogui.click()
    except pyautogui.ImageNotFoundException:
        localizacao = None