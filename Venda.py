import pyautogui
import time
import keyboard

def vendaFrango(menorFrango):
    #Abre o mercado
    pyautogui.moveTo(679, 491)
    pyautogui.click()

    #Publicar
    pyautogui.moveTo(608, 230)
    pyautogui.click()

    #Botao vender
    pyautogui.moveTo(842, 634)
    pyautogui.click()

    #Selecionar
    pyautogui.moveTo(491, 295)
    pyautogui.click()

    time.sleep(2)
    try:
        localizacao = pyautogui.locateOnScreen('frango.png', confidence=0.7)
        pyautogui.moveTo(localizacao)
        pyautogui.click()
    except pyautogui.ImageNotFoundException:
        print("A imagem não está na tela no momento.")
        localizacao = None
        
            #Fechar aba
        pyautogui.click()
        pyautogui.moveTo(1015, 197)
        pyautogui.click()
        return

    #Zerar quantidade
    pyautogui.moveTo(615, 332)
    pyautogui.click()

    pyautogui.moveTo(884, 335)
    for i in range(0,4):
        pyautogui.click()

    #Colocar preco
    pyautogui.moveTo(698, 308)
    pyautogui.click()

    pyautogui.write(menorFrango)

    #Vender
    pyautogui.moveTo(627, 591)
    pyautogui.click()

    #Confirmação
    pyautogui.moveTo(689, 498)
    pyautogui.click()

    #Fechar aba
    pyautogui.moveTo(1015, 197)
    pyautogui.click()

def vendaPaella(menorPaella):
    #Abre o mercado
    pyautogui.moveTo(679, 491)
    pyautogui.click()

    #Publicar
    pyautogui.moveTo(608, 230)
    pyautogui.click()

    #Botao vender
    pyautogui.moveTo(842, 634)
    pyautogui.click()

    #Selecionar
    pyautogui.moveTo(491, 295)
    pyautogui.click()

    time.sleep(2)
    try:
        localizacao = pyautogui.locateOnScreen('paella.png', confidence=0.7)
        pyautogui.moveTo(localizacao)
        pyautogui.click()
    except pyautogui.ImageNotFoundException:
        print("A imagem não está na tela no momento.")
        localizacao = None

            #Fechar aba

        pyautogui.click()
        pyautogui.moveTo(1015, 197)
        pyautogui.click()
        return

    #Zerar quantidade
    pyautogui.moveTo(615, 332)
    pyautogui.click()

    pyautogui.moveTo(884, 335)
    for i in range(0,4):
        pyautogui.click()

    #Colocar preco
    pyautogui.moveTo(698, 308)
    pyautogui.click()

    pyautogui.write(menorPaella)

    #Vender
    pyautogui.moveTo(627, 591)
    pyautogui.click()

    #Confirmação
    pyautogui.moveTo(689, 498)
    pyautogui.click()

    #Fechar aba
    pyautogui.moveTo(1015, 197)
    pyautogui.click()
