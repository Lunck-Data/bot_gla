import pyautogui
import time
import keyboard

def quit():

    print("10:20 da manhã, vamos aguardar o reset")
    #Deslogar
    pyautogui.moveTo(493, 45)
    pyautogui.click()

    time.sleep(1)

    pyautogui.moveTo(854, 568)
    pyautogui.click()

    #Aguardar o tempo
    contador = 1200

    def timer_forninho(tempo):
        print(f"Iniciando cronômetro de {tempo} segundos para ficar pronto")

        for i in range(tempo, 0, -1):
            print(f"Tempo restante: {i} ", end="\r")
            time.sleep(1)

        print("\n Ficou pronto, LETISGO")

    timer_forninho(contador)

    #Entrar no jogo
    pyautogui.moveTo(965,86)
    pyautogui.click()

    time.sleep(10)

