import pyautogui
import time
import keyboard

def resetMarket():
    for i in range (0,6):
        #Abre o mercado
        pyautogui.moveTo(966, 623)
        pyautogui.click()

        #Publicar
        pyautogui.moveTo(881, 336)
        pyautogui.click()

        #Selecionar Preço
        pyautogui.moveTo(1060,616)
        pyautogui.click()

        #Botao direito
        pyautogui.rightClick()

        #Cancelar
        pyautogui.moveTo(1089, 622)
        pyautogui.click()
    
    #Fechar aba
    pyautogui.moveTo(1289, 300)
    pyautogui.click()