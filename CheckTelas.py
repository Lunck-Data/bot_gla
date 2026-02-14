import pyautogui
import time
import keyboard
import Checagem

def checagemDeTelas():

    try:
        localizacao = pyautogui.locateOnScreen("Jogar.png", confidence=0.65, region=(804, 36, 323, 102))
        pyautogui.moveTo(localizacao)
        pyautogui.click()
        time.sleep(5)
    except pyautogui.ImageNotFoundException:
        localizacao = None

    try:
        localizacao = pyautogui.locateOnScreen("Loja.png", confidence=0.65, region=(1298, 302, 42, 39))
        pyautogui.moveTo(localizacao)
        pyautogui.click()
    except pyautogui.ImageNotFoundException:
        localizacao = None

checagemDeTelas()