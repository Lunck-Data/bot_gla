import pyautogui
import time
import keyboard
import Checagem

def ChecarCompra(nomeItem):
    #Abre o mercado
    pyautogui.moveTo(680, 489)
    pyautogui.click()

    time.sleep(1)

    #Pedido de compra
    pyautogui.moveTo(751, 233)
    pyautogui.click()

    time.sleep(0.5)

    #Clicar no nome
    pyautogui.moveTo(833, 274)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()

    #Pesquisar item compra
    pyautogui.write(nomeItem)

    pyautogui.moveTo(966, 273)
    pyautogui.click()

    time.sleep(2)
    preco_detectado = Checagem.ler_preco_mercado(907, 310, 92, 35)
    print(f"Menor preço de compra do {nomeItem}: {preco_detectado}")

    vendedor = Checagem.ler_nick_jogador(684, 310, 136, 33)
    print(vendedor)

    #Fechar aba
    pyautogui.moveTo(1012, 194)
    pyautogui.click()

    time.sleep(1)
    return preco_detectado, vendedor