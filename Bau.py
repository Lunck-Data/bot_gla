import pyautogui
import time
import keyboard

def bau():
    #Abrir baú
    pyautogui.moveTo(739, 494)
    pyautogui.click()

    #Coletar
    pyautogui.moveTo(1301, 286)
    pyautogui.click()

    #Fechar baú
    pyautogui.moveTo(1350, 287)
    pyautogui.click()
