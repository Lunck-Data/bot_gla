import pyautogui
import time
import keyboard

def resetMarket():
    #Abre o mercado
    pyautogui.moveTo(680, 489)
    pyautogui.click()

    #Publicar
    pyautogui.moveTo(614, 231)
    pyautogui.click()

    for i in range (0,6):
        #Selecionar Preço
        pyautogui.moveTo(795, 510)
        pyautogui.click()

        #Botao direito
        pyautogui.rightClick()

        #Cancelar
        pyautogui.moveTo(825, 518)
        pyautogui.click()
    
    #Fechar aba
    pyautogui.moveTo(1015, 197)
    pyautogui.click()